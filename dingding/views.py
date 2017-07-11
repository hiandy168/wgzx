import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Member, Group


@login_required
def index(request):
    return render(request, 'dingding/index.html', {'user': request.user})

@login_required
def iframe(request,key):
    group_list=[group.name for group in Group.objects.all()]
    member_list=[member.name for member in Member.objects.all()]
    return render(request,'dingding/%s.html'%key)

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
