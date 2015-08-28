from django.db import models

#####################################################################################################
class Champions(models.Model):
#lista de todos los pj    
    botEnabled = models.BooleanField(u'Puede usarlo un bot en customs')
    active = models.BooleanField(u'Esta activado')
    botMmEnabled = models.BooleanField(u'Puede ser un bot en Coop vs IA')
    freeToPlay = models.BooleanField(u'En rotacion semanal')
    idChampion = models.BigIntegerField(u'id')
    rankedPlayEnabled = models.BooleanField(u'puede ser elegido en ranked')

#####################################################################################################
class CurrentGame(models.Model):
#Informacion de X match
    bannedChampions=models.ManyToManyField(BannedChampions)
    gameId=models.BigIntegerField(u'Id del Partido')
    gameLength=models.BigIntegerField(u'Cuantos Segundos lleva durando')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameQueueConfigId=models.BigIntegerField(u'NO TENGO IDEA :D')#The queue type (queue types are documented on the Game Constants page)
    gameStartTime=models.BigIntegerField(u'Hora de inicio en milisegundos')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    mapId=models.BigIntegerField(u'Id del mapa')
    observers=models.ManyToManyField(Observer)
    participants=models.ManyToManyField(CurrentGameParicipant)
    platformId=models.CharField(u'Id de la plataforma en la que esta siendo jugado')

class BannedChampions(models.Model):
#PJ baneados en X match
    championId=models.BigIntegerField(u'Id del Pj baneado')
    pickTurn=models.IntegerField(u'El turno en el que el pj fue baneado')
    teamId=models.BigIntegerField(u'Id del equipo que baneo el Pj')

class CurrentGameParticipant(models.Model):
#Info de un jugador en X match
    bot=models.BooleanField(u'Es un bot')
    championId=models.BigIntegerField(u'Id del jugador')
    masteries=models.ManyToManyField(Mastery)
    profileIconId=models.BigIntegerField(u'Id del icono de invocador que esta usando')
    runes=models.ManyToManyField(Rune)
    spell1Id=models.BigIntegerField(u'Id del Summoner Spell 1')
    spell2Id=models.BigIntegerField(u'Id del Summoner Spell 2')
    summonerId=models.BigIntegerField(u'Id del jugador')
    summonerName=models.CharField(u'Nombre publico del jugador')
    teamId=models.BigIntegerField(u'Id del equipo en el participa')

class Mastery(models.Model):
#Maestria individual
    masteryId=models.BigIntegerField(u'Id de la maestria')
    rank=models.IntegerField(u'Puntos puestos en esta maestria')

class Rune(models.Model):
#Runa individual
    runeId=models.BigIntegerField(u'Id de la runa')
    count=models.IntegerField(u'Cantidad de copias de esta runa')

class Observer(models.Model):
#Espectador
    encryptionKey=models.CharField(u'Key used to decrypt the spectator grid game data for playback')

#####################################################################################################

class FeaturedGames(models.Model):
#Juegos Importantes
    clientRefreshInterval=models.BigIntegerField(u'Tiempo de espera antes de  actualizar los juegos importantes')
    gameList=models.ManyToManyField(FeaturedGameInfo)

class FeaturedGamesInfo(models.Model):
#Datos de los juegos Importantes
    bannedChampions=models.ManyToManyField(BannedChampions)
    gameId=models.BigIntegerField(u'Id del Partido')
    gameLength=models.BigIntegerField(u'Cuantos Segundos lleva durando')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameQueueConfigId=models.BigIntegerField(u'The queue type (queue types are documented on the Game Constants page)')
    gameStartTime=models.BigIntegerField(u'Hora de inicio en milisegundos')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    mapId=models.BigIntegerField(u'Id del mapa')
    observers=models.ManyToManyField(Observer)
    participants=models.ManyToManyField(CurrentGameParicipant)
    platformId=models.CharField(u'Id de la plataforma en la que esta siendo jugado')

#####################################################################################################

class RecentGamesDto(models.Model):
#Juegos recientes de X jugador
    games=models.ManyToManyField(u'GameDto')
    summonerId=models.BigIntegerField(u'Id del jugador')

