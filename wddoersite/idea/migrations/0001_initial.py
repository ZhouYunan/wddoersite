# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=20, verbose_name=b'\xe7\x9f\xad\xe8\xaf\xad\xe5\x88\x86\xe7\xb1\xbb', choices=[(b'RSGW', b'\xe4\xba\xba\xe7\x94\x9f\xe6\x84\x9f\xe6\x82\x9f'), (b'XXJH', b'\xe5\xb0\x8f\xe5\xb0\x8f\xe8\xae\xa1\xe5\x88\x92'), (b'DSBJ', b'\xe8\xaf\xbb\xe4\xb9\xa6\xe7\xac\x94\xe8\xae\xb0')])),
                ('content', models.TextField(verbose_name=b'\xe7\x9f\xad\xe8\xaf\xad\xe5\x86\x85\xe5\xae\xb9')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_displayed', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba')),
            ],
        ),
    ]
