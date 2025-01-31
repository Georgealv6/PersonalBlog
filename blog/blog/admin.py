from django.contrib import admin
from .models import Carousel, BlogPost, BlogPostImage


# from .forms import GalleryForm
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "category", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Carousel)
admin.site.register(BlogPost, PostAdmin)


class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 3  # Allows uploading multiple imgs at once


class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogPostImageInline]


admin.site.register(BlogPostImage)
