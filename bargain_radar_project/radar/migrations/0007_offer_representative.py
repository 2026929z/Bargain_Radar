# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0006_remove_offer_representative'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='representative',
            field=models.ForeignKey(default=2, to='radar.CustomerProfile'),
            preserve_default=False,
        ),
    ]
