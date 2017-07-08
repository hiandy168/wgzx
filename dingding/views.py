import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Member, Group


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
        group = [i.name for i in member.group.all()]
        lists = {'name': member.name, 'remark': member.remark, 'num': member.num, 'phone': member.phone, 'group': group}
    return HttpResponse(json.dumps(lists),content_type='application/json')


def post(request):
    print(request.post['name'])
    return HttpResponse(request.post['name'])
