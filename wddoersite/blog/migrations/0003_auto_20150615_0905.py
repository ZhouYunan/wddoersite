# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150530_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
