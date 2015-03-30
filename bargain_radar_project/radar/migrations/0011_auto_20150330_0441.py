# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0010_auto_20150330_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
        ),
    ]