class GameDto(models.Model):
#Informacion de los juegos recientes de X jugador
    championId=models.IntegerField(u'Id del Pj usado')
    createDate=models.BigIntegerField(u'Fecha en la que se grabo los datos del final del partido')
    fellowPlayers=models.ManyToManyField(PlayerDto)
    gameId=models.models.BigIntegerField(u'Id de la partida')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    invalid=models.BooleanField(u'Invalid flag(Supongo que es derrota evitada)')
    ipEarned=models.IntegerField(u'IP ganado')
    level=models.IntegerField(u'Nivel en el que termino')
    mapId=models.IntegerField(u'Id del mapa')
    spell1=models.IntegerField(u'Id del Summoner Spell 1')
    spell2=models.IntegerField(u'Id del Summoner Spell 2')
    stats=models.ForeingKey(RawStatsDto)#KDA y otros datos
    subType=models.CharField(u'SubTipo de partida(NONE, NORMAL, BOT, RANKED_SOLO_5x5, RANKED_PREMADE_3x3, RANKED_PREMADE_5x5, ODIN_UNRANKED, RANKED_TEAM_3x3, RANKED_TEAM_5x5, NORMAL_3x3, BOT_3x3, CAP_5x5, ARAM_UNRANKED_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF, URF_BOT, NIGHTMARE_BOT, ASCENSION, HEXAKILL, KING_PORO, COUNTER_PICK, BILGEWATER)'),
    teamId=models.IntegerField(u'Id del lado en el que jugaba (100=Blue, 200=Purple)')
    
class PlayerDto(models.Model):
    #INFO de los pj que usa y su team
    championId=models.IntegerField("Id del campeon asociado al jugador")
    summonerId=models.BigIntegerField(u'Id del invocador')
    teamId=models.IntegerField(u'Id al equipo asociado al jugador')
    
