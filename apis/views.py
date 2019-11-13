from django.http import HttpResponse, JsonResponse, FileResponse, Http404
import json
import requests
from thirdparty import hefengWeather
import os
from miniPragram import settings
import yaml
from utils import response


def weather(request):
    # http://127.0.0.1:8000/apis/weather?liocation=北京&weathertype=now
    if request.method == 'GET':
        print('request', request.GET)
        params = {
            "location":request.GET.get('location'),
            "weathertype": request.GET.get('weathertype'),
        }
        print('params', params)
        data = hefengWeather.Weather(params)
        return JsonResponse(data=data, status = 200)
    elif request.method == 'POST':
        receive_body = request.body
        receive_body = json.loads(receive_body)
        params = {
            "location": receive_body.get('location'),
            "weathertype": receive_body.get('weathertype'),
        }
        print('requestBody', params)
        data = hefengWeather.Weather(params)
        return JsonResponse(data=data, status=200)


def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps


def get_menu(request):
    print('get_menu')
    global_app_data = init_app_data()
    print('global_app_data', global_app_data)
    published_app_data = global_app_data.get('published')
    responseData = response.wrap_json_response(data=published_app_data,
                                                 code=response.RetureCode.SUCCESS)
    return JsonResponse(data=responseData, safe=False)


def image(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        print('imgfile', imgfile)
        if not os.path.exists(imgfile):
            return Http404()
        else:
            data = open(imgfile, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')


def image_text(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return response.wrap_json_response(code=response.RetureCode.SUCCESS)
        else:
            response_data = {}
            response_data['name'] = md5 + '.jpg'
            response_data['url'] = '/apis/iamge?md5=%s' % (md5)
            res_data = response.wrap_json_response(data=response_data)
            return JsonResponse(data=res_data, safe=False)
