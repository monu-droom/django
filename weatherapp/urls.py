from django.urls import path
from . import views

urlpatterns = [
    path('get-weather', views.get_weather, name='get_weather'),   
    path('fetch-weather', views.fetch_weather, name='fetch_weather'),      
]