#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','shop.settings')#添加环境变量

app=Celery('shop')#创建应用实例

app.config_from_object('django.conf:settings')#加载自定义设置
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)#为INSTALLED_APPS设置中列出自动查找异步任务