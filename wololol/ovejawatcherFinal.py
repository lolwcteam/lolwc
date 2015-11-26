#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importando
import json
import requests
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from lol.models import SummonerInfo, MostPlayedChampInfo, SummonerProfile, History

from lol.riotwatcher import RiotWatcher
from lol.riotwatcher import LoLException
from lol.riotwatcher import BRAZIL
from lol.riotwatcher import EUROPE_NORDIC_EAST
from lol.riotwatcher import EUROPE_WEST
from lol.riotwatcher import KOREA
from lol.riotwatcher import LATIN_AMERICA_NORTH
from lol.riotwatcher import LATIN_AMERICA_SOUTH
from lol.riotwatcher import NORTH_AMERICA
from lol.riotwatcher import OCEANIA
from lol.riotwatcher import RUSSIA
from lol.riotwatcher import TURKEY
#Apikey mayo: 3239e88a-bf1e-4a88-b746-6bac356bc78a
#Apikey mauro: 98f4f837-c794-4a58-bcb7-b436873a03d2
riotWatcher = RiotWatcher("a129b7be-5979-46f1-8abc-5c99b9395c25", default_region=LATIN_AMERICA_SOUTH) #Seteando mi clave para hacer APIcalls
#Diccionario con Id de los campeones
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

historyDic = {
    "map":{
        "1":"La Grieta del Invocador de Verano",
        "2":"La Grieta del Invocador de Invierno",
        "3":"Mapa del Tutorial",
        "4":"El Bosque Retorcido Original",
        "8":"La Cicatriz de Cristal",
        "10":"El Bosque Retorcido",
        "11":"La Grieta del Invocador",
        "12":"El Abismo de los Lamentos",
        "14":"El Puente del Carnicero",
    },
    "gameSubType":{
        "NONE":"Partida Personalizada",
        "NORMAL":"Normal 5 vs 5",
        "NORMAL_3x3":"Normal 3 vs 3",
        "ODIN_UNRANKED":"Partida Dominion",
        "ARAM_UNRANKED_5x5":"ARAM 5 vs 5",
        "BOT":"Partida Contra Bots",
        "BOT_3x3":"Partida Contra Bots 3 vs 3",
        "RANKED_SOLO_5x5":"Partida Clasificatoria 5 vs 5",
        "RANKED_TEAM_3x3":"Clasificatoria por Equipos 3 vs 3",
        "RANKED_TEAM_5x5":"Clasificatoria por Equipos 5 vs 5",
        "ONEFORALL_5x5":"Uno para Todos 5 vs 5",
        "FIRSTBLOOD_1x1":"Primera Sangre 1 vs 1",
        "FIRSTBLOOD_2x2":"Primera Sangre 2 vs 2",
        "SR_6x6":"Hexakill 6 vs 6",
        "CAP_5x5":"Creador de Equpos 5 vs 5",
        "URF":"Ultra Rápido y Furioso",
        "URF_BOT":"URF vs Bots",
        "NIGHTMARE_BOT":"Bots de Pesadilla",
        "ASCENSION":"Ascension",
        "HEXAKILL":"Hexakill Bosque Retorcido",
        "KING_PORO":"Rey Poro",
        "COUNTER_PICK":"Nemesis",
        "BILGEWATER":"Mercado Negro",
    }
}

