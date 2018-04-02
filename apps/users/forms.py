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
    username = forms.CharField(required=True,max_length=30) # 必填
    password = forms.CharField(required=True,min_length=6) # 必填


class RegisterForm(forms.Form):
    """增加验证码认证类"""
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=6) # 必填
    captcha = CaptchaField(error_messages={'invalid':'验证码填写错误'}) # error_message 定义验证码错误提示


class ForgetForm(forms.Form):
    """增加验证码认证类"""
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码填写错误'}) # error_message 定义验证码错误提示


class ModifyPwdForm(forms.Form):
    """增加验证码认证类"""
    password1 = forms.CharField(required=True,min_length=6) # 必填
    password2 = forms.CharField(required=True,min_length=6) # 必填
