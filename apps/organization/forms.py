#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : forms.py
# @Email   : 464580843@qq.com
# Create on 2018/4/3 13:46
import re
from django import forms

from operation.models import UserAsk

class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk # 继承这个model
        fields = ['name', 'mobile', 'course_name'] # 放入需要的字段

    def clean_mobile(self):
        """
        验证手机号码是否合法
        :return:
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')

