

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from riotwatcher import LATIN_AMERICA_SOUTH
from riotwatcher import RiotWatcher
from riotwatcher import LoLException

# Create your views here.

riotWatcher = RiotWatcher("98f4f837-c794-4a58-bcb7-b436873a03d2", default_region=LATIN_AMERICA_SOUTH)
#3239e88a-bf1e-4a88-b746-6bac356bc78a
i = 0

def home(request):
    minutos = [0,0,0,0,0]
    segundos = [0,0,0,0,0]
    free_to_play = True
    context = RequestContext(request)
    me = riotWatcher.get_summoner(name='sadjockerking')
#426174

    #-->SummonerInfo
    wins = 0
    losses = 0
    assists = 0
    kills = 0
    deaths = 0
    try:
        nombre = me['name']
        #-->Liga
        ligaInfo = riotWatcher.get_league_entry([str(me['id'])])
        liga = ligaInfo[str(me['id'])][0]['tier']
        #-->Division
        division = ligaInfo[str(me['id'])][0]['entries'][0]['division']
    except(LoLException):
        #-->En caso de no rankear
        liga = "unRanked"
        division = "unRanked"
    try:
            #-->Info como le va en rankeds
        rankedst = riotWatcher.get_ranked_stats(me['id'])

        x = int(len(rankedst['champions'])) - 1
        wins = rankedst['champions'][x]['stats']['totalSessionsWon']
        losses = rankedst['champions'][x]['stats']['totalSessionsLost']
        assists = rankedst['champions'][x]['stats']['totalAssists']
        kills = rankedst['champions'][x]['stats']['totalChampionKills']
        deaths = rankedst['champions'][x]['stats']['totalDeathsPerSession']
        totalPartidas = wins + losses
        winsPor = totalPartidas*wins/losses
    except(IndexError, LoLException):
        kills = '0'
        assists = '0'
        wins = '0'
        losses = '0'
        deaths = '0'


