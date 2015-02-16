# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from ballots.models import Poll


class Migration(migrations.Migration):

    dependencies = [
        ('ballots', '0005_auto_20150216_1613'),
    ]

    # poll = Poll.objects.get(slug='oscar_pool_2015')
    operations = [
        migrations.AddField(
            model_name='ballot',
            name='poll',
            field=models.ForeignKey(default=1, to='ballots.Poll'),
            preserve_default=False,
        ),
    ]
