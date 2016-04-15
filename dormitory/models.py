# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class user(models.Model):
    id = models.TextField(u'用户编号', primary_key=True)
    pwd = models.TextField(u'密码')
    authority = models.IntegerField(u'权限')
    name = models.TextField(u'姓名')
    sex = models.IntegerField(u'性别')
    major = models.TextField(u'专业', null=True)
    source = models.TextField(u'生源地', null=True)
    apartment = models.TextField(u'学院', null=True)

    def __unicode__(self):
        return self.name


class building(models.Model):
    id = models.AutoField(u'编号', primary_key=True)
    name = models.TextField(u'名称')
    remark = models.TextField(u'备注', null=True)

    def __unicode__(self):
        return self.name


class dormitory(models.Model):
    dor_id = models.IntegerField(u'宿舍编号', primary_key=True)
    buil_id = models.IntegerField(u'建筑编号')
    buil_id = models.ForeignKey(building, on_delete=models.CASCADE)
    name = models.IntegerField(u'宿舍名')
    capacity = models.IntegerField(u'容量')
    count = models.IntegerField(u'已用空间')
    state = models.IntegerField(u'可用状态')

    def __unicode__(self):
        return self.name


class dor_arr(models.Model):
    uesr_id = models.ForeignKey(user, related_name=u'用户编号')
    dor_id = models.ForeignKey(dormitory, related_name=u'宿舍编号')

    def __unicode__(self):
        return self.name


class question(models.Model):
    id = models.IntegerField(u'问题编号', primary_key=True)
    content = models.TextField(u'内容')
    option = models.TextField(u'选项')
    remark = models.TextField(u'备注', null=True)

    def __unicode__(self):
        return self.name


class user_answer(models.Model):
<<<<<<< HEAD
    user_id = models.TextField(u'用户编号', primary_key=True, blank=False)
    user_id = models.ForeignKey(user)
    que_id = models.IntegerField(u'问题编号', primary_key=True, blank=False)
    que_id = models.ForeignKey(question)
    answer = models.TextField(u'答案', blank=False)

    def __unicode__(self):
        return self.name
=======
    user_id = models.ForeignKey(user, related_name=u'用户编号', primary_key=True)
    que_id = models.ForeignKey(question, related_name=u'问题编号', primary_key=True)
    answer = models.TextField(u'答案')
>>>>>>> origin/div
