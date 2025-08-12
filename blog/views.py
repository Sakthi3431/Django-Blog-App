from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.
def Home(request):
    return render(request, 'home.html')
