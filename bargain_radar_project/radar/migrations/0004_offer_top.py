# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0003_auto_20150323_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='top',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
