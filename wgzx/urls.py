"""wgzx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from dingding import views as dingding_views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^login/',admin.site.login),
    url(r'^$',dingding_views.index,name='index'),
    url(r'^page/(.+)/$',dingding_views.iframe,name='iframe'),
    url(r'^group/(.+)/$',dingding_views.group,name='group'),
    url(r'^member/(.+)/$',dingding_views.member,name='member'),
    url(r'^data/$', dingding_views.member, name='data'),
    # url(r'^get/(?p<group>)',dingding_views.get,name='get'),
]
