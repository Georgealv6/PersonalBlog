# Generated by Django 3.2.8 on 2025-01-31 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_rename_image_blogpostimage_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPostImage',
        ),
    ]
