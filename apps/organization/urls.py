#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : urls.py
# @Email   : 464580843@qq.com
# Create on 2018/4/3 13:53
from django.conf.urls import url, include

from .views import OrgView, AddUserAskView,OrgHomeView
urlpatterns = [
    # 课程机构列表
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),

]
