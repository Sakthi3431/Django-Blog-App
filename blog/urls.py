from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import *
from . import views


urlpatterns = [
    path('', views.landing_page, name='home'), 
    path('new/', views.create_blog_post, name='create_post'),
    path('logout/', views.logout_view, name='logout'),
    path('mypost/', MyPosts, name='mypost'),
    path('mypost/delete/<int:id>', views.DeleteBlog, name='deletepost'),
    path('mypost/update/<int:id>', views.UpdateBlog, name='updatepost'),
    path("search/", views.search, name="search"),
    path("comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
]
