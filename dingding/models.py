from django.contrib import admin
from django.db import models


# Create your models here.
class Group(models.Model):
    class Meta:
        verbose_name = '分组'
        verbose_name_plural = '分组管理'
        ordering = ['name']
    name=models.CharField('分组',max_length=100)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')

class Member(models.Model):
    class Meta:
        verbose_name = '人员'
        verbose_name_plural = '人员管理'
        ordering = ['num']
    name=models.CharField('姓名',max_length=100)
    num=models.CharField('工号',max_length=100,null=True,blank=True)
    phone=models.CharField('电话',max_length=20,null=True,blank=True)
    remark=models.CharField('备注',max_length=100,null=True,blank=True)
    group=models.ManyToManyField(Group,verbose_name='分组')
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','num','phone','remark')


class Log(models.Model):
    class Meta:
        verbose_name = '日志'
        verbose_name_plural = '日志记录'
        ordering = ['time']

    time = models.CharField('时间', max_length=200)
    member = models.CharField('总数', max_length=200)
    fail=models.CharField('失败',max_length=200)
    content = models.CharField('内容', max_length=200)
    author = models.CharField('操作', max_length=200)
class LogAdmin(admin.ModelAdmin):
    list_display = ('time', 'content', 'author')
