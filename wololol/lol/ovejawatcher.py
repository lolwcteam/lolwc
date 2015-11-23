#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importando
#ID Sad Jocker King= 426174
import json
import requests
#from django.core.exceptions import ObjectDoesNotExist
#from django.shortcuts import render_to_response
#from django.shortcuts import render
#from django.template import RequestContext
#from lol.models import SummonerInfo, MostPlayedChampInfo, SummonerProfile
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

riotWatcher = RiotWatcher("7088def7-f1b0-4182-a9f2-07336754983a", default_region=LATIN_AMERICA_SOUTH) #Seteando mi clave para hacer APIcalls

ligueValue = {
    'Bronze V':26,
    'Bronze IV':25,
    'Bronze III':24,
    'Bronze II':23,
    'Bronze I':22,
    'Silver V':21,
    'Silver IV':20,
    'Silver III':19,
    'Silver II':18,
    'Silver I':17,
    'Gold V':16,
    'Gold IV':15,
    'Gold III':14,
    'Gold II':13,
    'Gold I':12,
    'Platinum V':11,
    'Platinum IV':10,
    'Platinum III':9,
    'Platinum II':8,
    'Platinum I':7,
    'Diamond V':6,
    'Diamond IV':5,
    'Diamond III':4,
    'Diamond II':3,
    'Diamond I':2,
    'Master':1,
    'Challenger':0
}

champsId = { #Diccionario con Id de los campeones
    "266":"Aatrox",
    "412":"Thresh",
    "23":"Tryndamere",
    "79":"Gragas",
    "69":"Cassiopeia",
    "13":"Ryze",
    "78":"Poppy",
    "14":"Sion",
    "1":"Annie",
    "111":"Nautilus",
    "43":"Karma",
    "99":"Lux",
    "103":"Ahri",
    "2":"Olaf",
    "112":"Viktor",
    "34":"Anivia",
    "86":"Garen",
    "27":"Singed",
    "127":"Lissandra",
    "57":"Maokai",
    "25":"Morgana",
    "28":"Evelynn",
    "105":"Fizz",
    "74":"Heimerdinger",
    "238":"Zed",
    "68":"Rumble",
    "37":"Sona",
    "82":"Mordekaiser",
    "96":"KogMaw",
    "55":"Katarina",
    "117":"Lulu",
    "22":"Ashe",
    "30":"Karthus",
    "12":"Alistar",
    "122":"Darius",
    "67":"Vayne",
    "77":"Udyr",
    "110":"Varus",
    "89":"Leona",
    "126":"Jayce",
    "134":"Syndra",
    "80":"Pantheon",
    "92":"Riven",
    "121":"Khazix",
    "42":"Corki",
    "51":"Caitlyn",
    "268":"Azir",
    "76":"Nidalee",
    "3":"Galio",
    "85":"Kennen",
    "45":"Veigar",
    "432":"Bard",
    "150":"Gnar",
    "104":"Graves",
    "90":"Malzahar",
    "254":"Vi",
    "10":"Kayle",
    "39":"Irelia",
    "64":"LeeSin",
    "60":"Elise",
    "106":"Volibear",
    "20":"Nunu",
    "4":"TwistedFate",
    "24":"Jax",
    "102":"Shyvana",
    "429":"Kalista",
    "36":"DrMundo",
    "223":"TahmKench",
    "63":"Brand",
    "131":"Diana",
    "113":"Sejuani",
    "8":"Vladimir",
    "154":"Zac",
    "421":"RekSai",
    "133":"Quinn",
    "84":"Akali",
    "18":"Tristana",
    "120":"Hecarim",
    "15":"Sivir",
    "236":"Lucian",
    "107":"Rengar",
    "19":"Warwick",
    "72":"Skarner",
    "54":"Malphite",
    "157":"Yasuo",
    "101":"Xerath",
    "17":"Teemo",
    "75":"Nasus",
    "58":"Renekton",
    "119":"Draven",
    "35":"Shaco",
    "50":"Swain",
    "115":"Ziggs",
    "91":"Talon",
    "40":"Janna",
    "245":"Ekko",
    "61":"Orianna",
    "114":"Fiora",
    "9":"FiddleSticks",
    "33":"Rammus",
    "31":"Chogath",
    "7":"Leblanc",
    "16":"Soraka",
    "26":"Zilean",
    "56":"Nocturne",
    "222":"Jinx",
    "83":"Yorick",
    "6":"Urgot",
    "203":"Kindred",
    "21":"MissFortune",
    "62":"MonkeyKing",
    "53":"Blitzcrank",
    "98":"Shen",
    "201":"Braum",
    "5":"XinZhao",
    "29":"Twitch",
    "11":"MasterYi",
    "44":"Taric",
    "32":"Amumu",
    "41":"Gangplank",
    "48":"Trundle",
    "38":"Kassadin",
    "161":"Velkoz",
    "143":"Zyra",
    "267":"Nami",
    "59":"JarvanIV",
    "81":"Ezreal"}


