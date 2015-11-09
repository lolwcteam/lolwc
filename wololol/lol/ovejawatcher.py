 #Hoy, 8 de Noviembre, Ovejawatcher usa 0 ApiCalls para devolver un usuario que se encuentra en el cache y 5 para devolver un usuario que no estaba en la base de datos

import json
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from lol.models import SummonerInfo, MostPlayedChampInfo
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
champsId = {
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

def getSummoner(summoner=None, idSum=None, region=None):
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
        b = SummonerInfo.objects.get(summonerName = summoner, summonerRegion = region)
        idSum = b.summonerId
    mostPlayedChampInfo = getMostPlayedChampInfo(idSum = idSum, region = region)
    finalJson = "{" + summonerInfo + "," + mostPlayedChampInfo + "}"
    jsonfinal = json.loads(finalJson)
    return jsonfinal

def getApiSummoner(summoner=None, idSum=None, region=None):
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
    if summoner==None:
        me = riotWatcher.get_summoner(_id=idSum)
    else:
        me = riotWatcher.get_summoner(name=summoner)
    summonerName = me['name']
    summonerId = me['id']
    summonerImg = me['profileIconId']
    summonerRegion = region
    try:
        summonerLeagueInfo = riotWatcher.get_league_entry([str(me['id'])])
        summonerLeague = summonerLeagueInfo[str(me['id'])][0]['tier']
        summonerDivision = summonerLeagueInfo[str(me['id'])][0]['entries'][0]['division']
    except(LoLException):
        summonerLeague = "unRanked"
        summonerDivision = "unRanked"
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
        summonerWinrate = int(round((float(wins)/float(matchs))*100, 0))
        killsAssists = float(assists)+float(kills)
        summonerKdaRatio = round(killsAssists/float(deaths), 2)
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
    SummonerInfo.objects.create(summonerId = str(summonerId),summonerServer = str(summonerRegion).upper(),summonerImg = str(summonerImg),summonerName = str(summonerName),summonerLeague = str(summonerLeague),summonerDivision = str(summonerDivision),summonerKills = str(summonerKills),summonerDeaths = str(summonerDeaths),summonerAssists = str(summonerAssists),summonerWinrate = str(summonerWinrate), summonerRegion = str(summonerRegion), summonerKdaRatio = str(summonerKdaRatio))
    jsonfinal = getCacheSummoner(idSum = summonerId, region = summonerRegion)
    return jsonfinal

def getCacheSummoner(idSum=None, region=None):
    a = SummonerInfo.objects.get(summonerId = idSum, summonerRegion=region)
    summonerInfoJson = str(
        '"summonerInfo":{"summonerId":"' + str(a.summonerId)
        + '","summonerImg":"' + str(a.summonerImg)
        + '","summonerName":"' + str(a.summonerName)
        + '","summonerLeague":"' + str(a.summonerLeague).lower().capitalize()
        + '","summonerDivision":"' + str(a.summonerDivision)
        + '","summonerKills":"' + str(a.summonerKills)
        + '","summonerDeaths":"' + str(a.summonerDeaths)
        + '","summonerAssists":"' + str(a.summonerAssists)
        + '","summonerServer":"' + str(a.summonerServer)
        + '","summonerRegion":"' + str(a.summonerRegion)
        + '","summonerKdaRatio":"' + str(a.summonerKdaRatio)
        + '","summonerWinrate":"' + str(a.summonerWinrate) + '"}')
    return summonerInfoJson

def getApiMostPlayedChampInfo(summoner=None, idSum=None, region=None):
    if summoner==None:
        me = riotWatcher.get_summoner(_id=idSum)
    else:
        me = riotWatcher.get_summoner(name=summoner)
    summonerId=me['id']
    try:
        rankedst = riotWatcher.get_ranked_stats(me['id'])
        x = int(len(rankedst['champions']))
        champWinPorcentaje = 0.0
        mostPlayedChampMatchesCount =  0
        mostPlayedChamp = 0
        mostPlayedChampName = "Ninguno"
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
    except(LoLException):
        mostPlayedChampKills = 0
        mostPlayedChampDeaths = 0
        mostPlayedChampAssist = 0
        mostPlayedChampGold = 0
        mostPlayedChampCs = 0
        champWinPorcentaje = 0
        mostPlayedChampMatchesWinCount = 0
        mostPlayedChampMatchesLoseCountPorcentaje = 0
        mostPlayedChampMatchesLoseCount = 0
        mostPlayedChampKdaRatio = 0
        print ('ERROR') 
        
    MostPlayedChampInfo.objects.create(summonerId=str(me['id']),
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
    
    infoparaJson = getCacheMostPlayedChampInfo(idSum=summonerId, region=region)
    return infoparaJson
def getMostPlayedChampInfo(idSum=None, region=None):
    try :
        MostPlayedChampInfo.objects.get(summonerId = idSum)
        mostPlayedChampionInfo = getCacheMostPlayedChampInfo(idSum=idSum, region=region)
    except(ObjectDoesNotExist):
        mostPlayedChampionInfo = getApiMostPlayedChampInfo(idSum=idSum, region=region)
    return mostPlayedChampionInfo

def getCacheMostPlayedChampInfo(idSum=None, region=None):
    a = MostPlayedChampInfo.objects.get(summonerId = idSum)
    infoparaJson = str('"mostPlayedChampInfo":{"mostPlayedChampId":"' + str(a.mostPlayedChampId)
                       + '","mostPlayedChampMatchesCount":"' + str(a.mostPlayedChampMatchesCount)
                       + '","mostPlayedChampKdaRatio":"' + str(a.mostPlayedChampKdaRatio)
                       + '","mostPlayedChampName":"' + str(a.mostPlayedChampName)
                       + '","mostPlayedChampMatchesWinCount":"' + str(a.mostPlayedChampMatchesWinCount)
                       #+ '","champWinPorcentaje":"' + str(a.champWinPorcentaje)
                       + '","mostPlayedChampMatchesLoseCount":"' + str(a.mostPlayedChampMatchesLoseCount)
                       #+ '","mostPlayedChampMatchesLoseCountPorcentaje":"' + str(a.mostPlayedChampMatchesLoseCountPorcentaje)
                       + '","mostPlayedChampKills":"' + str(a.mostPlayedChampKills)
                       + '","mostPlayedChampAssist":"' + str(a.mostPlayedChampAssist)
                       + '","mostPlayedChampDeaths":"' + str(a.mostPlayedChampDeaths)
                       + '","mostPlayedChampGold":"' + str(a.mostPlayedChampGold)
                       + '","mostPlayedChampCs":"' + str(a.mostPlayedChampCs) + '"}')
    return infoparaJson
    