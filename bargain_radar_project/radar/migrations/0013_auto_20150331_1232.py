# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0012_offer_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
    ]
