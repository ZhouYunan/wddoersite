# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe7\xb1\xbb', blank=True, to='blog.Category', null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98'),
        ),
    ]
