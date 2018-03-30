#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : adminx.py
# @Email   : 464580843@qq.com
# Create on 2018/3/30 0030 13:05
import xadmin
from .models import UserAsk, UserCourse, UserFavorite, UserMessage, CourseComments


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time'] # 字段显示格式
    search_fields = ['name', 'mobile', 'course_name'] # 添加搜索
    list_filter = ['name', 'mobile', 'course_name', 'add_time'] # 过滤器筛选


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time'] # 字段显示格式
    search_fields = ['user', 'course'] # 添加搜索
    list_filter = ['user', 'course', 'add_time'] # 过滤器筛选


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time'] # 字段显示格式
    search_fields = ['user', 'fav_id', 'fav_type'] # 添加搜索
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time'] # 过滤器筛选


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time'] # 字段显示格式
    search_fields = ['user', 'message', 'has_read'] # 添加搜索
    list_filter = ['user', 'message', 'has_read', 'add_time'] # 过滤器筛选


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time'] # 字段显示格式
    search_fields = ['user', 'course', 'comments'] # 添加搜索
    list_filter = ['user', 'course', 'comments', 'add_time'] # 过滤器筛选


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
