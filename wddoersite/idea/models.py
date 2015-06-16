# coding:utf-8
from django.db import models



TAG_CHOICES = (
    ('RSGW', '人生感悟'),
    ('XXJH', '小小计划'),
    ('DSBJ', '读书笔记'),
    ('JYBB', '军艳宝贝'),
    ('GSZS', '股市知识'),
)


class Idea(models.Model):
    tag = models.CharField(max_length=20, verbose_name="短语分类", choices=TAG_CHOICES)
    content = models.TextField(verbose_name="短语内容")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_displayed = models.BooleanField(verbose_name="是否显示")
