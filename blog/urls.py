from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'), 
    path('new/', views.create_blog_post, name='create_post'),
]
