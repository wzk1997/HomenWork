from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from . import models
from . import utils
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
@csrf_exempt
#博客主页
def index(req):
    return render(req, 'myblog/index.html')
#登陆页面
@csrf_exempt
def login(req):
    if req.method == 'GET':
        return render(req, 'myblog/login.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('pwd')
        code = req.POST.get('code')
        if code == req.session['check_code']:
            try:
                print(code)
                models.User.objects.get(name=name, password=password)
                return render(req, 'myblog/index.html')
            except:
                return render(req, 'myblog/login.html')
        else:
            return render(req, 'myblog/login.html')
@csrf_exempt
#注册页面
def regist(req):
    if req.method == 'GET':
        return render(req, 'myblog/register.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('pwd')
        if 6 < len(password) < 18:
            return HttpResponse('<h1>密码需在6~18位之间，请重新注册！</h1>')
        try:
            user = models.User.objects.get(name=name)
            return HttpResponse('<h1>用户名存在</h1>')
        except:
            addreg = models.User(name=name, password=password)
            addreg.save()
            return redirect('user:index')

    return render(req, 'myblog/register_success.html')
@csrf_exempt
#主页
def default(req):
    if req.method == 'GET':
        return render(req, 'myblog/default.html')
@csrf_exempt
#编辑博客
def article(req):
    if req.method == 'GET':
        return render(req, 'myblog/article.html')
    elif req.method == 'POST':
        title = req.POST.get('title')
        coutext = req.POST.get('coutext')
        user = models.User.objects.get(pk=1)
        upload = models.Article(title=title, coutext=coutext, author=user)
        upload.save()
    return render(req, 'myblog/index.html',)
@csrf_exempt
#列表页面
def article_list(req):
        if req.method == 'GET':
            own = models.Article.objects.all()
            print(own)
            context = {
                'own': own
            }
            return render(req, 'myblog/article_list.html',context)
@csrf_exempt
#列表详情
def article_detail(req):
    if req.method == 'GET':
        return render(req, 'myblog/article_detail.html')
@csrf_exempt
#验证码
def addutils(req):
    # 开辟内存空间
    B = BytesIO()
    # 引入utils的产生图片和数字的方法
    img, code = utils.create_code()
    # 保存图片和数字
    req.session['check_code'] = code
    img.save(B, 'PNG')
    return HttpResponse(B.getvalue())
# Create your views here.
@csrf_exempt
def jsontext(req):
    u = models.User.objects.get(pk=1)
    u=model_to_dict(u)
    return JsonResponse(u)