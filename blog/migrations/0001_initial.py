# Generated by Django 3.1.3 on 2020-11-22 10:09

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('background_image', models.ImageField(default='default.jpg', upload_to='blog-background')),
            ],
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo')),
                ('is_active', models.BooleanField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_sub_title', models.CharField(max_length=100)),
                ('blog_image', models.ImageField(upload_to='blog')),
                ('description', ckeditor.fields.RichTextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('blog_category', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
