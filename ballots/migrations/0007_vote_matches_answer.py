# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ballots', '0006_ballot_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='matches_answer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
