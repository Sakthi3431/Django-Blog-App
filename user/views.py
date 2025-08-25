from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from blog.models import *

def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # creates session
            return redirect("dashboard")   # or wherever
        else:
            return render(request, "login_page.html", {"error": "Invalid username or password"})

    return render(request, "login_page.html")

def RegisterPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return render(request, "register_page.html", {"error": "Username already exists!"})
            user = AuthUser.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect("login")
        else:
            return render(request, "register_page.html", {"error": "Passwords do not match!"})

    return render(request, "register_page.html")

@login_required(login_url='/user/login')
def Dashboard(request):
    posts = Post.objects.all().order_by('-created_at')  # fetch posts from db
    return render(request, 'dashboard.html', {'posts': posts})
