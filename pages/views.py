from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.core.files.storage import FileSystemStorage
import time
from . import forms
from pages.forms import postyForm
from home.models import posty

def formularz(request):
    if request.method == 'POST':
        form = postyForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.save()

    else:
        form = postyForm()
    
    context = {
        'form': form
    }
    return render(request, 'formularz.html',context)


def post(request):
    query_get = request.GET.get('nr')
    post = posty.objects.filter(id=query_get)
    return render(request, "post.html", {'post': post})