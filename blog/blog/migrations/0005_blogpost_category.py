# Generated by Django 3.2.8 on 2023-09-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.IntegerField(choices=[(0, 'Experiences'), (1, 'Code')], default=0),
        ),
    ]
