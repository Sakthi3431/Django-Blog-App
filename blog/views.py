from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def Home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def create_blog_post(request):
    context = {
        'form' : PostForm()
    }
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # or wherever you want
    else:
        form = PostForm()
    return render(request, 'create_post.html', context)
