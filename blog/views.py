from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    posts = Post.objects.all().order_by('-created_at')[:9]  # fetch posts
    return render(request, 'home.html', {'posts': posts})

@login_required(login_url='/user/login')
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

@login_required(login_url='/user/login')
def DeleteBlog(request, id):
    selected_post = Post.objects.get(id=id)
    selected_post.delete()
    return redirect('mypost')

@login_required(login_url='/user/login')
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

@login_required(login_url='/user/login')
def search(request):
    query = request.GET.get("q")
    results = []
    if query:
        results = Post.objects.filter(title__icontains=query)  # case-insensitive search
    
    return render(request, "search_results.html", {"results": results, "query": query})

@login_required(login_url='/user/login')
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user or request.user == comment.post.author:
        comment.delete()
    else:
        pass

    return redirect("detail_view", id= comment.post.id)

@login_required(login_url='/user/login')
def trending_post(request):
    posts = Post.objects.all().order_by('-views')  # fetch posts
    return render(request, 'trending_post.html', {'posts': posts})