def getSummoner(summoner=None, idSum=None, region=None): #Funcion que revisa si el jugador está en la base de datos, o hay que crearlo
    try :
        if idSum != None:
            SummonerInfo.objects.get(summonerId = idSum, summonerRegion = region)
            summonerInfo = getCacheSummoner(idSum = summonerId, region = region)
        else:
            b = SummonerInfo.objects.get(summonerName = summoner, summonerRegion = region)
            idSum = b.summonerId
            summonerInfo = getCacheSummoner(idSum = idSum, region = region)
    except(ObjectDoesNotExist):
        summonerInfo = getApiSummoner(idSum = idSum, summoner=summoner, region = region)
    jsonFinal = json.loads(summonerInfo)
    return jsonFinal

#def getApiSummoner(summoner=None, idSum=None, region=None): #Busca un jugador en la API
#    try:
#        if idSum!=None:
#            me = riotWatcher.get_summoner(_id=idSum)
#        else:
#            me = riotWatcher.get_summoner(name=summoner)
#        wins = 0
#        losses = 0
#        assists = 0
#        kills = 0
#        deaths = 0
#        i = 0
#        summonerName = str(me['name'])
#        summonerId = str(me['id'])
#        summonerImg = str(me['profileIconId'])
#        summonerRegion = str(region)
#        summonerLeagueInfoBase = riotWatcher.get_league_entry([summonerId])
#        summonerLeagueInfo = {}
#        a = 0
#        for i in range(len(summonerLeagueInfoBase[summonerId])):
#            tipo = summonerLeagueInfoBase[summonerId][i]['queue']
#            if(tipo == 'RANKED_SOLO_5x5'):
#                summonerLeagueInfo[summonerId][a] = summonerLeagueInfoBase[summonerId][i]
#                a+=1
#                #Crear RANKED_SOLO_5x5
#            elif(tipo == 'RANKED_TEAM_5x5'):
#                if(summonerLeagueInfo[summonerId][0]['queue'] != 'RANKED_SOLO_5x5'):
#                    summonerLeagueInfo[summonerId][0]['queue'] = 'RANKED_SOLO_5x5'
#                    a+=1
#                summonerLeagueInfo[summonerId][a] = summonerLeagueInfoBase[summonerId][i]
#                a+=1
#                #Si RANKED_SOLO_5x5 NO existe:
#                    #Crear RANKED_SOLO_5x5
#                #Crear RANKED_TEAM_5x5
#            elif(tipo == 'RANKED_TEAM_3X3'):
#                if(summonerLeagueInfo[summonerId][0]['queue'] != 'RANKED_SOLO_5x5'):
#                    summonerLeagueInfo[summonerId][0]['queue'] = 'RANKED_SOLO_5x5'
#                    a+=1
#                if(summonerLeagueInfo[summonerId][2]['queue'] != 'RANKED_TEAM_5x5'):
#                    summonerLeagueInfo[summonerId][0]['queue'] = 'RANKED_SOLO_5x5'
#                    a+=1
#                #Si RANKED_SOLO_5x5 NO existe:
#                    #Crear RANKED_SOLO_5x5
#                #Si RANKED_TEAM_5x5 NO existe:
#                    #Crear RANKED_TEAM_5x5
#                #Crear RANKED_TEAM_5x5
#        try:
#            rankedst = riotWatcher.get_ranked_stats(summonerId)
#            summonerSoloQLeague = summonerLeagueInfo[summonerId][0]['tier']
#            summonerDivision = summonerLeagueInfo[summonerId][0]['entries'][0]['division']
#            summonerSoloQLp = summonerLeagueInfo[summonerId][0]['entries'][0]['leaguePoints']
#            summonerSoloQLeagueName = summonerLeagueInfo[summonerId][0]['name']
#            for x in range(len(rankedst['champions'])):
#                wins += rankedst['champions'][x]['stats']['totalSessionsWon']
#                losses += rankedst['champions'][x]['stats']['totalSessionsLost']
#                assists += rankedst['champions'][x]['stats']['totalAssists']
#                kills += rankedst['champions'][x]['stats']['totalChampionKills']
#                deaths += rankedst['champions'][x]['stats']['totalDeathsPerSession']
#            matchs = wins + losses
#            summonerKills = round(float(kills)/float(matchs), 2)
#            summonerDeaths = round(float(deaths)/float(matchs), 2)
#            summonerAssists = round(float(assists)/float(matchs), 2)
#            summonerWinrate = int(round((float(wins)/float(matchs))*100, 0))
#            killsAssists = float(assists)+float(kills)
#            summonerKdaRatio = round(killsAssists/float(deaths), 2)
#            x = int(len(rankedst['champions']))
#            mostPlayedChampMatchesCount =  0
#            for q in range(x):
#                if (rankedst['champions'][q]['id'] != 0):
#                    partidaChampx = rankedst['champions'][q]['stats']['totalSessionsPlayed']
#                if (mostPlayedChampMatchesCount <= partidaChampx):
#                    mostPlayedChampMatchesCount = partidaChampx
#                    maxChampPos = q
#                    mostPlayedChamp = rankedst['champions'][q]['id']
#                    mostPlayedChampName = champsId[str(mostPlayedChamp)]
#            mostPlayedChampMatchesCount = float(mostPlayedChampMatchesCount)
#            mostPlayedChampKills = round(rankedst['champions'][maxChampPos]['stats']['totalChampionKills']/mostPlayedChampMatchesCount, 2)
#            mostPlayedChampDeaths = round(rankedst['champions'][maxChampPos]['stats']['totalDeathsPerSession']/mostPlayedChampMatchesCount, 2)
#            mostPlayedChampAssist = round(rankedst['champions'][maxChampPos]['stats']['totalAssists']/mostPlayedChampMatchesCount, 2)
#            mostPlayedChampGold = float(rankedssummonerLeagueInfo[summonerId]t['champions'][maxChampPos]['stats']['totalGoldEarned']/mostPlayedChampMatchesCount)
#            mostPlayedChampGold = round(mostPlayedChampGold/1000, 2)
#            mostPlayedChampCs = round(rankedst['champions'][maxChampPos]['stats']['totalMinionKills']/mostPlayedChampMatchesCount, 2)
#            champWinPorcentaje =  rankedst['champions'][maxChampPos]['stats']['totalSessionsWon']/mostPlayedChampMatchesCount * 100
#            champWinPorcentaje = round(champWinPorcentaje, 2)
#            mostPlayedChampMatchesWinCount = rankedst['champions'][maxChampPos]['stats']['totalSessionsWon']
#            mostPlayedChampMatchesLoseCountPorcentaje = rankedst['champions'][maxChampPos]['stats']['totalSessionsLost'] / mostPlayedChampMatchesCount * 100
#            mostPlayedChampMatchesLoseCountPorcentaje = round(mostPlayedChampMatchesLoseCountPorcentaje, 2)
#            mostPlayedChampMatchesLoseCount = rankedst['champions'][maxChampPos]['stats']['totalSessionsLost']
#            mostPlayedChampMatchesCount = int(mostPlayedChampMatchesCount)
#            killsAssists = float(mostPlayedChampKills) + float(mostPlayedChampAssist)
#            mostPlayedChampKdaRatio = round(killsAssists/float(mostPlayedChampDeaths), 2)
#        except(Traceback):
#            summonerSoloQLp = 0
#            summonerSoloQLeague = "unknow"
#            summonerSoloQLeagueName = "Sin Clasificar"
#            summonerDivision = "No disponible"
#            summonerKills = "0.0"
#            summonerDeaths = "0.0"
#            summonerAssists = "0.0"
#            summonerWinrate = "0.0"
#            summonerKdaRatio = "0.0"
#            mostPlayedChamp = "-"
#            mostPlayedChampName = "Ninguno"
#            mostPlayedChampMatchesCount = "0"
#            mostPlayedChampMatchesWinCount = "0"
#            mostPlayedChampMatchesLoseCount = "0"
#            mostPlayedChampKdaRatio = "0.0"
#            mostPlayedChampKills = "0.0"
#            mostPlayedChampDeaths = "0.0"
#            mostPlayedChampAssist = "0.0"
#            mostPlayedChampCs = "0.0"
#            mostPlayedChampGold = "0.0"
#        try:
#            bestLeague=30
#            x=0
#            for(x in range(len[])):
#                
#            summonerSoloQLeague = summonerLeagueInfo[summonerId][0]['tier']
#            summonerDivision = summonerLeagueInfo[summonerId][0]['entries'][0]['division']
#            summonerSoloQLp = summonerLeagueInfo[summonerId][0]['entries'][0]['leaguePoints']
#            summonerSoloQLeagueName = summonerLeagueInfo[summonerId][0]['name']
#
#        except(Traceback):
#        try:
#
#        except(Traceback):
#        SummonerProfile.objects.create(summonerId = summonerId,
#                                       leagueSoloQName = str(summonerSoloQLeagueName),
#                                       leagueSoloQTier = str(summonerSoloQLeague),
#                                       leagueSoloQDivision = str(summonerDivision),
#                                       leagueSoloQLp = str(summonerSoloQLp),
#                                       leagueTeamName = str("PEPE"),
#                                       leagueTeamTier = str("PEPE"),
#                                       leagueTeamDivision = str("PEPE"),
#                                       leagueTeamLp = str("PEPE"),
#                                       league3v3Name = str("PEPE"),
#                                       league3v3Tier = str("PEPE"),
#                                       league3v3Division = str("PEPE"),
#                                       league3v3Lp = str("PEPE"))
#
#        MostPlayedChampInfo.objects.create(summonerId=summonerId,
#                                       mostPlayedChampId=str(mostPlayedChamp),
#                                       mostPlayedChampName=str(mostPlayedChampName),
#                                       mostPlayedChampMatchesCount=str(mostPlayedChampMatchesCount),
#                                       mostPlayedChampMatchesWinCount=str(mostPlayedChampMatchesWinCount),
#                                       mostPlayedChampMatchesLoseCount=str(mostPlayedChampMatchesLoseCount),
#                                       mostPlayedChampKdaRatio=str(mostPlayedChampKdaRatio),
#                                       mostPlayedChampKills=str(mostPlayedChampKills),
#                                       mostPlayedChampDeaths=str(mostPlayedChampDeaths),
#                                       mostPlayedChampAssist=str(mostPlayedChampAssist),
#                                       mostPlayedChampCs=str(mostPlayedChampCs),
#                                       mostPlayedChampGold=str(mostPlayedChampGold))
#
#        SummonerInfo.objects.create(summonerId = summonerId,
#                                    summonerServer = str(summonerRegion).upper(),
#                                    summonerImg = str(summonerImg),
#                                    summonerName = str(summonerName),
#                                    summonerLeague = str(summonerSoloQLeague),
#                                    summonerDivision = str(summonerDivision),
#                                    summonerKills = str(summonerKills),
#                                    summonerDeaths = str(summonerDeaths),
#                                    summonerAssists = str(summonerAssists),
#                                    summonerWinrate = str(summonerWinrate),
#                                    summonerRegion = str(summonerRegion),
#                                    summonerKdaRatio = str(summonerKdaRatio))
#
#        summoner = str(getCacheSummoner(idSum=summonerId, region=summonerRegion))
#    except(LoLException):
#        summoner = str(getCacheSummoner(idSum='None', region='None'))
#    return summoner

