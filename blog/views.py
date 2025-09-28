from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, "blog/blogs.html", {"blogs": blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})




