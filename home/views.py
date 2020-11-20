from .models import Home
from django.shortcuts import render


def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {'image': home})
