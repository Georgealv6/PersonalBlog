from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("lifestyle/<str:Lifestyle>/", views.experiencepage, name="lifestyle"),
    path("post/<slug:slug>/", views.postdetail, name="post_detail"),
]