def getApiSummoner(summoner=None, idSum=None, region=None): #Busca un jugador en la API
    wins = 0
    losses = 0
    assists = 0
    kills = 0
    deaths = 0
    if idSum!=None:
        me = riotWatcher.get_summoner(_id=idSum)
    else:
        me = riotWatcher.get_summoner(name=summoner)
    summonerName = str(me['name'])
    summonerId = str(me['id'])
    summonerImg = str(me['profileIconId'])
    summonerRegion = str(region)
    try:
        #<--Summoner Info-->
        rankedst = riotWatcher.get_ranked_stats(summonerId)
        summonerLeagueInfo = riotWatcher.get_league_entry([summonerId])
        summonerSoloQLeague = summonerLeagueInfo[summonerId][0]['tier']
        summonerDivision = summonerLeagueInfo[summonerId][0]['entries'][0]['division']
        summonerSoloQLp = summonerLeagueInfo[summonerId][0]['entries'][0]['leaguePoints']
        summonerSoloQLeagueName = summonerLeagueInfo[summonerId][0]['name']
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
        summonerWinrate = int(round((float(wins)/float(matchs))*100, 0))
        killsAssists = float(assists)+float(kills)
        summonerKdaRatio = round(killsAssists/float(deaths), 2)
        #<--Champion mas utilizado-->
        x = int(len(rankedst['champions']))
        mostPlayedChampMatchesCount =  0
        for q in range(x):
            if (rankedst['champions'][q]['id'] != 0):
                partidaChampx = rankedst['champions'][q]['stats']['totalSessionsPlayed']
            if (mostPlayedChampMatchesCount <= partidaChampx):
                mostPlayedChampMatchesCount = partidaChampx
                maxChampPos = q
                mostPlayedChamp = rankedst['champions'][q]['id']
                mostPlayedChampName = champsId[str(mostPlayedChamp)]
        mostPlayedChampMatchesCount = float(mostPlayedChampMatchesCount)
        mostPlayedChampKills = round(rankedst['champions'][maxChampPos]['stats']['totalChampionKills']/mostPlayedChampMatchesCount, 2)
        mostPlayedChampDeaths = round(rankedst['champions'][maxChampPos]['stats']['totalDeathsPerSession']/mostPlayedChampMatchesCount, 2)
        mostPlayedChampAssist = round(rankedst['champions'][maxChampPos]['stats']['totalAssists']/mostPlayedChampMatchesCount, 2)
        mostPlayedChampGold = float(rankedst['champions'][maxChampPos]['stats']['totalGoldEarned']/mostPlayedChampMatchesCount)
        mostPlayedChampGold = round(mostPlayedChampGold/1000, 2)
        mostPlayedChampCs = round(rankedst['champions'][maxChampPos]['stats']['totalMinionKills']/mostPlayedChampMatchesCount, 2)
        champWinPorcentaje =  rankedst['champions'][maxChampPos]['stats']['totalSessionsWon']/mostPlayedChampMatchesCount * 100
        champWinPorcentaje = round(champWinPorcentaje, 2)
        mostPlayedChampMatchesWinCount = rankedst['champions'][maxChampPos]['stats']['totalSessionsWon']
        mostPlayedChampMatchesLoseCountPorcentaje = rankedst['champions'][maxChampPos]['stats']['totalSessionsLost'] / mostPlayedChampMatchesCount * 100
        mostPlayedChampMatchesLoseCountPorcentaje = round(mostPlayedChampMatchesLoseCountPorcentaje, 2)
        mostPlayedChampMatchesLoseCount = rankedst['champions'][maxChampPos]['stats']['totalSessionsLost']
        mostPlayedChampMatchesCount = int(mostPlayedChampMatchesCount)
        killsAssists = float(mostPlayedChampKills) + float(mostPlayedChampAssist)
        mostPlayedChampKdaRatio = round(killsAssists/float(mostPlayedChampDeaths), 2)
    except(IndexError, LoLException):
        summonerSoloQLp = 0
        summonerSoloQLeague = "unRanked"
        summonerSoloQLeagueName = "Sin Clasificar"
        summonerDivision = "No disponible"
        summonerKills = "0.0"
        summonerDeaths = "0.0"
        summonerAssists = "0.0"
        summonerWinrate = "0.0"
        summonerKdaRatio = "0.0"
        mostPlayedChamp = "-"
        mostPlayedChampName = "Ninguno"
        mostPlayedChampMatchesCount = "0"
        mostPlayedChampMatchesWinCount = "0"
        mostPlayedChampMatchesLoseCount = "0"
        mostPlayedChampKdaRatio = "0.0"
        mostPlayedChampKills = "0.0"
        mostPlayedChampDeaths = "0.0"
        mostPlayedChampAssist = "0.0"
        mostPlayedChampCs = "0.0"
        mostPlayedChampGold = "0.0"
    
    #<--Liga-->

    try:
        ligaWatcher = riotWatcher.get_league([str(me['id'])])
        league = {}
        summonerLeagueTabName = ligaWatcher[str(me['id'])][0]['name']
        summonerLeagueTabRank = ligaWatcher[str(me['id'])][0]['tier']
        league['summonerLeagueTabName'] = summonerLeagueTabName
        league['summonerLeagueTabRank'] = summonerLeagueTabRank
        league['summonerLeagueTabDivision'] = summonerDivision
        league['summonerLeagueTabPList'] = []
        league['summonerLeagueTabList'] = []
        for li in range (len(ligaWatcher[str(me['id'])][0]['entries'])):
            try:
                if(summonerDivision == ligaWatcher[str(me['id'])][0]['entries'][li]['division']):
                    summonerLeagueTabPListName = ligaWatcher[str(me['id'])][0]['entries'][li]['playerOrTeamName']
                    summonerLeagueTabPListWins = ligaWatcher[str(me['id'])][0]['entries'][li]['wins']
                    summonerLeagueTabPPromo = ligaWatcher[str(me['id'])][0]['entries'][li]['miniSeries']['progress']
                    summonerLeagueTabPListIsRecent = ligaWatcher[str(me['id'])][0]['entries'][li]['isFreshBlood']
                    summonerLeagueTabPListIsOnFire = ligaWatcher[str(me['id'])][0]['entries'][li]['isHotStreak']
                    league['summonerLeagueTabPList'].append({'summonerLeagueTabPListName':summonerLeagueTabPListName,
                                                            'summonerLeagueTabPListWins':summonerLeagueTabPListWins,
                                                            'summonerLeagueTabPPromo':summonerLeagueTabPPromo,
                                                            'summonerLeagueTabPListIsOnFire':summonerLeagueTabPListIsOnFire,
                                                            'summonerLeagueTabPListIsRecent':summonerLeagueTabPListIsRecent
                                                           })
            except(KeyError):
                if(summonerDivision == ligaWatcher[str(me['id'])][0]['entries'][li]['division']):
                    summonerLeagueTabListName = ligaWatcher[str(me['id'])][0]['entries'][li]['playerOrTeamName']
                    summonerLeagueTabListWins = ligaWatcher[str(me['id'])][0]['entries'][li]['wins']
                    summonerLeagueTabListIsRecent = ligaWatcher[str(me['id'])][0]['entries'][li]['isFreshBlood']
                    summonerLeagueTabListIsOnFire = ligaWatcher[str(me['id'])][0]['entries'][li]['isHotStreak'] 
                    summonerLeagueTabListLP = ligaWatcher[str(me['id'])][0]['entries'][li]['leaguePoints']
                    league['summonerLeagueTabList'].append({'summonerLeagueTabListName':summonerLeagueTabListName,
                                                            'summonerLeagueTabListWins':summonerLeagueTabListWins,
                                                            'summonerLeagueTabListIsRecent':summonerLeagueTabListIsRecent,
                                                            'summonerLeagueTabListIsOnFire':summonerLeagueTabListIsOnFire,
                                                            'summonerLeagueTabListLP':summonerLeagueTabListLP
                                                           })
    except(LoLException):
        league['summonerLeagueTabName'] = 'Sin Clasificar'
        league['summonerLeagueTabRank'] = 'unRanked'
        league['summonerLeagueTabDivision'] = 'No disponible'
        league['summonerLeagueTabPList'] = [{'summonerLeagueTabListName':'No disponible',
                                            'summonerLeagueTabListWins':'No disponible',
                                            'summonerLeagueTabListIsRecent':'No disponible',
                                            'summonerLeagueTabListIsOnFire':'No disponible',
                                            'summonerLeagueTabListLP':'No disponible'}]
        league['summonerLeagueTabList'] = [{'summonerLeagueTabPListName':'No disponible',
                                           'summonerLeagueTabPListWins':'No disponible',
                                           'summonerLeagueTabPPromo':'No disponible',
                                           'summonerLeagueTabPListIsOnFire':'No disponible',
                                           'summonerLeagueTabPListIsRecent':'No disponible'}]
    
    for summonerInLeague in range (len(league['summonerLeagueTabList'])):
        SummonerLeague.objects.create(summonerId = summonerId, 
                                      summonerLeagueTabName = str(summonerLeagueTabName),
                                      summonerLeagueTabRank = str(summonerLeagueTabRank),
                                      summonerLeagueTabDivision = str(summonerDivision),
                                      summonerLeagueTabListName = str(league['summonerLeagueTabList'][summonerInLeague]['summonerLeagueTabListName']),
                                      summonerLeagueTabListWins = str(league['summonerLeagueTabList'][summonerInLeague]['summonerLeagueTabListWins']),
                                      summonerLeagueTabListIsRecent = str(league['summonerLeagueTabList'][summonerInLeague]['summonerLeagueTabListIsRecent']),
                                      summonerLeagueTabListIsOnFire = str(league['summonerLeagueTabList'][summonerInLeague]['summonerLeagueTabListIsOnFire']),
                                      summonerLeagueTabListLP = str(league['summonerLeagueTabList'][summonerInLeague]['summonerLeagueTabListLP'])
                                     )
    for summonerInLeagueP in range(len(league['summonerLeagueTabPList'])):
        SummonerLeague.objects.create(summonerId = summonerId,
                                      summonerLeagueTabPListName = str(league['summonerLeagueTabPList'][summonerInLeagueP]['summonerLeagueTabPListName']),
                                      summonerLeagueTabPListWins = str(league['summonerLeagueTabPList'][summonerInLeagueP]['summonerLeagueTabPListWins']),
                                      summonerLeagueTabPPromo = str(league['summonerLeagueTabPList'][summonerInLeagueP]['summonerLeagueTabPPromo']),
                                      summonerLeagueTabPListIsOnFire = str(league['summonerLeagueTabPList'][summonerInLeagueP]['summonerLeagueTabPListIsOnFire']),
                                      summonerLeagueTabPListIsRecent = str(league['summonerLeagueTabPList'][summonerInLeagueP]['summonerLeagueTabPListIsRecent'])
                                     )
                                      
                    
    SummonerProfile.objects.create(summonerId = summonerId,
                                   leagueSoloQName = str(summonerSoloQLeagueName),
                                   leagueSoloQTier = str(summonerSoloQLeague),
                                   leagueSoloQDivision = str(summonerDivision),
                                   leagueSoloQLp = str(summonerSoloQLp),
                                   leagueTeamName = str("PEPE"),
                                   leagueTeamTier = str("PEPE"),
                                   leagueTeamDivision = str("PEPE"),
                                   leagueTeamLp = str("PEPE"),
                                   league3v3Name = str("PEPE"),
                                   league3v3Tier = str("PEPE"),
                                   league3v3Division = str("PEPE"),
                                   league3v3Lp = str("PEPE"))
    
    MostPlayedChampInfo.objects.create(summonerId=summonerId,
                                   mostPlayedChampId=str(mostPlayedChamp),
                                   mostPlayedChampName=str(mostPlayedChampName),
                                   mostPlayedChampMatchesCount=str(mostPlayedChampMatchesCount),
                                   mostPlayedChampMatchesWinCount=str(mostPlayedChampMatchesWinCount),
                                   mostPlayedChampMatchesLoseCount=str(mostPlayedChampMatchesLoseCount),
                                   mostPlayedChampKdaRatio=str(mostPlayedChampKdaRatio),
                                   mostPlayedChampKills=str(mostPlayedChampKills),
                                   mostPlayedChampDeaths=str(mostPlayedChampDeaths),
                                   mostPlayedChampAssist=str(mostPlayedChampAssist),
                                   mostPlayedChampCs=str(mostPlayedChampCs),
                                   mostPlayedChampGold=str(mostPlayedChampGold))
    
    SummonerInfo.objects.create(summonerId = summonerId,
                                summonerServer = str(summonerRegion).upper(),
                                summonerImg = str(summonerImg),
                                summonerName = str(summonerName),
                                summonerLeague = str(summonerSoloQLeague),
                                summonerDivision = str(summonerDivision),
                                summonerKills = str(summonerKills),
                                summonerDeaths = str(summonerDeaths),
                                summonerAssists = str(summonerAssists),
                                summonerWinrate = str(summonerWinrate),
                                summonerRegion = str(summonerRegion),
                                summonerKdaRatio = str(summonerKdaRatio))
    
    summoner = str(getCacheSummoner(idSum=summonerId, region=summonerRegion))
    return summoner

