from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("posts/lifstyle", views.lifestyleposts, name="lifestyle"),
    path("posts/code", views.codeposts, name="code"),
    path("post/<slug:slug>/", views.postdetail, name="post_detail"),
    path("post/<int:post_id>", views.postdetail, name="post_detail"),
]
