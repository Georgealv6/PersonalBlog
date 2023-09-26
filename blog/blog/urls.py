from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<slug:slug>/", views.BlogPost, name="blogpost"),
]
