# coding=utf-8
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.TextField(u'*用户编号', primary_key=True)
    pwd = models.TextField(u'*密码')
    authority = models.IntegerField(u'*权限')
    name = models.TextField(u'*姓名')
    sex = models.IntegerField(u'*性别')
    major = models.TextField(u'专业', null=True, blank=True)
    source = models.TextField(u'生源地', null=True, blank=True)
    apartment = models.TextField(u'学院', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id)


class Building(models.Model):
    id = models.AutoField(u'*编号', primary_key=True)
    name = models.TextField(u'*名称')
    remark = models.TextField(u'备注', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id)


class Dormitory(models.Model):
    dor_id = models.AutoField(u'*宿舍编号', primary_key=True)
    buil_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.TextField(u'*宿舍名')
    capacity = models.IntegerField(u'*容量')
    count = models.IntegerField(u'*已用空间')
    state = models.IntegerField(u'*可用状态')

    def __unicode__(self):
        return unicode(self.dor_id)


class DorArrange(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True)
    dor_id = models.ForeignKey(Dormitory, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user_id)


class Question(models.Model):
    id = models.AutoField(u'*问题编号', primary_key=True)
    content = models.TextField(u'*内容')
    option = models.TextField(u'*选项')
    remark = models.TextField(u'备注', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id)


class User_answer(models.Model):
    user_id = models.ForeignKey(User)
    que_id = models.ForeignKey(Question)
    answer = models.TextField(u'*答案')
    class Meta:
        unique_together = ('user_id', 'que_id')

    def __unicode__(self):
        return unicode(self.user_id)
