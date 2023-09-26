from django.shortcuts import render
from django.http import HttpResponse
from .models import Carousel, BlogPost


def homepage(request):
    carousel = Carousel.objects.all()
    post = BlogPost.objects.all()
    context = {"carousel": carousel, "post_detail": post}
    return render(request, "blog/homepage.html", context)


def detail(request):
    post = BlogPost.objects.all()
    context = {"post_detail": post}
    return render(request, "blog/post/detail.html", context)
