from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def posts(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,'blog/posts.html', {'posts': posts})