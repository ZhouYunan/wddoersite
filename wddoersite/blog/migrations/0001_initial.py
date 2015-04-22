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
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('po_type', models.ForeignKey(verbose_name=b'category', blank=True, to='wddoersite.blog.Category', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
