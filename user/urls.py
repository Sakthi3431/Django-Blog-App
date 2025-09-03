from django.urls import path
from . import views
from .views import detail_view

urlpatterns = [
    path('login/', views.LoginPage, name='login'),
    path('register/', views.RegisterPage, name='register'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('edit-profile/<int:id>/', views.EditUser, name='edituser'), 
    path('profile/', views.Profilepage, name='profile'), 
    path('profile/change-pass/<int:id>/', views.EditPass, name='changepass'), 
    path("post/<int:id>/", detail_view, name="detail_view"),
]