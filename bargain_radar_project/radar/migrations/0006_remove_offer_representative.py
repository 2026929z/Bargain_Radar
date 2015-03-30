# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0005_auto_20150327_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='representative',
        ),
    ]
