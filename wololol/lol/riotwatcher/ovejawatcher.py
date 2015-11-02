import json
from riotwatcher import RiotWatcher
from riotwatcher import LoLException
from riotwatcher import BRAZIL
from riotwatcher import EUROPE_NORDIC_EAST
from riotwatcher import EUROPE_WEST
from riotwatcher import KOREA
from riotwatcher import LATIN_AMERICA_NORTH
from riotwatcher import LATIN_AMERICA_SOUTH
from riotwatcher import NORTH_AMERICA
from riotwatcher import OCEANIA
from riotwatcher import RUSSIA
from riotwatcher import TURKEY

riotWatcher = RiotWatcher("9e3c8aec-25d1-4241-ab69-b8b65393e5e0", default_region=LATIN_AMERICA_SOUTH)
i = 0

def summonerInfo(summoner):
#inicio IDENTACION
    summonerImg = '' #Imagen del Summoner
    summonerName = '' #Nombre del Summoner
    summonerLeague = '' #Liga del Summoner
    summonerDivision = '' #Division del Summoner
    summonerKills = 0 #Promedio de Kills
    summonerDeaths = 0 #Promedio de Muertes
    summonerAssists = 0 #Promedio de Asistencias
    summonerWinrate = 0 #Promedio de Victorias
    wins = 0
    losses = 0
    assists = 0
    kills = 0
    deaths = 0
    matchs = 0
#final IDENTACION
#inicio PETICIONES
    me = riotWatcher.get_summoner(summonerName=summoner)
    summonerName = me['summonerName']
    summonerImg = riotWatcher.get_summoner_profileIconId(summonerName)
    #pidiendo Liga
    try:
        summonerLeagueInfo = riotWatcher.get_league_entry([str(me['id'])])
        summonerLeague = summonerLeagueInfo[str(me['id'])][0]['tier']
        summonerDivision = summonerLeagueInfo[str(me['id'])][0]['entries'][0]['summonerDivision']
    except(LoLException):
        summonerLeague = "unRanked"
        summonerDivision = "unRanked"

    #pidiendo RANKED STATS
    try:
        rankedst = riotWatcher.get_ranked_stats(me['id'])
        for x in range(len(rankedst['champions'])):
            wins += rankedst['champions'][x]['stats']['totalSessionsWon']
            losses += rankedst['champions'][x]['stats']['totalSessionsLost']
            assists += rankedst['champions'][x]['stats']['totalAssists']
            kills += rankedst['champions'][x]['stats']['totalChampionKills']
            deaths += rankedst['champions'][x]['stats']['totalDeathsPerSession']
        matchs = wins + losses
        summonerKills = kills/matchs
        summonerDeaths = deaths/matchs
        summonerAssists = assists/matchs
        summonerWinrate = wins/matchs
    except(IndexError, LoLException):
        kills = '0'
        assists = '0'
        wins = '0'
        losses = '0'
        deaths = '0'
        matchs = '0'
        summonerKills = '0'
        summonerDeaths = '0'
        summonerAssists = '0'
        summonerWinrate = '0'
#final PETICIONES
#inicio RETURNS
    return["summonerImg":summonerImg,"summonersummonerName":summonerName,"summonerLeague":summonerLeague,"summonersummonerDivision":summonerDivision,"summonerKills":summonerKills,"summonerDeaths":summonerDeaths,"summonerAssists":summonerAssists,"summonerWinrate":summonerWinrate]
#final RETURNS