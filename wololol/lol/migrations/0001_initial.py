# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isWin', models.TextField(verbose_name='booleano de ganada o perdida')),
                ('champId', models.TextField(verbose_name='id del campeon usado')),
                ('champLvl', models.TextField(verbose_name='nivel en el que termino')),
                ('spell1', models.TextField(verbose_name='summoner spell 1')),
                ('spell2', models.TextField(verbose_name='summoner spell 2')),
                ('gameType', models.TextField(verbose_name='tipo de juego')),
                ('gameMode', models.TextField(verbose_name='modo de juego')),
                ('gameSubType', models.TextField(verbose_name='sub tipo de juego')),
                ('_map', models.TextField(verbose_name='mapa')),
                ('timeLenght', models.TextField(verbose_name='duracion de la partida')),
                ('timePlayed', models.TextField(verbose_name='tiempo jugado')),
                ('piEarned', models.TextField(verbose_name='IP ganados')),
                ('kills', models.TextField(verbose_name='kills')),
                ('deaths', models.TextField(verbose_name='deaths')),
                ('assists', models.TextField(verbose_name='assists')),
                ('goldGained', models.TextField(verbose_name='oro ganado')),
                ('creepScore', models.TextField(verbose_name='minions asesinados')),
                ('createDate', models.TextField(verbose_name='fecha de creacion de la partida')),
                ('item1', models.TextField(verbose_name='item 1')),
                ('item2', models.TextField(verbose_name='item 2')),
                ('item3', models.TextField(verbose_name='item 3')),
                ('item4', models.TextField(verbose_name='item 4')),
                ('item5', models.TextField(verbose_name='item 5')),
                ('item6', models.TextField(verbose_name='item 6')),
                ('item7', models.TextField(verbose_name='baratija')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='league',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summonerLeagueTabName', models.TextField(verbose_name='nombre de la liga')),
                ('summonerLeagueTabRank', models.TextField(verbose_name='rango de la liga')),
                ('summonerLeagueTabDivision', models.TextField(verbose_name='division de la liga')),
                ('summonerLeagueTabPList', models.TextField(verbose_name='lista de jugadores en promo')),
                ('summonerLeagueTabList', models.TextField(verbose_name='lista de jugadores')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MostPlayedChampInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mostPlayedChampImg', models.TextField(verbose_name='icono del pj mas usado')),
                ('mostPlayedChampName', models.TextField(verbose_name='nombre')),
                ('mostPlayedChampMatchesCount', models.TextField(verbose_name='cantidad de jugada')),
                ('mostPlayedChampMatchesWinCount', models.TextField(verbose_name='cantidad de victorias')),
                ('mostPlayedChampMatchesLooseCount', models.TextField(verbose_name='cantidad de derrotas')),
                ('mostPlayedChampKdaRatio', models.TextField(verbose_name='kda')),
                ('mostPlayedChampKills', models.TextField(verbose_name='prom kills')),
                ('mostPlayedChampDeaths', models.TextField(verbose_name='prom deaths')),
                ('mostPlayedChampAssist', models.TextField(verbose_name='prom asssists')),
                ('mostPlayedChampCs', models.TextField(verbose_name='prom creeps')),
                ('mostPlayedChampGold', models.TextField(verbose_name='prom gold')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leagueSoloQName', models.TextField(verbose_name='nombre de la liga en solo Q de un jugador especifico')),
                ('leagueSoloQTier', models.TextField(verbose_name='tipo de liga en solo Q de un jugador especifico')),
                ('leagueSoloQDivision', models.TextField(verbose_name='division de la liga en solo Q de un jugador especifico')),
                ('leagueSoloQLp', models.TextField(verbose_name='puntos en la liga en solo Q de un jugador especifico')),
                ('leagueTeamName', models.TextField(verbose_name='nombre del equipo de un jugador especifico')),
                ('leagueTeamTier', models.TextField(verbose_name='tipo de la liga en equipo de un jugador especifico')),
                ('leagueTeamDivision', models.TextField(verbose_name='division de la liga en equipo de un jugador especifico')),
                ('leagueTeamLp', models.TextField(verbose_name='puntos de la liga en equipos de un jugador especifico')),
                ('league3v3Name', models.TextField(verbose_name='nombre de la liga en 3v3 de un jugador especifico')),
                ('league3v3Tier', models.TextField(verbose_name='tipo de liga en 3v3 de un jugador especifico')),
                ('league3v3Division', models.TextField(verbose_name='division de la liga en 3v3 de un jugador especifico')),
                ('league3v3Lp', models.TextField(verbose_name='puntos en la liga 3v3 de un jugador especifico')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='runes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activePage', models.TextField(verbose_name='pagina activa')),
                ('pages', models.TextField(verbose_name='paginas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SummonerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summonerImg', models.TextField(verbose_name='imagen del summoner')),
                ('summonrName', models.TextField(verbose_name='nombre del summoner')),
                ('summonerLeague', models.TextField(verbose_name='liga actual del sumoner(ej:Silver)')),
                ('summonerDivision', models.TextField(verbose_name='division actual del summoner(ej:IV)')),
                ('summonerKills', models.TextField(verbose_name='prom kills en ranked:')),
                ('summonerDeaths', models.TextField(verbose_name='prom deaths en ranked')),
                ('summonerAssists', models.TextField(verbose_name='prom assists en ranked')),
                ('summonerWinrate', models.TextField(verbose_name='porcentaje de victorias en ranked')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
