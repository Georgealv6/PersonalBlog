from django.shortcuts import render
from django.http import HttpResponse
from .models import Carousel


def homepage(request):
    carousel = Carousel.objects.all()
    context = {"carousel": carousel}
    return render(request, "blog/homepage.html", context)
