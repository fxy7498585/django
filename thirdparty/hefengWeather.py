
import json, requests


def Weather(params):
    key = '93a6dc7551f24003bf35255ac27bc39e'
    api = ("https://free-api.heweather.net/s6/weather/%s?location=%s&key=%s" % (params['weathertype'], params['location'], key))
    response = requests.get(url=api)
    result = json.loads(response.text)
    print('result', result)
    basic = result.get('HeWeather6')[0].get('basic')
    update = result.get('HeWeather6')[0].get('update')
    status = result.get('HeWeather6')[0].get('status')
    now = result.get('HeWeather6')[0].get('now')
    response = dict()
    response['basic'] = basic
    response['update'] = update
    response['status'] = status
    response['now'] = now
    print(response)
    return response


if __name__ == '__main__':
    data = Weather({"location": "shanghai", "weathertype": "now"})