#-->Champion mas usado
    try:
        
        champWinPorcentaje = 0.0
        maxPartidasChamp =  0
        for q in range(x):
            partidaChampx = rankedst['champions'][q]['stats']['totalSessionsPlayed']
            if (maxPartidasChamp <= partidaChampx):
                maxPartidasChamp = partidaChampx
                maxChampPos = q
                mostPlayedChamp = rankedst['champions'][q]['id']

        maxPartidasChamp = float(maxPartidasChamp)
        champKills = rankedst['champions'][maxChampPos]['stats']['totalChampionKills']
        champDeaths = rankedst['champions'][maxChampPos]['stats']['totalDeathsPerSession']
        champAssists = rankedst['champions'][maxChampPos]['stats']['totalAssists']
        champGoldEarned = rankedst['champions'][maxChampPos]['stats']['totalGoldEarned'] / maxPartidasChamp
        champGoldEarned = round(champGoldEarned, 2)
        champMinionsKills = rankedst['champions'][maxChampPos]['stats']['totalMinionKills'] / maxPartidasChamp
        champWinPorcentaje =  rankedst['champions'][maxChampPos]['stats']['totalSessionsWon'] / maxPartidasChamp * 100
        champWinPorcentaje = round(champWinPorcentaje, 2)
        champWins = rankedst['champions'][maxChampPos]['stats']['totalSessionsWon']
        champLossesPorcentaje = rankedst['champions'][maxChampPos]['stats']['totalSessionsLost'] / maxPartidasChamp * 100
        champLossesPorcentaje = round(champLossesPorcentaje, 2)
        champLosses = rankedst['champions'][maxChampPos]['stats']['totalSessionsLost']
        maxPartidasChamp = int(maxPartidasChamp)

    except(LoLException):
            print ('ERROR')


    #-->Free Champs
    freeChamps = riotWatcher.get_all_free_champions()
    freeChampsID = []
    for j in range(len(freeChamps['champions'])):
        freeChampsID.append(freeChamps['champions'][j]['id'])

    -->Partidas
    tiempoSec = [0,0,0,0,0]
    minutos = [0,0,0,0,0]
    segundos = [0,0,0,0,0]
    champPartida = []
    try:
        for k in range(5):
            champFGc = []
            champFGd = []
            featuredGames = riotWatcher.get_featured_games()
            tiempoSec[k] = featuredGames['gameList'][k]['gameLength']
            minutos[k] = tiempoSec[k] /60
            segundos[k] =  tiempoSec[k]%60
            for u in range (len(featuredGames['gameList'][k]['participants'])):
                if featuredGames['gameList'][k]['participants'][u]['teamId'] == 100 :
                    champFGc.append(featuredGames['gameList'][k]['participants'][u]['championId'])
                else:
                    champFGd.append(featuredGames['gameList'][k]['participants'][u]['championId'])
            champPartida.append(champFGd)
            champPartida.append(champFGc)
    except (LoLException):
        print 'error'

    
    --Historial
    hpartidasId = [0,0,0,0,0,0,0,0,0,0]
    hlevelChamp = [0,0,0,0,0,0,0,0,0,0]
    hwinOrDef = [0,0,0,0,0,0,0,0,0,0]
    hchamp = [0,0,0,0,0,0,0,0,0,0]
    hgameType = [0,0,0,0,0,0,0,0,0,0]
    hmap = [0,0,0,0,0,0,0,0,0,0]
    hduracionMin = [0,0,0,0,0,0,0,0,0,0]
    hduracionSec = [0,0,0,0,0,0,0,0,0,0]
    hdeaths = [0,0,0,0,0,0,0,0,0,0]
    hkills = [0,0,0,0,0,0,0,0,0,0]
    hassists = [0,0,0,0,0,0,0,0,0,0]
    hgoldEarned = [0,0,0,0,0,0,0,0,0,0]
    hminionsKilled = [0,0,0,0,0,0,0,0,0,0]

    historial = riotWatcher.get_match_list(me['id'], None, None, None, 'SEASON2015', None, None, 0, 10)
    for o in range (len(historial['matches'])):
        z = 0
        hpartidasId[o] =  historial['matches'][o]['matchId']
        hpartida = riotWatcher.get_match(hpartidasId[o])
        while (historial['matches'][o]['champion'] != hpartida['participants'][z]['championId']):
            z+=1

        hchamp[o] = hpartida['participants'][o]['championId']
        if (hpartida['participants'][o]['stats']['winner']):
            hwinOrDef[o] = 'Victoria'
        else:
            hwinOrDef[o] = 'Derrota'
        #himgChamp
        #hlinkChamp
        hlevelChamp[o] = hpartida['participants'][o]['stats']['champLevel']
        #imgSpells
        #linkSpells
        hgameType[o] = hpartida['queueType']
        hmap[o] = hpartida['mapId']
        hduracionMin[o] = hpartida['matchDuration'] / 60
        hduracionSec[o] = hpartida['matchDuration'] % 60
        hdeaths[o] = hpartida['participants'][o]['stats']['deaths']
        hkills[o] = hpartida['participants'][o]['stats']['kills']
        hassists[o] = hpartida['participants'][o]['stats']['assists']
        hgoldEarned[o] = hpartida['participants'][o]['stats']['goldEarned']
        hminionsKilled[o] = hpartida['participants'][o]['stats']['neutralMinionsKilled'] + hpartida['participants'][o]['stats']['minionsKilled']



    return render_to_response('home.html', {
                                            'hchamp':hchamp,'hwinOrDef':hwinOrDef,
                                            'hlevelChamp':hlevelChamp ,
                                            'hgameType':hgameType , 'hmap':hmap , 
                                            'hduracionMin':hduracionMin,
                                            'hduracionSec':hduracionSec, 'hdeaths':hdeaths,
                                            'hkills':hkills, 'hassists':hassists,
                                            'hassists':hassists, 'hgoldEarned':hgoldEarned,
                                            'hminionsKilled':hminionsKilled,
#            
                                            'nombre':nombre, 'liga':liga, 'division':division,
                                            'kills':kills, 'assists':assists,
                                            'deaths':deaths,
                                            'wins':wins, 'losses':losses,
                                            'champKills':champKills, 
                                           'champDeaths':champDeaths,
                                           'champAssists':champAssists, 
                                           'champGoldEarned':champGoldEarned,
                                           'maxPartidasChamp':maxPartidasChamp,
                                           'champMinionsKills':champMinionsKills,
                                           'champWinPorcentaje':champWinPorcentaje,
                                           'champWins':champWins,
                                           'champLossesPorcentaje':champLossesPorcentaje, 
                                           'champLosses':champLosses,
                                            'minutos':minutos,
                                            'segundos':segundos, 'champFGc':champFGc,
                                            'champFGd':champFGd, 'champPartida':champPartida
                                            }, context)


def most_common(L):
    return max(g(sorted(L)), key=lambda(x, v):(len(list(v)),-L.index(x)))[0]