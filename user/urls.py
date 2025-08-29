from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPage, name='login'),
    path('register/', views.RegisterPage, name='register'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('dashboard/<int:id>/', views.Detail_view, name='detail_view'), 
    path('edit-profile/<int:id>/', views.EditUser, name='edituser'), 

]