# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ballots', '0002_auto_20150206_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ballot',
            name='accepted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
