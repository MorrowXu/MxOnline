#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : forms.py
# @Email   : 464580843@qq.com
# Create on 2018/3/31 0031 9:46
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=16) # 必填
    password = forms.CharField(required=True,min_length=5) # 必填


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5) # 必填
    captcha = CaptchaField()
