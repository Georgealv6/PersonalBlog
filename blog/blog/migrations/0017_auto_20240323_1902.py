# Generated by Django 3.2.8 on 2024-03-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_carousel_sub_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pics/%y/%m/%d/')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='gallery',
            field=models.ManyToManyField(blank=True, to='blog.Image'),
        ),
    ]
