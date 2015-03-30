# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0009_auto_20150330_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='picture',
            field=models.ImageField(default=b'offer_images/default_offer_img.jpg', upload_to=b'offer_images'),
        ),
    ]
