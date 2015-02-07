# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ballots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='abc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='slug',
            field=models.SlugField(default='abd'),
            preserve_default=False,
        ),
    ]
