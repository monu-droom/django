from django.urls import path, include
from . import views

urlpatterns = [
    path('play', views.rpc, name='rpc')
]
