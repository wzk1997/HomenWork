from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from hashlib import sha384


def index(req):
    if req.method == 'GET':
        own=models.Article.objects.all()
        context={
            'own':own
        }
        return render(req, 'myblog/acticle_list.html',context)


def login(req):
    if req.method == 'GET':
        return render(req, 'myblog/login.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('pwd')
        try:
            models.User.objects.get(name=name, password=password)
            return render(req, 'myblog/index.html')
        except:
            return render(req, 'myblog/login.html')


def regist(req):
    if req.method == 'GET':
        return render(req, 'myblog/register.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('pwd')
        addreg = models.User(name=name, password=password)
        print(name, password)
        addreg.save()
    return render(req, 'myblog/register_success.html')


def default(req):
    if req.method == 'GET':
        return render(req, 'myblog/default.html')


def article(req):
    if req.method == 'GET':
        return render(req, 'myblog/article.html')
    elif req.method == 'POST':
        title = req.POST.get('title')
        coutext = req.POST.get('coutext')
        author = req.POST.get('author')
        upload = models.Article(title=title, coutext=coutext,author=author)
        upload.save()
    return render(req, 'myblog/index.html')


def article_list(req):
    if req.method == 'GET':
        return render(req, 'myblog/article_list.html')


def article_detail(req):
    if req.method == 'GET':
        return render(req, 'myblog/article_detail.html')
# Create your views here.
