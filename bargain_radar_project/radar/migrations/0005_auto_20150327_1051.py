# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0004_offer_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='representative',
            field=models.ForeignKey(default=2, to='radar.CustomerProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='picture',
            field=models.ImageField(default=b'offer_images/default_offer_img.jpg', upload_to=b'offer_images'),
        ),
    ]
