from django.urls import path

from . import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('menu/', views.get_menu, name='menu'),
    path('image/', views.image, name='image'),
    path('imagetext/', views.image_text, name='imagetext')
]