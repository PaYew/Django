from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from .models import posty

# Create your views here.

def index(request):
    if 'quer' in request.GET:
        query = request.GET.get('quer')
        post = posty.objects.filter(title__icontains=query)

        return render(request, "index.html", {'post': post})
    else:
        post = posty.objects.all()
        return render(request, "index.html", {'post': post})

