from django.shortcuts import render, redirect
from django.contrib.auth import logout
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

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')   # your dashboard url name
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def search(request):
    query = request.GET.get("q")
    results = []
    if query:
        results = Post.objects.filter(title__icontains=query)  # case-insensitive search
    
    return render(request, "search_results.html", {"results": results, "query": query})