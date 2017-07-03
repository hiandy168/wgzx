from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from .models import Member,Group
import json

@login_required
def index(request):
    return render(request, 'dingding/index.html')
@login_required
def iframe(request,key):
    group_list=[group.name for group in Group.objects.all()]
    member_list=[member.name for member in Member.objects.all()]
    return render(request,'dingding/%s.html'%key)
@login_required
def group(request,key):
    if key=='all':
        group_list = Group.objects.all()
        lists = [group.name for group in group_list]
    else:
        member_list = Member.objects.filter(group=Group.objects.get(name=key))
        lists = [member.name for member in member_list]
    return HttpResponse(json.dumps(sorted(lists[1:])),content_type='application/json')
@login_required
def member(request,key):
    if key=='all':
        member_list = Member.objects.all()
        lists = [member.name for member in member_list]
    else:
        member = Member.objects.get(name=key)
        lists = {'name':member.name,'remark':member.remark,'num':member.num,'phone':member.phone}
    return HttpResponse(json.dumps(lists),content_type='application/json')