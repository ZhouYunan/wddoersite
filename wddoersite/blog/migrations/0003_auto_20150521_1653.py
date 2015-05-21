# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_note_is_removed'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 21, 16, 53, 34, 699000), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='category',
            name='is_removed',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xa7\xbb\xe9\x99\xa4'),
        ),
    ]
