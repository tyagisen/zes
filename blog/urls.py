from django.urls import path, include
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.blog_detail, name='blog-detail'),

]
