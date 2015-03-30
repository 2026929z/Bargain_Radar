# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0008_auto_20150329_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='picture',
            field=models.ImageField(upload_to=b'offer_images', blank=True),
        ),
    ]
