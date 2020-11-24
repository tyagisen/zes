from django.contrib import admin
from .models import Blog, Navigation, BlogHead, FooterContact


admin.site.register(Navigation)
admin.site.register(BlogHead)
admin.site.register(Blog)
admin.site.register(FooterContact)
