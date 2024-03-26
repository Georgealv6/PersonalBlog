from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("posts/lifstyle", views.lifestyleposts, name="lifestyle"),
    path("posts/code", views.codeposts, name="code"),
    path("post/<slug:slug>/", views.postdetail, name="post_detail"),
    path("post/<int:blog_id>", views.gallery, name="post_detail"),
]
