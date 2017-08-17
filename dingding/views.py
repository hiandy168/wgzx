import json
import sys

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Member, Group, Log

sys.path.append('static/')
from api import api

@login_required
def index(request):
    return render(request, 'dingding/index.html', {'user': request.user})

@login_required
def iframe(request, page):
    group_list=[group.name for group in Group.objects.all()]
    member_list=[member.name for member in Member.objects.all()]
    return render(request, 'dingding/%s.html' % page)

@login_required
def data(request):
    if request.POST.get('type') == 'member':
        if request.POST.get('data')=='all':
            member_list = Member.objects.all()
            lists = sorted([[member.name,member.id] for member in member_list])
        else:
            member = Member.objects.get(name=request.POST.get('data'))
            group = [[i.name,i.id] for i in member.group.all()]
            lists = {'id':member.id,'name': member.name, 'remark': member.remark, 'num': member.num, 'phone': member.phone, 'group': group}
    else:
        if request.POST.get('data')=='all':
            group_list = Group.objects.all()
            lists = sorted([[group.name,group.id] for group in group_list][1:])
        else:
            member_list = Member.objects.filter(group=Group.objects.get(name=request.POST.get('data')))
            lists = sorted([[member.name,member.id] for member in member_list])
    return HttpResponse(json.dumps(lists),content_type='application/json')

def replace(input):
    if input==None:
        input=''
    return input

def member(request):
    code,id,name,num,phone,remark,group=request.POST.get('code'),request.POST.get('id'),request.POST.get('name'),request.POST.get('num'),request.POST.get('phone'),request.POST.get('remark'),request.POST.get('group')
    id=replace(id)
    name=replace(name)
    num=replace(num)
    phone=replace(phone)
    remark=replace(remark)
    group=replace(group)
    print([code, id, name, num, phone, remark, group])
    if group == '':
        group = []
    else:
        group = list(set(group.split(';')[:-1]))
    if code == '-1':
        Member.objects.get(id=id).delete()
        return HttpResponse('Success: %s 已删除' % name)
    elif code == '1':
        try:
            Member.objects.get(name=name)
            return HttpResponse('Error: %s 已存在' % name)
        except:
            member = Member.objects.create()
            member.name, member.num, member.phone, member.remark = name, num, phone, remark
            for id in group: member.group.add(id)
            member.save()
            return HttpResponse('Success: %s 已添加' % name)
    else:
        member = Member.objects.get(id=id)
        member.name, member.num, member.phone, member.remark = name, num, phone, remark
        member.group.clear()
        for id in group: member.group.add(id)
        member.save()
        return HttpResponse('Success: %s 已修改' % name)

def group(request):
    group,member_list2=request.POST.get('group'),request.POST.get('member_list')
    member_list1 = Member.objects.filter(group=Group.objects.get(id=group))
    member_list1 = [member.id for member in member_list1]
    if member_list2 == '':
        member_list2 = []
    else:
        member_list2 = list(set(member_list2.split(';')[:-1]))
    minus = [id for id in member_list1 if id not in member_list2]
    add = [id for id in member_list2 if id not in member_list1]
    print(group,minus,add)
    for id in minus:
        member=Member.objects.get(id=id)
        member.group.remove(group)
        member.save()
    for id in add:
        member=Member.objects.get(id=id)
        member.group.add(group)
        member.save()
    return HttpResponse('Success: %s 组已修改' % Group.objects.get(id=group).name)


def log(request):
    lists = Log.objects.all()
    info = [{'time': i.time, 'num': i.num, 'fail': i.fail, 'content': i.content, 'author': i.author} for i in lists]
    return HttpResponse(json.dumps(info), content_type='application/json')


def send(request):
    touser = []
    for i in request.POST.get('touser').split('|')[:-1]:
        if i[0] == 'g':
            for member in Member.objects.filter(group=Group.objects.get(id=i[1:])):
                touser.append(str(member.num))
        else:
            try:
                touser.append(str(Member.objects.get(id=i).num))
            except:
                pass
    touser_num = len(set(touser))
    touser = '|'.join(set(touser))
    content = request.POST.get('content')
    author = request.POST.get('author')
    print(touser_num, touser, content, author)
    time, err = api(touser, content)
    if err == '':
        err = '无'
    else:
        err = '|'.join([Member.objects.get(num=i).name for i in err.split('|')])
    log = Log.objects.create()
    log.time, log.num, log.fail, log.content, log.author = time, touser_num, err, content, author
    log.save()
    return HttpResponse('Success:发送成功')
