# Generated by Django 3.2.8 on 2024-03-26 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='images',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='image',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.blogpost'),
        ),
    ]