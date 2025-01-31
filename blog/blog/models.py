from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.mixins import date

ROUTES = (
    (0, "homepage"),
    (1, "lifestyle"),
    (2, "code"),
)


# Create your models here.
class Carousel(models.Model):
    image = models.ImageField(upload_to="pics/%y/%m/%d/")
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100, blank=True)
    route = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Post
STATUS = ((0, "Draft"), (1, "Publish"))

GENRE = ((0, "Lifestyle"), (1, "Code"))


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    header_image = models.ImageField(upload_to="pics/%y/%m/%d/", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=GENRE, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="images"
    )
    images = models.ImageField(upload_to="blog_images/%y/%m/%d/")

    def __str__(self):
        return f"Image for {self.blog_post.title}"
