from django.shortcuts import render
from django.http import HttpResponse
from . import models
from hashlib import sha384


def index(req):
    return render(req, 'myblog/default.html')


def login(req):
    if req.method == 'GET':
        return render(req, 'myblog/login.html')
    elif req.method == 'POST':
        name= req.POST.get('name')
        password=req.POST.get('pwd')
        try:
            models.User.objects.get(name=name,password=password)
            return render(req,'myblog/index.html')
        except:
            return render(req,'myblog/login.html')


def regist(req):
    if req.method == 'GET':
        return render(req, 'myblog/register.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('pwd')
        addreg = models.User(name=name,password=password)
        m=sha384(addreg)
        print(name, password)
        print(m)
        m.save()
    return render(req, 'myblog/register_success.html')

def list(req):
    pass

def detail(req):
    pass
# Create your views here.
