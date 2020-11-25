from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Navigation(models.Model):
    logo = models.ImageField(upload_to='logo')
    is_active = models.BooleanField(unique=True, blank=True)


class BlogHead(models.Model):
    title = models.CharField(max_length=100)
    background_image = models.ImageField(default='default.jpg', upload_to='blog-background')
    is_active = models.BooleanField(unique=True, blank=True)


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=100)
    blog_sub_title = models.CharField(max_length=100, blank=True)
    blog_image = models.ImageField(upload_to='blog')
    description = RichTextField()
    date_published = models.DateTimeField(auto_now_add=True)
    blog_category = models.CharField(max_length=50)


class FooterContact(models.Model):
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    is_valid = models.BooleanField(unique=True, blank=True)