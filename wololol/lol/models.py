from django.db import models

class SummonerInfo(models.Model):
    summonerImg = models.TextField(u'imagen del summoner')
    summonrName = models.TextField(u'nombre del summoner')
    summonerLeague = models.TextField(u'liga actual del sumoner(ej:Silver)')
    summonerDivision = models.TextField(u'division actual del summoner(ej:IV)')
    summonerKills = models.TextField(u'prom kills en ranked:')
    summonerDeaths = models.TextField(u'prom deaths en ranked')
    summonerAssists = models.TextField(u'prom assists en ranked')
    summonerWinrate = models.TextField(u'porcentaje de victorias en ranked')

class MostPlayedChampInfo(models.Model):
    mostPlayedChampImg(u'imagen (icono)')
    mostPlayedChampName(u'nombre')
    mostPlayedChampMatchesCount(u'cantidad de jugada')
    mostPlayedChampMatchesWinCount(u'cantidad de victorias')
    mostPlayedChampMatchesLooseCount(u'cantidad de derrotas')
    mostPlayedChampKdaRatio(u'kda')
    mostPlayedChampKills(u'prom kills')
    mostPlayedChampDeaths(u'prom deaths')
    mostPlayedChampAssist(u'prom asssists')
    mostPlayedChampCs(u'prom creeps')
    mostPlayedChampGold(u'prom gold')
    