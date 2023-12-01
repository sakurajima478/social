from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegisterFrom, LoginUser


def register_view(request):
    if request.method == 'GET':
        return render(request, 'pages/register.html', context={
            'form' : UserRegisterFrom,
        })
        
    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                messages.success(request, 'User registered successfully!')
                return redirect('blog:posts')
            
            except IntegrityError:
                messages.warning(request, 'User already exists')
                return render(request, 'pages/register.html', context={
                    'form' : UserRegisterFrom,
                })
          
        messages.warning(request, 'Password not match!')      
        return render(request, 'pages/register.html', context={
            'form' : UserRegisterFrom,
        })
    

def login_view(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html', context={
            'form' : LoginUser,
        })
    
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.warning(request, 'Username or Password incorrect')
            return render(request, 'pages/login.html', context={
                    'form' : LoginUser,
                })
        else:
            login(request, user)
            return redirect('blog:posts')

def logout_view(request):
    logout(request)
    return redirect('login')