from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.createUser, name='create_user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]