def getCacheSummoner(idSum=None, region=None): #Busca en la base de datos un jugador
    a = MostPlayedChampInfo.objects.get(summonerId = idSum)
    b = SummonerInfo.objects.get(summonerId = idSum, summonerRegion=region)
    c = SummonerProfile.objects.get(summonerId = idSum)
    d = SummonerLeague.objects.get(summonerId = idSum)
    go = True
    summoner = str('"summonerInfo":{"summonerId":"' + str(b.summonerId)
                    + '","summonerImg":"' + str(b.summonerImg)
                    + '","summonerName":"' + str(b.summonerName)
                    + '","summonerLeague":"' + str(b.summonerLeague).lower().capitalize()
                    + '","summonerDivision":"' + str(b.summonerDivision)
                    + '","summonerKills":"' + str(b.summonerKills)
                    + '","summonerDeaths":"' + str(b.summonerDeaths)
                    + '","summonerAssists":"' + str(b.summonerAssists)
                    + '","summonerServer":"' + str(b.summonerServer)
                    + '","summonerRegion":"' + str(b.summonerRegion)
                    + '","summonerKdaRatio":"' + str(b.summonerKdaRatio)
                    + '","summonerWinrate":"' + str(b.summonerWinrate) + '"}')
    favoriteChamp = str('"mostPlayedChampInfo":{"mostPlayedChampId":"' + str(a.mostPlayedChampId)
                    #+ '","mostPlayedChampMatchesLoseCountPorcentaje":"' + str(a.mostPlayedChampMatchesLoseCountPorcentaje)
                    #+ '","champWinPorcentaje":"' + str(a.champWinPorcentaje)
                    + '","mostPlayedChampMatchesCount":"' + str(a.mostPlayedChampMatchesCount)
                    + '","mostPlayedChampKdaRatio":"' + str(a.mostPlayedChampKdaRatio)
                    + '","mostPlayedChampName":"' + str(a.mostPlayedChampName)
                    + '","mostPlayedChampMatchesWinCount":"' + str(a.mostPlayedChampMatchesWinCount)
                    + '","mostPlayedChampMatchesLoseCount":"' + str(a.mostPlayedChampMatchesLoseCount)
                    + '","mostPlayedChampKills":"' + str(a.mostPlayedChampKills)
                    + '","mostPlayedChampAssist":"' + str(a.mostPlayedChampAssist)
                    + '","mostPlayedChampDeaths":"' + str(a.mostPlayedChampDeaths)
                    + '","mostPlayedChampGold":"' + str(a.mostPlayedChampGold)
                    + '","mostPlayedChampCs":"' + str(a.mostPlayedChampCs) + '"}')
    profile = str('"profile":{"leagueSoloQName":"' + str(c.leagueSoloQName)
                  + '","leagueSoloQTier":"' + str(c.leagueSoloQTier)
                  + '","leagueSoloQDivision":"' + str(c.leagueSoloQDivision)
                  + '","leagueSoloQLp":"' + str(c.leagueSoloQLp)
                  + '","leagueTeamName":"' + str(c.leagueTeamName)
                  + '","leagueTeamTier":"' + str(c.leagueTeamTier)
                  + '","leagueTeamDivision":"' + str(c.leagueTeamDivision)
                  + '","leagueTeamLp":"' + str(c.leagueTeamLp)
                  + '","league3v3Name":"' + str(c.league3v3Name)
                  + '","league3v3Tier":"' + str(c.league3v3Tier)
                  + '","league3v3Division":"' + str(c.league3v3Division)
                  + '","league3v3Lp":"' + str(c.league3v3Lp) + '"}')
    while(go):
        count = 0
        str('"league":{"summonerLeagueTabName
           )
        
        
    savedJson =  '{' + summoner + ',' + favoriteChamp + ',' + profile + '}'
    return savedJson