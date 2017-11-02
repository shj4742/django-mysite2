from django.shortcuts import render

# Create your views here.
from hashlib import sha1
from .models import UserInfo


def index(request):
    return render(request, 'index.html')


def find_doctor(request):
    return render(request, 'find_doctor.html')


def classic_answer(request):
    return render(request, 'classic_answer.html')


def health_info(request):
    return render(request, 'health_info.html')


def repository(request):
    return render(request, 'repository.html')


def calorie_counter(request):
    return render(request, 'calorie_counter.html')


def login(request):
    return render(request, 'login.html')

def registe(request):
    return render(request, 'register.html')

def registe_handle(request):
    #获取form post
    post = request.POST
    name = post['username']
    pwd = post['userpwd']
    #加密密码
    pwd_jm = sha1(pwd.encode('utf-8')).hexdigest()
    list = UserInfo.objects.filter()


