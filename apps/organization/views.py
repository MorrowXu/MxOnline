# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict
# Create your views here.


class OrgView(View):
    """
        课程机构列表功能
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 城市
        all_cities = CityDict.objects.all()
        return render(request, 'org-list.html', {
            'all_orgs': all_orgs,
            'all_cities': all_cities,
        })
