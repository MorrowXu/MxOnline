#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : adminx.py.py
# @Email   : 464580843@qq.com
# Create on 2018/3/30 0030 10:34
import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    '''xadmin主题设置'''
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    '''xadmin全局设置'''
    site_title = '慕学后台管理系统' # 顶部title
    site_footer = '慕学在线网' # 底部
    menu_style = 'accordion' # app菜单收起


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time'] # 字段显示格式
    search_fields = ['code', 'email', 'send_type'] # 添加搜索
    list_filter = ['code', 'email', 'send_type', 'send_time'] # 过滤器筛选


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time'] # 字段显示格式
    search_fields = ['title','image','url','index'] # 添加搜索
    list_filter = ['title','image','url','index','add_time'] # 过滤器筛选


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin) # 表注册
xadmin.site.register(Banner, BannerAdmin) # 轮播图注册
xadmin.site.register(views.BaseAdminView, BaseSetting) # 注册xadmin主题功能
xadmin.site.register(views.CommAdminView, GlobalSetting) # 注册后台左上角和底部title
