from django.urls import path, include
from . import views

urlpatterns = [
    path('play', views.find_ball, name="find_ball")
]
