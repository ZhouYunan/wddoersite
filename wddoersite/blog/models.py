# coding:utf-8
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=128, verbose_name='文章名')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    category = models.ForeignKey(Category, verbose_name='分类', blank=True, null=True)
    content = models.TextField(verbose_name='笔记正文')

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.title
