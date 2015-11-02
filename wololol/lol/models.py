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
    mostPlayedChampImg = models.TextField(u'icono del pj mas usado')
    mostPlayedChampName = models.TextField(u'nombre')
    mostPlayedChampMatchesCount = models.TextField(u'cantidad de jugada')
    mostPlayedChampMatchesWinCount = models.TextField(u'cantidad de victorias')
    mostPlayedChampMatchesLooseCount = models.TextField(u'cantidad de derrotas')
    mostPlayedChampKdaRatio = models.TextField(u'kda')
    mostPlayedChampKills = models.TextField(u'prom kills')
    mostPlayedChampDeaths = models.TextField(u'prom deaths')
    mostPlayedChampAssist = models.TextField(u'prom asssists')
    mostPlayedChampCs = models.TextField(u'prom creeps')
    mostPlayedChampGold = models.TextField(u'prom gold')

class profile(models.Model):
    leagueSoloQName = models.TextField(u'nombre de la liga en solo Q de un jugador especifico')
    leagueSoloQTier = models.TextField(u'tipo de liga en solo Q de un jugador especifico')
    leagueSoloQDivision = models.TextField(u'division de la liga en solo Q de un jugador especifico')
    leagueSoloQLp = models.TextField(u'puntos en la liga en solo Q de un jugador especifico')
    leagueTeamName = models.TextField(u'nombre del equipo de un jugador especifico')
    leagueTeamTier = models.TextField(u'tipo de la liga en equipo de un jugador especifico')
    leagueTeamDivision = models.TextField(u'division de la liga en equipo de un jugador especifico')
    leagueTeamLp = models.TextField(u'puntos de la liga en equipos de un jugador especifico')
    league3v3Name = models.TextField(u'nombre de la liga en 3v3 de un jugador especifico')
    league3v3Tier = models.TextField(u'tipo de liga en 3v3 de un jugador especifico')
    league3v3Division = models.TextField(u'division de la liga en 3v3 de un jugador especifico')
    league3v3Lp = models.TextField(u'puntos en la liga 3v3 de un jugador especifico')

class league(models.Model):
    summonerLeagueTabName = models.TextField(u'nombre de la liga')
    summonerLeagueTabRank = models.TextField(u'rango de la liga')
    summonerLeagueTabDivision = models.TextField(u'division de la liga')
    summonerLeagueTabPList = models.TextField(u'lista de jugadores en promo') #relacionar con la CLASE del mismo nombre
    summonerLeagueTabList = models.TextField(u'lista de jugadores') #relacionar con la CLASE del mismo nombre

class history(models.Model):
    isWin = models.TextField(u'booleano de ganada o perdida')
    champId = models.TextField(u'id del campeon usado')
    champLvl = models.TextField(u'nivel en el que termino')
    spell1 = models.TextField(u'summoner spell 1')
    spell2 = models.TextField(u'summoner spell 2')
    gameType = models.TextField(u'tipo de juego')
    gameMode = models.TextField(u'modo de juego')
    gameSubType = models.TextField(u'sub tipo de juego')
    _map = models.TextField(u'mapa')
    timeLenght = models.TextField(u'duracion de la partida')
    timePlayed = models.TextField(u'tiempo jugado')
    piEarned = models.TextField(u'IP ganados')
    kills = models.TextField(u'kills')
    deaths = models.TextField(u'deaths')
    assists = models.TextField(u'assists')
    goldGained = models.TextField(u'oro ganado')
    creepScore = models.TextField(u'minions asesinados')
    createDate = models.TextField(u'fecha de creacion de la partida')
    item1 = models.TextField(u'item 1')
    item2 = models.TextField(u'item 2')
    item3 = models.TextField(u'item 3')
    item4 = models.TextField(u'item 4')
    item5 = models.TextField(u'item 5')
    item6 = models.TextField(u'item 6')
    item7 = models.TextField(u'baratija')

class runes(models.Model):
    activePage = models.TextField(u'pagina activa')
    pages = models.TextField(u'paginas') #TODO: ver como carajo voy a poner las paginas

#TODO: agregar las clases restantes
