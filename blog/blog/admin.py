from django.contrib import admin
from .models import Carousel, BlogPost, Image
from .forms import GalleryForm

# Register your models here.
admin.site.register(Carousel)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "category", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, PostAdmin)

class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm

admin.site.register(Image)
