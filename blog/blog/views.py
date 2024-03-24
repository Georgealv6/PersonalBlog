from django.shortcuts import get_object_or_404, render
from .models import Carousel, BlogPost, Image


def homepage(request):
    carousel = Carousel.objects.all()
    post = BlogPost.objects.filter(status=1).order_by("created_on")
    context = {"carousel": carousel, "posts": post}
    return render(request, "blog/index.html", context)


def postdetail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {"posts": post}
    return render(request, "blog/posts/detail.html", context)

def gallery(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    img = blog.gallery.all()
    context = {"blog": blog,
               "img": img}
    return render(request, "blog/posts/detail.html", context)

def lifestyleposts(request):
    chosen_category = "0"
    post = BlogPost.objects.filter(category=chosen_category)
    context = {"detail": post, "chosen_category": chosen_category}
    return render(request, "blog/lifestyle/lifestyle.html", context)


def codeposts(request):
    chosen_category = "1"
    post = BlogPost.objects.filter(category=chosen_category)
    context = {"detail": post, "chosen_category": chosen_category}
    return render(request, "blog/code/codepage.html", context)
