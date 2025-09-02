from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from blog.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # creates session
            return redirect("dashboard")
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
    post_list = Post.objects.all().order_by('-created_at')  # fetch posts from db
    paginator = Paginator(post_list, 9)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'dashboard.html', {'posts': posts})

@login_required(login_url='/user/login')
def Detail_view(request, id):
    selected_post = Post.objects.get(id=id)
    return render(request, 'detail_view.html', {'post': selected_post})

@login_required(login_url='/user/login')
def MyPosts(request):
    posts = Post.objects.filter(author = request.user).order_by('-created_at')
    return render(request, 'own_posts.html', {'posts': posts})
    
@login_required(login_url='/user/login')
def EditUser(request, id):
    user = User.objects.get(id=id)
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = ProfileEditForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("dashboard")  # ✅ will redirect properly
        
    else:
        user_form = ProfileEditForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {
        "user_form": user_form,
        "profile_form": profile_form,
        "user": user
    })

def EditPass(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()  
            update_session_auth_hash(request, user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user)

    return render(request, 'changepass.html', {"form":form, "user": user})

def Profilepage(request):
    return render(request, 'profile.html')
