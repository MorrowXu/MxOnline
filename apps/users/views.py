# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q # 或运算
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email

# Create your views here.


class CustomBackend(ModelBackend):
    """重写authenticate,兼容邮箱认证"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):

    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        if all_record: # 激活码已存在,则...
            for record in all_record:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else: # 不存在则返回一个404
            return render(request, 'active_failed.html', {'msg': '链接失效'})
        return render(request, 'login.html', {})


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form' : register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", '')
            if UserProfile.objects.filter(email=user_name): # 检查用户是否已经存在
                return render(request, 'register.html', {'register_form': register_form,'msg': '用户已经存在', })
            pass_word = request.POST.get("password", '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_email(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html',{'register_form': register_form,})
            pass


class LoginView(View):

    def get(self,request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", '')
            pass_word = request.POST.get("password", '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {})
                else:
                    return render(request, 'login.html', {'msg': '用户未激活', })
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误',})

        else:
            return render(request, 'login.html', {'login_form':login_form,})


class ForgetPwdView(View):

    def get(self, request):
        forget_from = ForgetForm(request.POST)

        return render(request, 'forgetpwd.html', {'forget_from':forget_from})

    def post(self, request):
        forget_from = ForgetForm(request.POST)
        if forget_from.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, send_type='forget')
            return render(request, 'send_success.html',{})
        else:
            return render(request, 'forgetpwd.html', {'forget_from': forget_from})


class ResetView(View):

    def get(self, request, reset_code):
        all_record = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_record: # 激活码已存在,则...
            for record in all_record:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})

        else: # 不存在则返回一个404
            return render(request, 'active_failed.html', {'msg': '链接失效'})
        return render(request, 'login.html', {})

class ModifyPwdView(View):

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get("email", '')
            print email
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email,
                                                               'msg': '密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, 'login.html')

        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'email': email,
                                                           'modify_form': modify_form})

