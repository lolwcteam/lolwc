from django.db import models

class SummonerInfo(models.Model):
    summonerId = models.TextField(u'id del summoner', primary_key=True)
    summonerRegion = models.TextField(u'region del summoner')
    summonerServer = models.TextField(u'server del summoner')
    summonerImg = models.TextField(u'imagen del summoner')
    summonerName = models.TextField(u'nombre del summoner')
    summonerLeague = models.TextField(u'liga actual del sumoner(ej:Silver)')
    summonerDivision = models.TextField(u'division actual del summoner(ej:IV)')
    summonerKills = models.TextField(u'prom kills en ranked:')
    summonerDeaths = models.TextField(u'prom deaths en ranked')
    summonerAssists = models.TextField(u'prom assists en ranked')
    summonerWinrate = models.TextField(u'porcentaje de victorias en ranked')
    summonerKdaRatio = models.TextField(u'kda ratio general')

class MostPlayedChampInfo(models.Model):
    summonerId = models.TextField(u'id del summoner', primary_key=True)
    mostPlayedChampId = models.TextField(u'icono del pj mas usado')
    mostPlayedChampName = models.TextField(u'nombre')
    mostPlayedChampMatchesCount = models.TextField(u'cantidad de jugada')
    mostPlayedChampMatchesWinCount = models.TextField(u'cantidad de victorias')
    mostPlayedChampMatchesLoseCount = models.TextField(u'cantidad de derrotas')
    mostPlayedChampKdaRatio = models.TextField(u'kda ratio con este Pj')
    mostPlayedChampKills = models.TextField(u'prom kills')
    mostPlayedChampDeaths = models.TextField(u'prom deaths')
    mostPlayedChampAssist = models.TextField(u'prom asssists')
    mostPlayedChampCs = models.TextField(u'prom creeps')
    mostPlayedChampGold = models.TextField(u'prom gold')

class SummonerProfile(models.Model):
    summonerId = models.TextField(u'id del summoner', primary_key=True)
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

class League(models.Model):
    summonerLeagueTabName = models.TextField(u'nombre de la liga')
    summonerLeagueTabRank = models.TextField(u'rank del summoner')
    summonerLeagueQueue = models.TextField(u'queue por ejemplo RANKED_SOLO_5X5')
    summonerLeagueTabDivision = models.TextField(u'division del summoner')
    
class EntriesP(models.Model):
    summonerLeagueTabName = models.TextField(u'nombre de la liga')
    summonerLeagueTabRank = models.TextField(u'rank del summoner')
    summonerLeagueQueue = models.TextField(u'queue por ejemplo RANKED_SOLO_5X5')
    summonerLeagueTabDivision = models.TextField(u'division del summoner')
    summonerLeagueTabPListName = models.TextField(u'nombre del summoner')
    summonerLeagueTabPListWins = models.TextField(u'partidas ganadas')
    summonerLeagueTabPPromo = models.TextField(u'su proveso en la promo (LWN)')
    summonerLeagueTabPListIsOnFire = models.TextField(u'si el summoner esta onFire o en racha')
    summonerLeagueTabPListIsRecent = models.TextField(u'si el summoner es reciente en su division')
    

class History(models.Model):
    summonerId = models.TextField(u'id del summoner', primary_key=True)
    jsonInfo = models.TextField(u'json con la informacion al toke perro') 
#    champName = models.TextField(u'nombre del campeon usado')
#    isWin = models.TextField(u'ganada?')
#    champId = models.TextField(u'id champ')
#    champLvl = models.TextField(u'lvl final')
#    spell1 = models.TextField(u'spell 1')
#    spell2 = models.TextField(u'spell 2')
#    gameSubType = models.TextField(u'subtipo')
#    _map = models.TextField(u'mapa')
#    timePlayed = models.TextField(u'tiempo jugado')
#    piEarned = models.TextField(u'IP ganado')
#    kills = models.TextField(u'Asesinatos')
#    deaths = models.TextField(u'Muertes')
#    assists = models.TextField(u'Asistencias')
#    goldGained = models.TextField(u'oro ganado')
#    creepScore = models.TextField(u'minions farmeados')
#    createDate = models.TextField(u'fecha creacion')
#    createTime = models.TextField(u'hora creacion')
#    item1 = models.TextField(u'Item 1')
#    item2 = models.TextField(u'Item 2')
#    item3 = models.TextField(u'Item 3')
#    item4 = models.TextField(u'Item 4')
#    item5 = models.TextField(u'Item 5')
#    item6 = models.TextField(u'Item 6')
#    item7 = models.TextField(u'Item 7')

class runes(models.Model):
    activePage = models.TextField(u'pagina activa')
    pages = models.TextField(u'paginas') #TODO: ver como carajo voy a poner las paginas

#TODO: agregar las clases restantes
