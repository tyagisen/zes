from django.shortcuts import render
from .models import Blog, Navigation, BlogHead, FooterContact


def blog(request):
    logo = Navigation.objects.all()
    blog_head = BlogHead.objects.all()
    blog = Blog.objects.order_by('-date_published')
    contact = FooterContact.objects.all()

    return render(request, 'blog/blog-grid-2-sidebar.html',
                  {'logo': logo, 'blog': blog, 'blog_head': blog_head, 'contact': contact})


def blog_detail(request, pk):
    logo = Navigation.objects.all()
    blog_detail = Blog.objects.get(id=pk)
    contact = FooterContact.objects.all()
    return render(request, 'blog/blog-detail.html', {'sug': blog_detail, 'logo':logo, 'contact': contact, 'arrange': True})
