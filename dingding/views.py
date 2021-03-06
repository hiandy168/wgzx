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
        if request.POST.get('data') == 'all':
            member_list = Member.objects.all()
            lists = [{'id': member.id, 'name': member.name} for member in member_list]
        else:
            member = Member.objects.get(id=request.POST.get('data'))
            group = [{'name': group.name, 'id': group.id} for group in member.group.all()]
            lists = {'id': member.id, 'name': member.name, 'remark': member.remark, 'num': member.num,
                     'phone': member.phone, 'group': group}
    elif request.POST.get('type') == 'group':
        if request.POST.get('data') == 'all':
            group_list = Group.objects.all()
            lists = [{'id': group.id, 'name': group.name} for group in group_list]
        else:
            member_list = Member.objects.filter(group=Group.objects.get(id=request.POST.get('data')))
            lists = [{'id': member.id, 'name': member.name} for member in member_list]
    elif request.POST.get('type') == 'history':
        log = Log.objects.get(id=request.POST.get('data'))
        lists = eval(log.member)
    if isinstance(lists, list):
        lists = sorted(lists, key=lambda x: x['name'])
    return HttpResponse(json.dumps(lists), content_type='application/json')


def replace(input):
    if input==None:
        input=''
    return input

@login_required
def member(request):
    add = request.POST.get('add')
    if add == '-1':
        Member.objects.get(id=request.POST.get('id')).delete()
        return HttpResponse('Success:已删除')
    else:
        name = replace(request.POST.get('name'))
        num = replace(request.POST.get('num'))
        phone = replace(request.POST.get('phone'))
        remark = replace(request.POST.get('remark'))
        group = eval(request.POST.get('group'))
        if add == '1':
            member = Member.objects.create()
            member.name, member.num, member.phone, member.remark = name, num, phone, remark
            for id in group: member.group.add(id)
            member.save()
            return HttpResponse('Success: %s 已添加' % name)
        else:
            member = Member.objects.get(id=request.POST.get('id'))
            member.name, member.num, member.phone, member.remark = name, num, phone, remark
            member.group.clear()
            for id in group: member.group.add(id)
            member.save()
            return HttpResponse('Success: %s 已修改' % name)

@login_required
def group(request):
    group, add, delete = request.POST.get('group'), eval(request.POST.get('add')), eval(request.POST.get('del'))
    for id in delete:
        member=Member.objects.get(id=id)
        member.group.remove(group)
        member.save()
    for id in add:
        member=Member.objects.get(id=id)
        member.group.add(group)
        member.save()
    return HttpResponse('Success: %s 组已修改' % Group.objects.get(id=group).name)

@login_required
def log(request):
    logs = Log.objects.all()
    lists = [{'time': log.time, 'member': log.id, 'fail': log.fail,
              'content': log.content, 'author': log.author} for log in logs[::-1]]
    return HttpResponse(json.dumps(lists), content_type='application/json')

@login_required
def send(request):
    touser = []
    member_list = json.loads(request.POST.get('touser'))
    for member in member_list:
        if member['id'][0] == 'g':
            for member in Member.objects.filter(group=Group.objects.get(id=member['id'][1:])):
                if member.num == '': touser.append((member.phone))
                else:touser.append((member.num))
        else:
            member = Member.objects.get(id=member['id'])
            if member.num == '':touser.append((member.phone))
            else:touser.append((member.num))
    touser = '|'.join(set(touser))
    content = request.POST.get('content')
    author = request.POST.get('author')
    time, err, errcode = api(touser, content)
    if errcode==0:
        fail = '无' if err == {} else ''
        for info in err:
            list1,list2=err[info].split('|'),[]
            for num in list1:
                try:
                    name=Member.objects.filter(num=num)[0].name
                except:
                    name=Member.objects.filter(phone=num)[0].name
                list2.append(name)
            fail+=info+'【'+','.join(list2)+'】'
        log = Log.objects.create()
        log.time, log.member, log.fail, log.content, log.author = time, member_list, fail, content, author
        log.save()
        return HttpResponse('Success:发送成功')
    else:
        return HttpResponse(err)
