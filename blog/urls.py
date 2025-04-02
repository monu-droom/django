from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('remove-blog/<int:id>', views.remove_blog, name='remove_blogs'),
    path('view-blog/<int:id>', views.blog, name='blog'),
    path('update-blog', views.update_blog, name='update_blog'),
]
