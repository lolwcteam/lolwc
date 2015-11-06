# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summonerinfo',
            old_name='summonrName',
            new_name='summonerName',
        ),
    ]
