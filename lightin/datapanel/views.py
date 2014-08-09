#-*- coding:utf8 -*-
from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'datapanel/index.html')