leagueValue = {
    'unknow':100,
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
def getSummoner(summoner=None, idSum=None, region=None): #Funcion que revisa si el jugador está en la base de datos, o hay que crearlo
    try :
        if idSum != None:
            SummonerInfo.objects.get(summonerId = idSum, summonerRegion = region)
            summonerInfo = getCacheSummoner(idSum = summonerId, region = region)
        else:
            summoner = summoner.lower()
            b = SummonerInfo.objects.get(summonerUserName = summoner, summonerRegion = region)
            idSum = b.summonerId
            summonerInfo = getCacheSummoner(idSum = idSum, region = region)
    except(ObjectDoesNotExist):
        summonerInfo = getApiSummoner(idSum = idSum, summoner=summoner, region = region)
    jsonFinal = json.loads(str(summonerInfo))
    return jsonFinal

def getApiSummoner(summoner=None, idSum=None, region=None):
    if idSum!=None:
        me = riotWatcher.get_summoner(_id=idSum)
    else:
        me = riotWatcher.get_summoner(name=summoner, region=region)
    print("CHABON ENCONTRADO")
    summonerName = str(me['name'])
    summonerUserName = str(summonerName).lower()
    summonerId = str(me['id'])
    summonerImg = str(me['profileIconId'])
    summonerRegion = str(region)
    league3v3Name = 'Unranked'
    league3v3Tier = 'unknow'
    league3v3Division = ''
    league3v3Lp = 0
    leagueTeamName = 'Unranked'
    leagueTeamTier = 'unknow'
    leagueTeamDivision = ''
    leagueTeamLp = 0
    x = 0
    summonerLeague = "unRanked"
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
    try:
        rankedst = riotWatcher.get_ranked_stats(summonerId)
        print("RANKED STATS PEDIDOS")
        summonerLeagueInfo = riotWatcher.get_league_entry([summonerId])
        print("INFO DE LIGA PEDIDA")
        for x in range(len(summonerLeagueInfo[summonerId])):
        #################3vs3#################
            if(summonerLeagueInfo[summonerId][x]['queue'] == 'RANKED_TEAM_3x3'):
                thisLeagueTier = str(summonerLeagueInfo[summonerId][x]['tier']).lower().capitalize()
                thisLeagueDivision = str(summonerLeagueInfo[summonerId][x]['entries'][0]['division'])
                thisLeague = thisLeagueTier + ' ' + thisLeagueDivision
                thisLeagueValue = leagueValue[thisLeague]
                if(league3v3Tier!='unknow'):
                    topLeague = str(league3v3Tier) + ' ' + str(league3v3Division)
                else:
                    topLeague = 'unknow'
                topLeagueValue = LeagueValue[topLeagueValue]
                if(thisLeagueValue<topLeagueValue):
                    league3v3Name = str(summonerLeagueInfo[summonerId][x]['name'])
                    league3v3Tier = thisLeagueTier
                    league3v3Division = thisLeagueDivision
                    league3v3Lp = summonerLeagueInfo[summonerId][x]['entries'][0]['leaguePoints']
        #################Team5vs5#################
            elif(summonerLeagueInfo[summonerId][x]['queue'] == 'RANKED_TEAM_5x5'):
                thisLeagueTier = str(summonerLeagueInfo[summonerId][x]['tier']).lower().capitalize()
                thisLeagueDivision = str(summonerLeagueInfo[summonerId][x]['entries'][0]['division'])
                thisLeague = thisLeagueTier + ' ' + thisLeagueDivision
                thisLeagueValue = leagueValue[thisLeague]
                if(leagueTeamTier!='unknow'):
                    topLeague = str(leagueTeamTier) + ' ' + str(leagueTeamDivision)
                else:
                    topLeague = 'unknow'
                topLeagueValue = leagueValue[topLeague]
                if(thisLeagueValue<topLeagueValue):
                    leagueTeamName = str(summonerLeagueInfo[summonerId][x]['name'])
                    leagueTeamTier = thisLeagueTier
                    leagueTeamDivision = thisLeagueDivision
                    leagueTeamLp = summonerLeagueInfo[summonerId][x]['entries'][0]['leaguePoints']
        #################SoloQ5vs5#################
            else:
                wins = 0
                losses = 0
                assists = 0
                kills = 0
                deaths = 0
                summonerLeague = summonerLeagueInfo[summonerId][x]['tier']
                summonerDivision = summonerLeagueInfo[summonerId][x]['entries'][0]['division']
                summonerLeagueName = summonerLeagueInfo[summonerId][x]['name']
                summonerLeaguePoints = summonerLeagueInfo[summonerId][x]['entries'][0]['leaguePoints']
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
    except(LoLException):
        mostPlayedChamp = ''
        mostPlayedChampName = ''
        mostPlayedChampMatchesCount = ''
        mostPlayedChampMatchesWinCount = ''
        mostPlayedChampMatchesLoseCount = ''
        mostPlayedChampKdaRatio = ''
        mostPlayedChampKills = ''
        mostPlayedChampDeaths = ''
        mostPlayedChampAssist = ''
        mostPlayedChampCs = ''
        mostPlayedChampGold = ''
        summonerImg = ''
        summonerName = ''
        summonerUserName = ''
        summonerLeague = ''
        summonerDivision = ''
        summonerKills = ''
        summonerDeaths = ''
        summonerAssists = ''
        summonerWinrate = ''
        summonerRegion = ''
        summonerKdaRatio = ''
        summonerId = ''
        summonerLeagueName = ''
        summonerLeaguePoints = ''
        leagueTeamName = ''
        leagueTeamTier = ''
        leagueTeamDivision = ''
        leagueTeamLp = ''
        league3v3Name = ''
        league3v3Tier = ''
        league3v3Division = ''
        league3v3Lp = ''

    listapartidas=''
    partida=''
    hpartidasId = 0
    champLvl = 0
    isWin = False
    champId = 0
    gameType = 0
    hmap = 0
    hduracionMin = 0
    hduracionSec = 0
    deaths = 0
    kills = 0
    assists = 0
    goldGained = 0
    creepScore= 0
    piEarned = 0
    createDate = 0
    item1 = 0
    item2 = 0
    item3 = 0
    item4 = 0
    item4 = 0
    item6 = 0
    item7 = 0
    history = {}

    historial = riotWatcher.get_recent_games(summonerId)
    print("HISTORIAL BUSCADO")
    for o in range(len(historial['games'])):
        champLvl = historial['games'][o]['stats']['level']
        if (historial['games'][o]['stats']['win']):
            isWin = '1'
        else:
            isWin = '0'
        createDate = str(historial['games'][o]['createDate'])
        createDate = createDate[0:10]
        createTime = datetime.datetime.fromtimestamp(int(createDate)).strftime('%H:%M:%S')
        createDate = datetime.datetime.fromtimestamp(int(createDate)).strftime('%Y-%m-%d')
        champId = historial['games'][o]['championId']
        champName = champsId[str(champId)]
        spell1 = historial['games'][o]['spell1']
        spell2 = historial['games'][o]['spell2']
        gameType = historial['games'][o]['subType']
        gameType = historyDic['gameSubType'][gameType]
        hmap = str(historial['games'][o]['mapId'])
        hmap = historyDic['map'][hmap]
        hduracionSec = historial['games'][o]['stats']['timePlayed']
        hduracionMin = historial['games'][o]['stats']['timePlayed'] / 60
        if not 'numDeaths' in historial['games'][o]['stats']:
            deaths = 0
        else:
            deaths = historial['games'][o]['stats']['numDeaths']
        if not 'championsKilled' in historial['games'][o]['stats']:
            kills = 0
        else:
            kills = historial['games'][o]['stats']['championsKilled']
        if not 'assists' in historial['games'][o]['stats']:
            assists = 0
        else:
            assists = historial['games'][o]['stats']['assists']
        goldGained = historial['games'][o]['stats']['goldEarned']
        if not 'minionsKilled' in  historial['games'][o]['stats']:
            creepScore = 0
        else:
            creepScore = historial['games'][o]['stats']['minionsKilled']
        piEarned = historial['games'][o]['ipEarned']
        if not 'item0' in  historial['games'][o]['stats']:
            item1 = 'Vacio'
        else:
            item1 = historial['games'][o]['stats']['item0']
        if not 'item1' in  historial['games'][o]['stats']:
            item2 = 'Vacio'
        else:
            item2 = historial['games'][o]['stats']['item1']
        if not 'item2' in  historial['games'][o]['stats']:
            item3 = 'Vacio'
        else:
            item3 = historial['games'][o]['stats']['item2']
        if not 'item3' in  historial['games'][o]['stats']:
            item4 = 'Vacio'
        else:
            item4 = historial['games'][o]['stats']['item3']
        if not 'item4' in  historial['games'][o]['stats']:
            item5 = 'Vacio'
        else:
            item5 = historial['games'][o]['stats']['item4']
        if not 'item5' in  historial['games'][o]['stats']:
            item6 = 'Vacio'
        else:
            item6 = historial['games'][o]['stats']['item5']
        if not 'item6' in  historial['games'][o]['stats']:
            item7 = 'Vacio'
        else:
            item7 = historial['games'][o]['stats']['item6']

        partida = str('{"isWin":"' + str(isWin)
                                 + '","champId":"' + str(champId)
                                 + '","champName":"' + str(champName)
                                 + '","champLvl":"' + str(champLvl)
                                 + '","spell1":"' + str(spell1)
                                 + '","spell2":"' + str(spell2)
                                 + '","gameSubType":"' + str(gameType)
                                 + '","map":"' + str(hmap)
                                 + '","timePlayed":"' + str(hduracionSec)
                                 + '","ipEarned":"' + str(piEarned)
                                 + '","kills":"' + str(kills)
                                 + '","deaths":"' + str(deaths)
                                 + '","assists":"' + str(assists)
                                 + '","goldGained":"' + str(goldGained)
                                 + '","creepScore":"' + str(creepScore)
                                 + '","createDate":"' + str(createDate)
                                 + '","createTime":"' + str(createTime)
                                 + '","item1":"' + str(item1)
                                 + '","item2":"' + str(item2)
                                 + '","item3":"' + str(item3)
                                 + '","item4":"' + str(item4)
                                 + '","item5":"' + str(item5)
                                 + '","item6":"' + str(item6)
                                 + '","item7":"' + str(item7)
                                 + '"}'
                                )
        if(listapartidas==''):
            listapartidas = '"history":[' + partida
        elif(o == len(historial['games'])-1):
            listapartidas = listapartidas + ',' +partida + ']'
        else:
            listapartidas = listapartidas + ',' + partida
    History.objects.create(summonerId=summonerId,
                           jsonInfo=listapartidas)

    MostPlayedChampInfo.objects.create(summonerId=summonerId,
                                       mostPlayedChampId = str(mostPlayedChamp),
                                       mostPlayedChampName = str(mostPlayedChampName),
                                       mostPlayedChampMatchesCount = str(mostPlayedChampMatchesCount),
                                       mostPlayedChampMatchesWinCount = str(mostPlayedChampMatchesWinCount),
                                       mostPlayedChampMatchesLoseCount = str(mostPlayedChampMatchesLoseCount),
                                       mostPlayedChampKdaRatio = str(mostPlayedChampKdaRatio),
                                       mostPlayedChampKills = str(mostPlayedChampKills),
                                       mostPlayedChampDeaths = str(mostPlayedChampDeaths),
                                       mostPlayedChampAssist = str(mostPlayedChampAssist),
                                       mostPlayedChampCs = str(mostPlayedChampCs),
                                       mostPlayedChampGold = str(mostPlayedChampGold))

    SummonerInfo.objects.create(summonerId = summonerId,
                                summonerServer = str(summonerRegion).upper(),
                                summonerImg = str(summonerImg),
                                summonerName = str(summonerName),
                                summonerUserName = str(summonerUserName),
                                summonerLeague = str(summonerLeague),
                                summonerDivision = str(summonerDivision),
                                summonerKills = str(summonerKills),
                                summonerDeaths = str(summonerDeaths),
                                summonerAssists = str(summonerAssists),
                                summonerWinrate = str(summonerWinrate),
                                summonerRegion = str(summonerRegion),
                                summonerKdaRatio = str(summonerKdaRatio))

    SummonerProfile.objects.create(summonerId = str(summonerId),
                                   leagueSoloQName = str(summonerLeagueName),
                                   leagueSoloQTier = str(summonerLeague),
                                   leagueSoloQDivision = str(summonerDivision),
                                   leagueSoloQLp = str(summonerLeaguePoints),
                                   leagueTeamName = str(leagueTeamName),
                                   leagueTeamTier = str(leagueTeamTier),
                                   leagueTeamDivision = str(leagueTeamDivision),
                                   leagueTeamLp = str(leagueTeamLp),
                                   league3v3Name = str(league3v3Name),
                                   league3v3Tier = str(league3v3Tier),
                                   league3v3Division = str(league3v3Division),
                                   league3v3Lp = str(league3v3Lp))

    summonerJson = getCacheSummoner(idSum=summonerId, region=summonerRegion)
    return summonerJson

def getCacheSummoner(idSum=None, region=None): #Busca en la base de datos un jugador
    a = MostPlayedChampInfo.objects.get(summonerId = idSum)
    b = SummonerInfo.objects.get(summonerId = idSum, summonerRegion=region)
    c = SummonerProfile.objects.get(summonerId = idSum)
    d = History.objects.get(summonerId = idSum)
    summoner = str('"summonerInfo":{"summonerId":"' + str(b.summonerId)
                    + '","summonerImg":"' + str(b.summonerImg)
                    + '","summonerName":"' + str(b.summonerName)
                    + '","summonerUserName":"' + str(b.summonerUserName)
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
                  + '","leagueSoloQTier":"' + str(c.leagueSoloQTier).lower().capitalize()
                  + '","leagueSoloQDivision":"' + str(c.leagueSoloQDivision)
                  + '","leagueSoloQLp":"' + str(c.leagueSoloQLp)
                  + '","leagueTeamName":"' + str(c.leagueTeamName)
                  + '","leagueTeamTier":"' + str(c.leagueTeamTier).lower().capitalize()
                  + '","leagueTeamDivision":"' + str(c.leagueTeamDivision)
                  + '","leagueTeamLp":"' + str(c.leagueTeamLp)
                  + '","league3v3Name":"' + str(c.league3v3Name)
                  + '","league3v3Tier":"' + str(c.league3v3Tier).lower().capitalize()
                  + '","league3v3Division":"' + str(c.league3v3Division)
                  + '","league3v3Lp":"' + str(c.league3v3Lp) + '"}')
    history = d.jsonInfo
    savedJson =  '{' + summoner + ',' + favoriteChamp + ',' + profile + ',' + history + '}'
    return savedJson
