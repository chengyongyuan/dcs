#-*- coding:utf8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='datapanel/login')
def index(req):
    return render(req, 'datapanel/index.html')

def login(req):
    if req.POST:
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login_user(req, user)
            return redirect('/datapanel/')
        else:
            return render(req, 'datapanel/login.html', {'login_error':True})
    return render(req, 'datapanel/login.html')
