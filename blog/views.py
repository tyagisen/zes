from django.shortcuts import render
from .models import Blog, Navigation, BlogHead, FooterContact
from django.core.paginator import Paginator


def blog(request):
    logo = Navigation.objects.all()
    blog_head = BlogHead.objects.all()
    contact = FooterContact.objects.all()
    blog = Blog.objects.order_by('-date_published')
    paginator = Paginator(blog, 4, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog-grid-2-sidebar.html',
                  {'logo': logo, 'blog': page_obj, 'blog_head': blog_head, 'contact': contact})


def blog_detail(request, pk):
    logo = Navigation.objects.all()
    blog_detail = Blog.objects.get(id=pk)
    contact = FooterContact.objects.all()
    return render(request, 'blog/blog-detail.html', {'sug': blog_detail, 'logo':logo, 'contact': contact, 'arrange': True})
