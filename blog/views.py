from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    posts = Post.objects.all().order_by('-created_at')[:9]  # fetch posts
    return render(request, 'home.html', {'posts': posts})

@login_required
def create_blog_post(request):
    context = {
        'form' : PostForm()
    }
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user 
            form.save()
            return redirect('dashboard')  # or wherever you want
    else:
        form = PostForm()
    return render(request, 'create_post.html', context)

def DeleteBlog(request, id):
    selected_post = Post.objects.get(id=id)
    selected_post.delete()
    return redirect('mypost')

def UpdateBlog(request, id):
    selected_post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=selected_post)
        if form.is_valid():
            form.save()
            return redirect('mypost')
        
    else:
        form = PostForm(instance=selected_post)

    context = {'form' : form}
    return render(request, 'create_post.html', context)