class RawStatsDto(models.Model):
    #INFO de cada partida
    assists=models.IntegerField(u'Cantidad de asistencias')
    barracksKilled=models.IntegerField(u'Cantidad de inhibidores')
    championsKilled=models.IntegerField(u'Cantidad de asesinatos')
    combatPlayerScore=models.IntegerField(u'')
    consumablesPurchased=models.IntegerField(u'Cantidad de consumibles comprados')
    damageDealtPlayer=models.IntegerField(u'Daño a campeones')
    doubleKills=models.IntegerField(u'Cantidad de Doblekills')
    firstBlood=models.IntegerField(u'Cantidad de FirstBlood')
    gold=models.IntegerField(u'Oro ganado')
    goldEarned=models.IntegerField(u'Oro ganado')
    goldSpent=models.IntegerField(u'Oro gastado')
    item0=models.IntegerField(u'Item 0')
    item1=models.IntegerField(u'Item 1')
    item2=models.IntegerField(u'Item 2')
    item3=models.IntegerField(u'Item 3')
    item4=models.IntegerField(u'Item 4')
    item5=models.IntegerField(u'Item 5')
    item6=models.IntegerField(u'Item 6')
    itemsPurchased=models.IntegerField(u'Cantidad de items comprados')
    killingSprees=models.IntegerField(u'Cantidad de killingSprees')
    largestCriticalStrike=models.IntegerField(u'Mayor daño con un critico')
    largestKillingSpree=models.IntegerField(u'Mayor killingSprees')
    largestMultiKill=models.IntegerField(u'Mayor racha de asesinatos')
    legendaryItemsCreated=models.IntegerField(u'Items completados')
    level=models.IntegerField(u'Nivel')
    magicDamageDealtPlayer=models.IntegerField(u'Daño magico hecho')
    magicDamageDealtToChampions=models.IntegerField(u'Daño magico a campeones')
    magicDamageTaken=models.IntegerField(u'Daño magico recibido')
    minionsDenied=models.IntegerField(u'Minions denegados')
    minionsKilled=models.IntegerField(u'Minions asesinados')
    neutralMinionsKilled=models.IntegerField(u'Minions neutrales asesinados')
    neutralMinionsKilledEnemyJungle=models.IntegerField(u'Minions de la jungla enemiga asesinados')
    neutralMinionsKilledYourJungle=models.IntegerField(u'Minions de tu jungla enemiga asesinados')
    nexusKilled=models.BooleanField(u'Partida ganada'
    nodeCapture=models.IntegerField(u'Torres capturadas')
    nodeCaptureAssist=models.IntegerField(u'Asistencias al capturar torres')
    nodeNeutralize=models.IntegerField(u'Torres neutralizadas')
    nodeNeutralizeAssist=models.IntegerField(u'Asistencias para neutralizar torres')
    numDeaths=models.IntegerField(u'Muertes')
    numItemsBought=models.IntegerField(u'Cantidad de items comprados')
    objectivePlayerScore=models.IntegerField(u'Puntaje objetivo del jugador')
    pentaKills=models.IntegerField(u'Cantidad de Pentakills')
    physicalDamageDealtPlayer=models.IntegerField(u'Daño fisico hecho')
    physicalDamageDealtToChampions=models.IntegerField(u'Daño fisico a campeones')
    physicalDamageTaken=models.IntegerField(u'Daño fisico recibido')
    playerPosition=models.IntegerField(u'Posicion (TOP(1), MIDDLE(2), JUNGLE(3), BOT(4))')
    playerRole=models.IntegerField(u'Rol (DUO(1), SUPPORT(2), CARRY(3), SOLO(4))')
    quadraKills=models.IntegerField(u'Cantidad de cuadrakills')
    sightWardsBought=models.IntegerField(u'Wards rosas comprados')
    spell1Cast=models.IntegerField(u'Veces que lanzó el Spell 1')
    spell2Cast=models.IntegerField(u'Veces que lanzó el Spell 2')
    spell3Cast=models.IntegerField(u'Veces que lanzó el Spell 3')
    spell4Cast=models.IntegerField(u'Veces que lanzó el Spell 4')
    summonSpell1Cast=models.IntegerField(u'Veces que lanzó el SummonerSpell 1')
    summonSpell2Cast=models.IntegerField(u'Veces que lanzó el SummonerSpell 2')
    superMonsterKilled=models.IntegerField(u'Asesinatos de Nashor')
    team=models.IntegerField(u'Equipo')
    teamObjective=models.IntegerField(u'Objetivo del equipo')
    timePlayed=models.IntegerField(u'Tiempo jugado')
    totalDamageDealt=models.IntegerField(u'Daño total realizado')
    totalDamageDealtToChampions=models.IntegerField(u'Daño total a campeones')
    totalDamageTaken=models.IntegerField(u'Daño total recibido')
    totalHeal=models.IntegerField(u'Vida curada')
    totalPlayerScore=models.IntegerField(u'Puntaje total del jugador')
    totalScoreRank=models.IntegerField(u'Rango total del puntaje')
    totalTimeCrowdControlDealt=models.IntegerField(u'Tiempo que duro tu control de mazas')
    totalUnitsHealed=models.IntegerField(u'Unidades curadas')
    tripleKills=models.IntegerField(u'Cantidad de tripleKills')
    trueDamageDealtPlayer=models.IntegerField(u'Cantidad de True Damage realizado')
    trueDamageDealtToChampions=models.IntegerField(u'Cantidad de True Damage realizado a campeones')
    trueDamageTaken=models.IntegerField(u'Cantidad de True Damage recibido')
    turretsKilled=models.IntegerField(u'Torres que destruiste')
    unrealKill=models.IntegerField(u'Cantidad de True Damage realizado')
    victoryPointTotals=models.IntegerField(u'Puntos totales por la victoria')
    visionWardsBought=models.IntegerField(u'Wards comprados')
    wardKilled=models.IntegerField(u'Wards destruidos')
    wardPlaced=models.IntegerField(u'Wards colocados')
    win=models.BooleanField(u'Partida ganada')
    
#####################################################################################################

class LeagueDto(models.Model):
    #INFO de la liga
    entries=models.ManyToManyField(LeagueEntryDto)
    name=models.CharField(u'This name is an internal place-holder name only. Display and localization of names in the game client are handled client-side.')
    participantId=models.CharField(u'Id del perteneciente a esta liga (Sea un team o un jugador)')
    queue=models.CharField(u'(RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)')
    tier=models.CharField(u'Liga (CHALLENGER, MASTER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE)')
    
class LeagueEntryDto(models.Model):
    #Informacion sobre los integrantes de esta liga
    division=models.CharField(u'Division en la que esta')
    isFreshBlood=models.BooleanField(u'Especifica si es nuevo en la liga')
    isHotStreak=models.BooleanField(u'Especifica si está en racha')
    isInactive=models.BooleanField(u'Especifica si está inactivo')
    isVeteran=models.BooleanField(u'Especifica si es un veterano en la liga')
    leaguePoints=models.IntegerField(u'Puntos en la liga')
    losses=models.IntegerField(u'Derrotas')
    miniSeries=models.ForeingKey(MiniSeriesDto)
    playerOrTeamId=models.CharField(u'Id del jugador o del team')
    playerOrTeamName=models.CharField(u'Nombre del jugador o del team')
    wins=models.IntegerField(u'Victorias')
    
class MiniSeriesDto(models.Model):
    #Informacion de las miniseries
    losses=models.IntegerField(u'Numero de partidas que perdió en promo')
    progress=models.CharField(u'Muestra la promocion actual (W=Victoria L=Derrota N=Falta Jugar)')
    target=models.IntegerField(u'Numero de victorias necesarias para promocionar')
    wins=models.IntegerField(u'Numero de partidas que ganó en promo')
    
#####################################################################################################

class ChampionListDto(models.Model):
    #Lista para ver INFO de los campeones
    data
    format=models.CharField(u'')
    keys
    type=models.CharField(u'')
    version=models.CharField(u'')
    
class ChampionsDto(models.Model):
    #Datos de los campeones
    allytips
    blurb=models.CharField(u'')
    enemytips
    id=models.IntegerField(u'')
    image
    info
    key=models.CharField(u'')
    lore=models.CharField(u'')
    name=models.CharField(u'')
    partype=models.CharField(u'')
    passive
    recommended
    skins
    spells
    stats
    tags
    title=models.CharField(u'')
    
class ChampionsSpellDto(models.Model):
    #INFO de los spells de cada campeon
    altimages
    cooldown
    cooldownBurn=models.CharField(u'')
    cost
    costBurn=models.CharField(u'')
    costType=models.CharField(u'')
    description=models.CharField(u'')
    effect
    effectBurn
    image
    key=models.CharField(u'')
    leveltip
    maxrank=models.IntegerField(u'')
    name=models.CharField(u'')
    range
    rangeBurn
    resource=models.CharField(u'')
    sanitizedTooltip=models.CharField(u'')
    sanitizedDescription=models.CharField(u'')
    tooltip=models.CharField(u'')
    vars
    
    
class ImageDto(models.Model)
    #Datos de las imagenes
    full=models.CharField(u'')
    group=models.CharField(u'')
    h=models.IntegerField(u'')
    sprite=models.CharField(u'')
    w=models.IntegerField(u'')
    x=models.IntegerField(u'')
    y=models.IntegerField(u'')
    
class InfoDto(models.Model):
    #INFO de los campeones
    attack=models.IntegerField(u'')
    defense=models.IntegerField(u'')
    difficulty=models.IntegerField(u'')
    magic=models.IntegerField(u'')

class PassiveDto(models.Model):
    #Data de la pasiva del campeon
    description=models.CharField(u'')
    image
    name=models.CharField(u'')
    sanitizedDescription=models.CharField(u'')
    
class RecommendedDto(models.Model):
    #Data de las recomendaciones para los campeones
    blocks
    champion=models.CharField(u'')
    map=models.CharField(u'')
    mode=models.CharField(u'')
    priority
    title=models.CharField(u'')
    type=models.CharField(u'')
    
class SkinDto(models.Model):
    #Data de los Skins
    id=models.IntegerField(u'')
    name=models.CharField(u'')
    num=models.IntegerField(u'')
    
class StatsDto (models.Model):
    #Data de las estadisticas del campeon
    armor
    armorperlevel
    attackdamage
    attackdamageperlevel
    crit
    critperlevel
    hp
    hpperlevel
    hpregen
    hpregenperlevel
    movespeed
    mp
    mpperlevel
    mpregen
    mpregenperlevel
    spellblock
    spellblockperlevel
    
class LevelTipDto(models.Model):
    #This object contains champion level tip data.
    effect
    label
    
class SpellVarsDto(models.Model):
    #Data de los spells
    coeff
    dyn=models.CharField(u'')
    keyslink=models.CharField(u'')
    link=models.CharField(u'')
    ranksWith=models.CharField(u'')
    
class BlockDto(models.Model):
    #Data del bloque de recomendaciones
    items
    recMath
    type=models.CharField(u'')
    
class BlockItemDto(models.Model):
    count=models.IntegerField(u'')
    id=models.IntegerField(u'')