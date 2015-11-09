# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0002_auto_20151109_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='summonerinfo',
            name='summonerServer',
            field=models.TextField(default='LAS', verbose_name='server del summoner'),
            preserve_default=False,
        ),
    ]
