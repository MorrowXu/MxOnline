# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict
from .forms import UserAskForm
from courses.models import Course
import json
# Create your views here.


class OrgView(View):
    """
        课程机构列表功能
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 热门机构
        hot_orgs = all_orgs.order_by('-click_nums')[:5] # 倒序排列
        # 城市
        all_cities = CityDict.objects.all()
        #取出筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        #类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        #排序
        sort = request.GET.get('sort', '')
        if sort: # 如果sort存在
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students') # 用students这个字段倒序
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums') # 用course_nums这个字段倒序
        # 机构数量
        org_nums = all_orgs.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 5, request=request) # 课程机构对象, 每页的机构数, 请求

        orgs = p.page(page)


        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_cities': all_cities,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort,
        })

class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            user_ask = user_ask_form.save(commit=True) # model_form 保存方法
            return HttpResponse(json.dumps({"status":"success"}),
                                content_type='application/json') # ajax传回
        else:
            return HttpResponse(json.dumps({"status":"fail", "msg":"添加出错"}),
                                content_type='application/json')

class OrgHomeView(View):
    """
    机构首页
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3] # 拿到Course外键
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
        })
