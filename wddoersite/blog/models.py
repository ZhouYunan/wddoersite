# coding:utf-8
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_displayed = models.BooleanField(verbose_name="是否显示")

    def __unicode__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=128, verbose_name="文章标题")
    category = models.ForeignKey(Category, verbose_name="文章分类", blank=True, null=True)
    content = models.TextField(verbose_name="文章正文")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_displayed = models.BooleanField(verbose_name="是否显示")

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.title
