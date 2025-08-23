from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
def user(request):
    userss = User.objects.all()
    return render(request, 'user.html', {'userss': userss})

def createUser(request):
    context = {
        'form': RegisterForm()
    }

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = RegisterForm()

    return render(request, 'create_user.html', context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now login.")
            return redirect('user')  # redirect to login page
    else:
        form = RegisterForm()
    return render(request, 'create_user.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')  # change 'home' to your homepage URL name
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')