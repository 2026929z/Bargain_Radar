# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0011_auto_20150330_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
