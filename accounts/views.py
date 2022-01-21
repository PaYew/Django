from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
import time
from django.db import models
from .models import posty
from home.models import posty
from django.apps import apps

# Create your views here.

def register(request):
    if request.method == 'POST':

        if 'reg' in request.POST:
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']

            tak='tak'
            nie='nie'

            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Login zajety')
                    return render(request,'register.html', {'stan':nie})
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email zajety')
                    return render(request,'register.html', {'stan':nie})
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, is_staff=False)
                    user.save()
                    messages.info(request,'Użytkownik utworzony, możesz się zalogować.')
                    return render(request,'register.html', {'stan':tak})

            else:
                messages.info(request,'Podane hasła nie są takie same.')
                return render(request, 'register.html', {'stan':nie})
        else:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')

            else:
                messages.info(request, 'Wpisz poprawne dane')
                return redirect('register')
    else:
        return render(request, 'register.html')
        

def profile(request):
    id = request.user
    post = posty.objects.filter(author_id=id)
    return render(request, 'profile.html', {'post': post})

def logout(request):
    auth.logout(request)
    return redirect('/')


