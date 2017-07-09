from django.db import models
from django.contrib import admin
import datetime

# Create your models here.
class Group(models.Model):
    class Meta:
        verbose_name = '分组'
        verbose_name_plural = '分组管理'
        ordering = ['name']
    name=models.CharField('分组',max_length=100)
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
    time=models.DateTimeField(default=datetime.datetime.now)
    content=models.CharField('内容',max_length=200)
    success=models.CharField('成功',max_length=200)
    fail=models.CharField('失败',max_length=200)
class LogAdmin(admin.ModelAdmin):
    list_display = ('time','content')