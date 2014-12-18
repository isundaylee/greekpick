# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('choice', models.TextField()),
            ],
            options={
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
            },
            bases=(models.Model,),
        ),
    ]
