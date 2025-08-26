from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Home, name='home'), 
    path('<int:id>/', views.Detail_view, name='detail_view'), 
    path('new/', views.create_blog_post, name='create_post'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
