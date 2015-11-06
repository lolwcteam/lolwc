import json
from lol.models import SummonerInfo 
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

riotWatcher = RiotWatcher("c8587cc1-abdf-4911-8d19-d3802e2800d0", default_region=LATIN_AMERICA_SOUTH)
i = 0

def getSummonerInfo(summoner = None, idSum = None, region = None):
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
    me = riotWatcher.get_summoner(name=summoner)
    summonerName = me['name']
    summonerImg = get_summoner_profileIconId(name = summonerName)
    #pidiendo Liga
    try:
        summonerLeagueInfo = riotWatcher.get_league_entry([str(me['id'])])
        summonerLeague = summonerLeagueInfo[str(me['id'])][0]['tier']
        summonerDivision = summonerLeagueInfo[str(me['id'])][0]['entries'][0]['division']
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
        summonerKills = round(float(kills)/float(matchs), 2)
        summonerDeaths = round(float(deaths)/float(matchs), 2)
        summonerAssists = round(float(assists)/float(matchs), 2)
        summonerWinrate = int(round(float(wins)/float(matchs), 0)*100)
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
    baseDatos = SummonerInfo(summonerImg = str(summonerImg),summonerName = str(summonerName),summonerLeague = str(summonerLeague),summonerDivision = str(summonerDivision),summonerKills = str(summonerKills),summonerDeaths = str(summonerDeaths),summonerAssists = str(summonerAssists),summonerWinrate = str(summonerWinrate) )
    baseDatos.save()
    
#final PETICIONES
#inicio RETURNS
    return 
#final RETURNS


def get_summoner_profileIconId(name=None, _id=None, region='las'):
    if (name is None) != (_id is None):
        if name is not None:
            return get_summoners(names=[name, ], region=region)[profileIconId]
        else:
            name = get_summoners(ids=[_id, ], region=region)[str(_id)]
            return get_summoners(names=[name, ], region=region)[profileIconId]
    return None
