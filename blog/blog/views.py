from django.shortcuts import get_object_or_404, render
from .models import Carousel, BlogPost


def homepage(request):
    carousel = Carousel.objects.all()
    post = BlogPost.objects.filter(status=1).order_by("-created_on")
    context = {"carousel": carousel, "posts": post}
    return render(request, "blog/index.html", context)


def postdetail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {"posts": post}
    return render(request, "blog/posts/detail.html", context)


def lifestyleposts(request):
    chosen_category = "0"
    post = BlogPost.objects.filter(category=chosen_category)
    context = {"detail": post, "chosen_category": chosen_category}
    return render(request, "blog/lifestyle/lifestyle.html", context)
