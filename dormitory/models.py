# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class user(models.Model):
    id = models.TextField(u'用户编号', primary_key=True, blank=False)
    pwd = models.TextField(u'密码', blank=False)
    authority = models.IntegerField(u'权限', blank=False)
    name = models.TextField(u'姓名', blank=False)
    sex = models.IntegerField(u'性别', blank=False)
    major = models.TextField(u'专业')
    source = models.TextField(u'生源地')
    apartment = models.TextField(u'学院')


class building(models.Model):
    id = models.AutoField(u'编号', primary_key=True, blank=False)
    name = models.TextField(u'名称', blank=False)
    remark = models.TextField(u'备注')


class dormitory(models.Model):
    dor_id = models.IntegerField(u'宿舍编号', primary_key=True, blank=False)
    buil_id = models.IntegerField(u'建筑编号', blank=False)
    buil_id = models.ForeignKey(building)
    name = models.IntegerField(u'宿舍名', blank=False)
    capacity = models.IntegerField(u'容量', blank=False)
    count = models.IntegerField(u'已用空间', blank=False)
    state = models.IntegerField(u'可用状态', blank=False)


class dor_arr(models.Model):
    uesr_id = models.TextField(u'用户编号')
    uesr_id = models.ForeignKey(user)
    dor_id = models.IntegerField(u'宿舍编号')
    dor_id = models.ForeignKey(dormitory)


class question(models.Model):
    id = models.IntegerField(u'问题编号', primary_key=True, blank=False)
    content = models.TextField(u'内容', blank=False)
    option = models.TextField(u'选项', blank=False)
    remark = models.TextField(u'备注')


class user_answer(models.Model):
    user_id = models.TextField(u'用户编号', primary_key=True, blank=False)
    user_id = models.ForeignKey(user)
    que_id = models.IntegerField(u'问题编号', primary_key=True, blank=False)
    que_id = models.ForeignKey(question)
    answer = models.TextField(u'答案', blank=False)
