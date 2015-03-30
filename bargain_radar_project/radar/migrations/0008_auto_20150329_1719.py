# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0007_offer_representative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='representative',
            field=models.BooleanField(default=False),
        ),
    ]
