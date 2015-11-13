# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0003_summonerinfo_summonerserver'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profile',
            new_name='SummonerProfile',
        ),
    ]
