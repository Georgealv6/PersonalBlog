# Generated by Django 3.2.8 on 2023-12-11 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.IntegerField(choices=[(0, 'Lifestyle'), (1, 'Code')], default=0),
        ),
    ]
