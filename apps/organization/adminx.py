#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : adminx.py
# @Email   : 464580843@qq.com
# Create on 2018/3/30 0030 12:12
import xadmin
from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):
    list_display = ['name','desc','add_time'] # 字段显示格式
    search_fields = ['name','desc'] # 添加搜索
    list_filter = ['name','desc','add_time'] # 过滤器筛选


class CourseOrgAdmin(object):
    list_display = ['name','desc','click_nums','fav_nums','image','address','city','add_time'] # 字段显示格式
    search_fields = ['name','desc','click_nums','fav_nums','image','address','city'] # 添加搜索
    list_filter = ['name','desc','click_nums','fav_nums','image','address','city','add_time'] # 过滤器筛选


class TeacherAdmin(object):
    list_display = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time'] # 字段显示格式
    search_fields = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums']# 添加搜索
    list_filter = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time'] # 过滤器筛选


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
