# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_displayed', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x90\x8d')),
                ('is_displayed', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba')),
                ('content', models.TextField(verbose_name=b'\xe7\xac\x94\xe8\xae\xb0\xe6\xad\xa3\xe6\x96\x87')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('category', models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', blank=True, to='blog.Category', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
