# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='picture',
            field=models.ImageField(default=b'default_offer_img.jpg', upload_to=b'offer_images'),
            preserve_default=True,
        ),
    ]
