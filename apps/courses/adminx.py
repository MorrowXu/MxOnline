#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : adminx.py
# @Email   : 464580843@qq.com
# Create on 2018/3/30 0030 12:22
import xadmin
from .models import Course, Video, CourseResource, Lesson


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'image', 'click_nums', 'add_time'] # 字段显示格式
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                     'click_nums'] # 添加搜索
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                     'click_nums', 'add_time'] # 过滤器筛选


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time'] # 字段显示格式
    search_fields = ['course', 'name'] # 添加搜索
    list_filter = ['course__name', 'name', 'add_time'] # 过滤器筛选


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time'] # 字段显示格式
    search_fields = ['lesson', 'name'] # 添加搜索
    list_filter = ['lesson', 'name', 'add_time'] # 过滤器筛选


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time'] # 字段显示格式
    search_fields = ['course', 'name', 'download'] # 添加搜索
    list_filter = ['course', 'name', 'download', 'add_time'] # 过滤器筛选

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
