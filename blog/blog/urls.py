from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("post/<slug:slug>/", views.postdetail, name="post_detail"),
]
