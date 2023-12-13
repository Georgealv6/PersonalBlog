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


def codepage(request, Code):
    post = BlogPost.objects.filter(category=Code)
    context = {"pageone": post}
    return render(request, "blog/code/codepage.html", context)


def experiencepage(request, Lifestyle):
    post = BlogPost.objects.filter(category=Lifestyle)
    context = {"pagetwo": post}
    return render(request, "blog/code/experiences.html", context)


# class PostDetail(generic.DetailView):
#     model = BlogPost
#     template_name = "blog/posts/detail.html"
