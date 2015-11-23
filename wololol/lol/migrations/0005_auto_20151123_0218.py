# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0004_auto_20151112_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='_map',
        ),
        migrations.RemoveField(
            model_name='history',
            name='assists',
        ),
        migrations.RemoveField(
            model_name='history',
            name='champId',
        ),
        migrations.RemoveField(
            model_name='history',
            name='champLvl',
        ),
        migrations.RemoveField(
            model_name='history',
            name='createDate',
        ),
        migrations.RemoveField(
            model_name='history',
            name='creepScore',
        ),
        migrations.RemoveField(
            model_name='history',
            name='deaths',
        ),
        migrations.RemoveField(
            model_name='history',
            name='gameMode',
        ),
        migrations.RemoveField(
            model_name='history',
            name='gameSubType',
        ),
        migrations.RemoveField(
            model_name='history',
            name='gameType',
        ),
        migrations.RemoveField(
            model_name='history',
            name='goldGained',
        ),
        migrations.RemoveField(
            model_name='history',
            name='isWin',
        ),
        migrations.RemoveField(
            model_name='history',
            name='item1',
        ),
        migrations.RemoveField(
            model_name='history',
            name='item2',
        ),
        migrations.RemoveField(
            model_name='history',
            name='item3',
        ),
        migrations.RemoveField(
            model_name='history',
            name='item4',
        ),
        migrations.RemoveField(
            model_name='history',
            name='item5',
        ),
        migrations.RemoveField(
            model_name='history',
            name='item6',
        ),
        migrations.RemoveField(
            model_name='history',
            name='item7',
        ),
        migrations.RemoveField(
            model_name='history',
            name='kills',
        ),
        migrations.RemoveField(
            model_name='history',
            name='piEarned',
        ),
        migrations.RemoveField(
            model_name='history',
            name='spell1',
        ),
        migrations.RemoveField(
            model_name='history',
            name='spell2',
        ),
        migrations.RemoveField(
            model_name='history',
            name='timeLenght',
        ),
        migrations.RemoveField(
            model_name='history',
            name='timePlayed',
        ),
        migrations.AddField(
            model_name='history',
            name='jsonInfo',
            field=models.TextField(verbose_name='json con la informacion al toke perro', default=''),
            preserve_default=False,
        ),
    ]
