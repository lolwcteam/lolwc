from django.db import models
#Las variables que estaban reservadas cambiaron su nombre por: "ex" + "NOMBREdeVARIABLE"
#Las variables son: format=exFormat, type=exType, id=exId, range=exRange, vars=exVars, map=exMap
#Tareas por terminar estan Taggeadas como #TODO
#Los FloatField seran rellenados con valores del tipo "double"

class AggregatedStatsDto(models.Model): #Datos de un Jugador
    averageAssists=models.IntegerField(u'Promedio de asistencias en dominion') # Dominion only.
    averageChampionsKilled=models.IntegerField(u'Promedio de kills en dominion') # Dominion only.
    averageCombatPlayerScore=models.IntegerField(u'Promedio de los puntos de batalla en dominion') # Dominion only.
    averageNodeCapture=models.IntegerField(u'Promedio de torres capturadas en dominion') # Dominion only.
    averageNodeCaptureAssist=models.IntegerField(u'Promedio de asistencias capturando torres en dominion') # Dominion only.
    averageNodeNeutralize=models.IntegerField(u'Promedio de torres neutralizadas en dominion') # Dominion only.
    averageNodeNeutralizeAssist=models.IntegerField(u'Promedio de asistencias neutralizando torres en dominion') # Dominion only.
    averageNumDeaths=models.IntegerField(u'Promedio de muertes en dominion') # Dominion only.
    averageObjectivePlayerScore=models.IntegerField(u'Promedio de puntos de objetivo del jugador en dominion') # Dominion only.
    averageTeamObjective=models.IntegerField(u'Promedio de puntos del equipo en dominion') # Dominion only.
    averageTotalPlayerScore=models.IntegerField(u'Promedio de puntos totales en dominion') # Dominion only.
    botGamesPlayed=models.IntegerField(u'Partidas jugadas en modo "vs IA"')
    killingSpree=models.IntegerField(u'Cantidad de rachas de asesinatos')
    maxAssists=models.IntegerField(u'Cantidad maxima de asistencias en dominion') # Dominion only.
    maxChampionsKilled=models.IntegerField(u'Cantidad maxima de campeones asesinados en una partida')
    maxCombatPlayerScore=models.IntegerField(u'Cantidad maxima de puntos de combate en dominion') # Dominion only.
    maxLargestCriticalStrike=models.IntegerField(u'Mayor daño realizado con un critico')
    maxLargestKillingSpree=models.IntegerField(u'Mayor racha de asesinatos')
    maxNodeCapture=models.IntegerField(u'Cantidad maxima de torres capturados en dominion') # Dominion only.
    maxNodeCaptureAssist=models.IntegerField(u'Cantidad maxima de asistencias neutralizando torres en dominion') # Dominion only.
    maxNodeNeutralize=models.IntegerField(u'Cantidad maxima de torres neutralizados en dominion') # Dominion only.
    maxNodeNeutralizeAssist=models.IntegerField(u'Cantidad maxima de asistencias neutralizando torres en dominion') # Dominion only.
    maxNumDeaths=models.IntegerField(u'Cantidad maxima de muertes en dominion') # Only returned for ranked statistics.
    maxObjectivePlayerScore=models.IntegerField(u'Cantidad maxima ') # Dominion only.
    maxTeamObjective=models.IntegerField(u'Cantidad maxima de puntaje de objetivo del equipo en dominion') # Dominion only.
    maxTimePlayed=models.IntegerField(u'Partida mas larga jugada')
    maxTimeSpentLiving=models.IntegerField(u'Maxima cantidad de tiempo sin morir')
    maxTotalPlayerScore=models.IntegerField(u'Cantidad maxima de puntaje total del jugador en dominion') # Dominion only.
    mostChampionKillsPerSession=models.IntegerField(u'Cantidad maxima de asesinatos en una partida')
    mostSpellsCast=models.IntegerField(u'Cantidad maxima de hechizos lanzados en una partida')
    normalGamesPlayed=models.IntegerField(u'Cantidad de partidas normales jugadas')
    rankedPremadeGamesPlayed=models.IntegerField(u'Cantidad de rankeds jugadas en premade')
    rankedSoloGamesPlayed=models.IntegerField(u'Cantidad de rankeds jugadas en solitario')
    totalAssists=models.IntegerField(u'Asistencias totales')
    totalChampionKills=models.IntegerField(u'Total de campeones asesinados')
    totalDamageDealt=models.IntegerField(u'Total de daño realizado')
    totalDamageTaken=models.IntegerField(u'Total de daño recibido')
    totalDeathsPerSession=models.IntegerField(u'Total de muertes en una partida (solo en rankeds)') # Only returned for ranked statistics.
    totalDoubleKills=models.IntegerField(u'Total de doublekills')
    totalFirstBlood=models.IntegerField(u'Total de "Primeras Sangres" realizadas')
    totalGoldEarned=models.IntegerField(u'Total de oro ganado')
    totalHeal=models.IntegerField(u'Total de vida curada')
    totalMagicDamageDealt=models.IntegerField(u'Total de daño magico realizado')
    totalMinionKills=models.IntegerField(u'Total de minions asesinados')
    totalNeutralMinionsKilled=models.IntegerField(u'Total de minions neutrales asesinados')
    totalNodeCapture=models.IntegerField(u'Total de nodos capturados en dominion') # Dominion only.
    totalNodeNeutralize=models.IntegerField(u'Total de nodos neutralizados en dominion') # Dominion only.
    totalPentaKills=models.IntegerField(u'Total de pentakills realizadas')
    totalPhysicalDamageDealt=models.IntegerField(u'Total de daño fisico realizado')
    totalQuadraKills=models.IntegerField(u'Total de quadrakills realizadas')
    totalSessionsLost=models.IntegerField(u'Total de partidas perdidas')
    totalSessionsPlayed=models.IntegerField(u'Total de partidas jugadas')
    totalSessionsWon=models.IntegerField(u'Total de partidas ganadas')
    totalTripleKills=models.IntegerField(u'Total de triplekills')
    totalTurretsKilled=models.IntegerField(u'Total de torres destruidas')
    totalUnrealKills=models.IntegerField(u'Total de ejecuciones')

class BannedChampion(models.Model):  #Datos individuales de un personaje banneado en una partida
    championId=models.IntegerField(u'Id del campeon banneado')
    pickTurn=models.IntegerField(u'Turno en el que fue banneado')

class BannedChampions(models.Model):  #Lista de los personajes banneados en una partida
    championId=models.BigIntegerField(u'Id del campeon baneado')
    pickTurn=models.IntegerField(u'El turno en el que el campeon fue baneado')
    teamId=models.BigIntegerField(u'Id del equipo que baneo el campeon')

class BasicDataDto(models.Model):  #Datos basicos de un Item
    colloq=models.CharField(u'')
    consumeOnFull=models.BooleanField(u'')
    consumed=models.BooleanField(u'')
    depth=models.IntegerField(u'')
    description=models.CharField(u'')
    exFrom=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    gold=#TODO#GoldDto #Data Dragon includes the gold field for basic data, which is shared by both rune and item. However, only items have a gold field on them, representing their gold cost in the store. Since runes are not sold in the store, they have no gold cost.
    group=models.CharField(u'')
    hideFromAll=models.BooleanField(u'')
    exId=models.IntegerField(u'')
    image=#TODO#ImageDto
    inStore=models.BooleanField(u'')
    into=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    maps=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, boolean
    name=models.CharField(u'')
    plaintext=models.CharField(u'')
    requiredChampion=models.CharField(u'')
    rune=#TODO#MetaDataDto
    sanitizedDescription=models.CharField(u'')
    specialRecipe=models.IntegerField(u'')
    stacks=models.IntegerField(u'')
    stats=#TODO#BasicDataStatsDto
    tags=models.TextField(u'')#Lista en JSON compuesta de valores tipo string

class BasicDataStatsDto(models.Model):  #Datos de las bonificaciones de un Item
    FlatArmorMod=models.FloatField(u'')
    FlatAttackSpeedMod=models.FloatField(u'')
    FlatBlockMod=models.FloatField(u'')
    FlatCritChanceMod=models.FloatField(u'')
    FlatCritDamageMod=models.FloatField(u'')
    FlatEXPBonus=models.FloatField(u'')
    FlatEnergyPoolMod=models.FloatField(u'')
    FlatEnergyRegenMod=models.FloatField(u'')
    FlatHPPoolMod=models.FloatField(u'')
    FlatHPRegenMod=models.FloatField(u'')
    FlatMPPoolMod=models.FloatField(u'')
    FlatMPRegenMod=models.FloatField(u'')
    FlatMagicDamageMod=models.FloatField(u'')
    FlatMovementSpeedMod=models.FloatField(u'')
    FlatPhysicalDamageMod=models.FloatField(u'')
    FlatSpellBlockMod=models.FloatField(u'')
    PercentArmorMod=models.FloatField(u'')
    PercentAttackSpeedMod=models.FloatField(u'')
    PercentBlockMod=models.FloatField(u'')
    PercentCritChanceMod=models.FloatField(u'')
    PercentCritDamageMod=models.FloatField(u'')
    PercentDodgeMod=models.FloatField(u'')
    PercentEXPBonus=models.FloatField(u'')
    PercentHPPoolMod=models.FloatField(u'')
    PercentHPRegenMod=models.FloatField(u'')
    PercentLifeStealMod=models.FloatField(u'')
    PercentMPPoolMod=models.FloatField(u'')
    PercentMPRegenMod=models.FloatField(u'')
    PercentMagicDamageMod=models.FloatField(u'')
    PercentMovementSpeedMod=models.FloatField(u'')
    PercentPhysicalDamageMod=models.FloatField(u'')
    PercentSpellBlockMod=models.FloatField(u'')
    PercentSpellVampMod=models.FloatField(u'')
    rFlatArmorModPerLevel=models.FloatField(u'')
    rFlatArmorPenetrationMod=models.FloatField(u'')
    rFlatArmorPenetrationModPerLevel=models.FloatField(u'')
    rFlatCritChanceModPerLevel=models.FloatField(u'')
    rFlatCritDamageModPerLevel=models.FloatField(u'')
    rFlatDodgeMod=models.FloatField(u'')
    rFlatDodgeModPerLevel=models.FloatField(u'')
    rFlatEnergyModPerLevel=models.FloatField(u'')
    rFlatEnergyRegenModPerLevel=models.FloatField(u'')
    rFlatGoldPer10Mod=models.FloatField(u'')
    rFlatHPModPerLevel=models.FloatField(u'')
    rFlatHPRegenModPerLevel=models.FloatField(u'')
    rFlatMPModPerLevel=models.FloatField(u'')
    rFlatMPRegenModPerLevel=models.FloatField(u'')
    rFlatMagicDamageModPerLevel=models.FloatField(u'')
    rFlatMagicPenetrationMod=models.FloatField(u'')
    rFlatMagicPenetrationModPerLevel=models.FloatField(u'')
    rFlatMovementSpeedModPerLevel=models.FloatField(u'')
    rFlatPhysicalDamageModPerLevel=models.FloatField(u'')
    rFlatSpellBlockModPerLevel=models.FloatField(u'')
    rFlatTimeDeadMod=models.FloatField(u'')
    rFlatTimeDeadModPerLevel=models.FloatField(u'')
    rPercentArmorPenetrationMod=models.FloatField(u'')
    rPercentArmorPenetrationModPerLevel=models.FloatField(u'')
    rPercentAttackSpeedModPerLevel=models.FloatField(u'')
    rPercentCooldownMod=models.FloatField(u'')
    rPercentCooldownModPerLevel=models.FloatField(u'')
    rPercentMagicPenetrationMod=models.FloatField(u'')
    rPercentMagicPenetrationModPerLevel=models.FloatField(u'')
    rPercentMovementSpeedModPerLevel=models.FloatField(u'')
    rPercentTimeDeadMod=models.FloatField(u'')
    rPercentTimeDeadModPerLevel=models.FloatField(u'')

class BlockDto(models.Model):  #Datos de cada bloque
    items=models.TextField(u'')#Lista en JSON compuesta de valores tipo BlockItemDto
    recMath=models.BooleanGield(u'Item con "Unica Pasiva"')
    exType=models.CharField(u'Tipo de los items')

class BlockItemDto(models.Model):  #Datos de qué item aparece en un bloque
    count=models.IntegerField(u'Cantidad de el item a comprar')
    exId=models.IntegerField(u'ID del item') 

class ChampionListDto(models.Model):  #Lista de los campeones
    champions=models.TextField(u'')#Lista en JSON compuesta de valores tipo ChampionDto

class ChampionStatsDto(models.Model):  #Stats de cada campeon
    exId=models.IntegerField(u'') # Champion ID. Note that champion ID 0 represents the combined stats for all champions. For static information correlating to champion IDs, please refer to the LoL Static Data API.
    stats=#TODO#AggregatedStatsDto # Aggregated stats associated with the champion.

class ChampionsDto(models.Model):  #Detalles de las limitaciones de cada campeon
    active=models.BooleanField(u'')
    botEnabled=models.BooleanField(u'')
    botMmEnabled=models.BooleanField(u'')
    freeToPlay=models.BooleanField(u'')
    exId=models.BigIntegerField(u'')
    rankedPlayEnabled=models.BooleanField(u'')

class ChampionsSpellDto(models.Model):  #Informacion de los spells de cada campeon
    altimages=models.TextField(u'')#Lista en JSON compuesta de valores tipo ImageDto
    cooldown=models.TextField(u'')#Lista en JSON compuesta de valores tipo double
    cooldownBurn=models.CharField(u'Cooldown a travez de los niveles de la habilidad')
    cost=models.TextField(u'')#Lista en JSON compuesta de valores tipo int
    costBurn=models.CharField(u'Coste de Energia/Mana/Furia/Heat (no incluye coste de vida)')
    costType=models.CharField(u'Tipo de Coste pofcurrentHealth(vida)/Energia/Mana/Furia/Heat(calor)')
    description=models.CharField(u'Descripcion de la habilidad')
    effect=models.TextField(u'')#Lista en JSON compuesta de valores tipo object # This field is a List of List of Double.
    effectBurn=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    image=#TODO#ImageDto
    key=models.CharField(u'Key de la habilidad')
    leveltip=#TODO#LevelTipDto
    maxrank=models.IntegerField(u'Nivel maximo de la habilidad')
    name=models.CharField(u'Nombre de la habilidad')
    exRange=#TODO#Object # This field is either a List of Integer or the String 'self' for spells that target one's own champion.
    rangeBurn=models.CharField(u'Rango a travez de los niveles de la habilidad')
    resource=models.CharField(u'Muestra el coste de la habilidad, obteniendolo desde la variable "cost"')
    sanitizedTooltip=models.CharField(u'Funcion concreta de la habilidad')
    sanitizedDescription=models.CharField(u'Descripcion concreta de lo que hace la habilidad')
    tooltip=models.CharField(u'Funcion de la habilidad')
    exVars=#TODO#SpellsVarDto

class CurrentGameInfo(models.Model):  #Informacion de una partida en especifico
    bannedChampions=models.TextField(u'')#Lista en JSON compuesta de valores tipo BannedChampions
    gameId=models.BigIntegerField(u'Id del Partido')
    gameLength=models.BigIntegerField(u'Cuantos Segundos lleva durando')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameQueueConfigId=models.BigIntegerField(u'Tipo de partida(RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)')
    gameStartTime=models.BigIntegerField(u'Hora de inicio en milisegundos')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    mapId=models.BigIntegerField(u'Id del mapa')
    observers=#TODO#Observer
    participants=models.TextField(u'')#Lista en JSON compuesta de valores tipo CurrentGameParicipant
    platformId=models.CharField(u'Id de la plataforma en la que esta siendo jugado')

class CurrentGameParticipant(models.Model):  #Informacion de un jugador en una partida en especifico
    bot=models.BooleanField(u'Es un bot')
    championId=models.BigIntegerField(u'Id del jugador')
    masteries=models.TextField(u'')#Lista en JSON compuesta de valores tipo Mastery
    profileIconId=models.BigIntegerField(u'Id del icono de invocador que esta usando')
    runes=models.TextField(u'')#Lista en JSON compuesta de valores tipo Rune
    spell1Id=models.BigIntegerField(u'Id del Summoner Spell 1')
    spell2Id=models.BigIntegerField(u'Id del Summoner Spell 2')
    summonerId=models.BigIntegerField(u'Id del jugador')
    summonerName=models.CharField(u'Nombre publico del jugador')
    teamId=models.BigIntegerField(u'Id del equipo en el participa')

class Event(models.Model):  #Eventos que suceden a lo largo de la partida
    ascendedType=models.CharField(u'') # The ascended type of the event. Only present if relevant. Note that CLEAR_ASCENDED refers to when a participants kills the ascended player. (Legal values: CHAMPION_ASCENDED, CLEAR_ASCENDED, MINION_ASCENDED)
    assistingParticipantIds=models.TextField(u'')#Lista en JSON compuesta de valores tipo int The assisting participant IDs of the event. Only present if relevant.
    buildingType=models.CharField(u'') # The building type of the event. Only present if relevant. (Legal values: INHIBITOR_BUILDING, TOWER_BUILDING)
    creatorId=models.IntegerField(u'') # The creator ID of the event. Only present if relevant.
    eventType=models.CharField(u'') # Event type. (Legal values: ASCENDED_EVENT, BUILDING_KILL, CAPTURE_POINT, CHAMPION_KILL, ELITE_MONSTER_KILL, ITEM_DESTROYED, ITEM_PURCHASED, ITEM_SOLD, ITEM_UNDO, PORO_KING_SUMMON, SKILL_LEVEL_UP, WARD_KILL, WARD_PLACED)
    itemAfter=models.IntegerField(u'') # The ending item ID of the event. Only present if relevant.
    itemBefore=models.IntegerField(u'') # The starting item ID of the event. Only present if relevant.
    itemId=models.IntegerField(u'') # The item ID of the event. Only present if relevant.
    killerId=models.IntegerField(u'') # The killer ID of the event. Only present if relevant. Killer ID 0 indicates a minion.
    laneType=models.CharField(u'') # The lane type of the event. Only present if relevant. (Legal values: BOT_LANE, MID_LANE, TOP_LANE)
    levelUpType=models.CharField(u'') # The level up type of the event. Only present if relevant. (Legal values: EVOLVE, NORMAL)
    monsterType=models.CharField(u'') # The monster type of the event. Only present if relevant. (Legal values: BARON_NASHOR, BLUE_GOLEM, DRAGON, RED_LIZARD, VILEMAW)
    participantId=models.IntegerField(u'') # The participant ID of the event. Only present if relevant.
    pointCaptured=models.CharField(u'') # The point captured in the event. Only present if relevant. (Legal values: POINT_A, POINT_B, POINT_C, POINT_D, POINT_E)
    position=#TODO#Position # The position of the event. Only present if relevant.
    skillSlot=models.IntegerField(u'') # The skill slot of the event. Only present if relevant.
    teamId=models.IntegerField(u'') # The team ID of the event. Only present if relevant.
    timestamp=models.BigIntegerField(u'') # Represents how many milliseconds into the game the event occurred.
    towerType=models.CharField(u'') # The tower type of the event. Only present if relevant. (Legal values: BASE_TURRET, FOUNTAIN_TURRET, INNER_TURRET, NEXUS_TURRET, OUTER_TURRET, UNDEFINED_TURRET)
    victimId=models.IntegerField(u'') # The victim ID of the event. Only present if relevant.
    wardType=models.CharField(u'') # The ward type of the event. Only present if relevant. (Legal values: SIGHT_WARD, TEEMO_MUSHROOM, UNDEFINED, VISION_WARD, YELLOW_TRINKET, YELLOW_TRINKET_UPGRADE)

class FeaturedGames(models.Model):  #Juegos destacados
    clientRefreshInterval=models.BigIntegerField(u'Tiempo de espera antes de actualizar los juegos importantes')
    gameList=models.TextField(u'')#Lista en JSON compuesta de valores tipo FeaturedGameInfo

class FeaturedGamesInfo(models.Model):  #Datos de los juegos destacados
    bannedChampions=models.TextField(u'')#Lista en JSON compuesta de valores tipo BannedChampions
    gameId=models.BigIntegerField(u'Id del Partido')
    gameLength=models.BigIntegerField(u'Cuantos Segundos lleva durando')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameQueueConfigId=models.BigIntegerField(u'Tipo de partida(RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)')
    gameStartTime=models.BigIntegerField(u'Hora de inicio en milisegundos')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    mapId=models.BigIntegerField(u'Id del mapa')
    observers=models.CharField(Observer)
    participants=models.TextField(u'')#Lista en JSON compuesta de valores tipo CurrentGameParicipant
    platformId=models.CharField(u'Id de la plataforma en la que esta siendo jugado')


class Frame(models.Model):  #Datos sobre cada Frame
    events=models.TextField(u'')#Lista en JSON compuesta de valores tipo Event # List of events for this frame.
    participantFrames=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, ParticipantFrame # Map of each participant ID to the participant's information for the frame.
    timestamp=models.BigIntegerField(u'') # Represents how many milliseconds into the game the frame occurred.

class GameDto(models.Model):  #Informacion de los juegos recientes de un jugador especifico
    championId=models.IntegerField(u'Id del Pj usado')
    createDate=models.BigIntegerField(u'Fecha en la que se grabo los datos del final del partido')
    fellowPlayers=models.TextField(u'')#Lista en JSON compuesta de valores tipo PlayerDto
    gameId=models.models.BigIntegerField(u'Id de la partida')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    invalid=models.BooleanField(u'Invalid flag(Supongo que es derrota evitada)')
    ipEarned=models.IntegerField(u'IP ganado')
    level=models.IntegerField(u'Nivel en el que termino')
    mapId=models.IntegerField(u'Id del mapa')
    spell1=models.IntegerField(u'Id del Summoner Spell 1')
    spell2=models.IntegerField(u'Id del Summoner Spell 2')
    stats=#TODO#RawStatsDto
    subType=models.CharField(u'SubTipo de partida(NONE, NORMAL, BOT, RANKED_SOLO_5x5, RANKED_PREMADE_3x3, RANKED_PREMADE_5x5, ODIN_UNRANKED, RANKED_TEAM_3x3, RANKED_TEAM_5x5, NORMAL_3x3, BOT_3x3, CAP_5x5, ARAM_UNRANKED_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF, URF_BOT, NIGHTMARE_BOT, ASCENSION, HEXAKILL, KING_PORO, COUNTER_PICK, BILGEWATER)'),
    teamId=models.IntegerField(u'Id del lado en el que jugaba (100=Blue, 200=Purple)')

class GoldDto(models.Model):  #Datos sobre el manejo del oro durante la partida
    base=models.IntegerField(u'')
    purchasable=models.BooleanField(u'')
    sell=models.IntegerField(u'')
    total=models.IntegerField(u'')

class GroupDto(models.Model):  #Datos sobre los grupos de items
    MaxGroupOwnable=models.CharField(u'')
    key=models.CharField(u'')

class ImageDto(models.Model):  #Imagenes y sus datos
    full=models.CharField(u'')
    group=models.CharField(u'')
    h=models.IntegerField(u'')
    sprite=models.CharField(u'')
    w=models.IntegerField(u'')
    x=models.IntegerField(u'')
    y=models.IntegerField(u'')

class Incident(models.Model):  #TODO Informacion sobre el servidor
    active=models.BooleanField(u'')
    created_at=models.CharField(u'')
    exId=models.BigIntegerField(u'')
    updates=models.TextField(u'')#Lista en JSON compuesta de valores tipo Message

class InfoDto(models.Model):  #INFO basica de los campeones
    attack=models.IntegerField(u'Ataque segun Riot')
    defense=models.IntegerField(u'Defensa segun Riot')
    difficulty=models.IntegerField(u'Dificultad segun Riot')
    magic=models.IntegerField(u'Poder magico segun Riot')

class ItemDto(models.Model):  #Informacion registrada sobre cada item
    colloq=models.CharField(u'')
    consumeOnFull=models.BooleanField(u'')
    consumed=models.BooleanField(u'')
    depth=models.IntegerField(u'')
    description=models.CharField(u'')
    effect=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, string
    exFrom=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    gold=#TODO#GoldDto #Data Dragon includes the gold field for basic data, which is shared by both rune and item. However, only items have a gold field on them, representing their gold cost in the store. Since runes are not sold in the store, they have no gold cost.
    group=models.CharField(u'')
    hideFromAll=models.BooleanField(u'')
    exId=models.IntegerField(u'')
    image=#TODO#ImageDto
    inStore=models.BooleanField(u'')
    into=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    maps=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, boolean
    name=models.CharField(u'')
    plaintext=models.CharField(u'')
    requiredChampion=models.CharField(u'')
    rune=#TODO#MetaDataDto
    sanitizedDescription=models.CharField(u'')
    specialRecipe=models.IntegerField(u'')
    stacks=models.IntegerField(u'')
    stats=#TODO#BasicDataStatsDto
    tags=models.TextField(u'')#Lista en JSON compuesta de valores tipo string

class ItemTreeDto(models.Model):  #Informacion de cada arbol de items
    header=models.CharField(u'')
    tags=models.TextField(u'')#Lista en JSON compuesta de valores tipo string

class LanguageStringsDto(models.Model):  #Informacion de los strings de cada idioma
    data=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, string
    exType=models.CharField(u'')
    version=models.CharField(u'')

class LeagueDto(models.Model):  #INFO de la liga
    entries=models.TextField(u'')#Lista en JSON compuesta de valores tipo LeagueEntryDto
    name=models.CharField(u'Nombre expresado del jugador en esta liga')
    participantId=models.CharField(u'Id del perteneciente a esta liga (Sea un team o un jugador)')
    queue=models.CharField(u'Tipo de juego(RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)')
    tier=models.CharField(u'Liga (CHALLENGER, MASTER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE)')

class LeagueEntryDto(models.Model):  #Informacion sobre los integrantes de esta liga
    division=models.CharField(u'Division en la que esta')
    isFreshBlood=models.BooleanField(u'Especifica si es nuevo en la liga')
    isHotStreak=models.BooleanField(u'Especifica si está en racha')
    isInactive=models.BooleanField(u'Especifica si está inactivo')
    isVeteran=models.BooleanField(u'Especifica si es un veterano en la liga')
    leaguePoints=models.IntegerField(u'Puntos en la liga')
    losses=models.IntegerField(u'Derrotas')
    miniSeries=#TODO#MiniSeriesDto
    playerOrTeamId=models.CharField(u'Id del jugador o del team')
    playerOrTeamName=models.CharField(u'Nombre del jugador o del team')
    wins=models.IntegerField(u'Victorias')

class LevelTipDto(models.Model):  #Contiene la informacion de qué gana un campeon al levear
    effect=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    label=models.TextField(u'')#Lista en JSON compuesta de valores tipo string

class MapDataDto(models.Model):  #Informacion del mapa
    data=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, MapDetailsDto
    exType=models.CharField(u'')
    version=models.CharField(u'')

class MapDetailsDto(models.Model): #Detalles del mapa en el que se esta jugando
    image=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: ImageDto
    mapId=models.BigIntegerField(u'')
    mapName=models.CharField(u'')
    unpurchasableItemList=models.TextField(u'')#Lista en JSON compuesta de valores tipo long

class Mastery(models.Model):  #Datos individuales de cada maestria activa
    masteryId=models.BigIntegerField(u'') # Mastery ID
    rank=models.BigIntegerField(u'') # Mastery rank

class MasteryDto(models.Model):#Informacion de cada maestria
    exId=models.IntegerField(u'') # Mastery ID. For static information correlating to masteries, please refer to the LoL Static Data API.
    rank=models.IntegerField(u'') # Mastery rank (i.e., the number of points put into this mastery).

class MasteryListDto(models.Model):  #Conjunto de maestrias utilizadas
    datamodels.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, MasteryDto
    tree#TODO#MasteryTreeDto
    exType=models.CharField(u'')
    version=models.CharField(u'')

class MasteryPageDto(models.Model):  #Datos de las paginas de maestrias configuradas
    current=models.BooleanField(u'') # Indicates if the mastery page is the current mastery page.
    exId=models.BigIntegerField(u'') # Mastery page ID.
    masteries=models.TextField(u'')#Lista en JSON compuesta de valores tipo MasteryDto Collection of masteries associated with the mastery page.
    name=models.CharField(u'') # Mastery page name.

class MasteryPagesDto(models.Model):  
    pages=#TODO#Set#MasteryPageDto # Collection of mastery pages associated with the summoner.
    summonerId=models.BigIntegerField(u'') # Summoner ID.


class MasteryTreeDto(models.Model):
    Defense=models.TextField(u'')#Lista en JSON compuesta de valores tipo MasteryTreeListDto
    Offense=models.TextField(u'')#Lista en JSON compuesta de valores tipo MasteryTreeListDto
    Utility=models.TextField(u'')#Lista en JSON compuesta de valores tipo MasteryTreeListDto

class MasteryTreeItemDto(models.Model):
    masteryId=models.IntegerField(u'')
    prereq=models.CharField(u'')

class MasteryTreeListDto(models.Model):
    masteryTreeItems=models.TextField(u'')#Lista en JSON compuesta de valores tipo MasteryTreeItemDto


class MatchDetail(models.Model):
    mapId=models.IntegerField(u'') # Match map ID
    matchCreation=models.BigIntegerField(u'') # Match creation time. Designates when the team select lobby is created and/or the match is made through match making, not when the game actually starts.
    matchDuration=models.BigIntegerField(u'') # Match duration
    matchId=models.BigIntegerField(u'') # ID of the match
    matchMode=models.CharField(u'') # Match mode (Legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)
    matchType=models.CharField(u'') # Match type (Legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
    matchVersion=models.CharField(u'') # Match version
    participantIdentities=models.TextField(u'')#Lista en JSON compuesta de valores tipo ParticipantIdentity Participant identity information
    participants=models.TextField(u'')#Lista en JSON compuesta de valores tipo Participant Participant information
    platformId=models.CharField(u'') # Platform ID of the match
    queueType=models.CharField(u'') # Match queue type (Legal values: CUSTOM, NORMAL_5x5_BLIND, RANKED_SOLO_5x5, RANKED_PREMADE_5x5, BOT_5x5, NORMAL_3x3, RANKED_PREMADE_3x3, NORMAL_5x5_DRAFT, ODIN_5x5_BLIND, ODIN_5x5_DRAFT, BOT_ODIN_5x5, BOT_5x5_INTRO, BOT_5x5_BEGINNER, BOT_5x5_INTERMEDIATE, RANKED_TEAM_3x3, RANKED_TEAM_5x5, BOT_TT_3x3, GROUP_FINDER_5x5, ARAM_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF_5x5, ONEFORALL_MIRRORMODE_5x5, BOT_URF_5x5, NIGHTMARE_BOT_5x5_RANK1, NIGHTMARE_BOT_5x5_RANK2, NIGHTMARE_BOT_5x5_RANK5, ASCENSION_5x5, HEXAKILL, BILGEWATER_ARAM_5x5, KING_PORO_5x5, COUNTER_PICK, BILGEWATER_5x5)
    region=models.CharField(u'') # Region where the match was played
    season=models.CharField(u'') # Season match was played (Legal values: PRESEASON3, SEASON3, PRESEASON2014, SEASON2014, PRESEASON2015, SEASON2015)
    teams=models.TextField(u'')#Lista en JSON compuesta de valores tipo Team Team information
    timeline=#TODO#Timeline    # Match timeline data (not included by default)

class MatchHistorySummaryDto(models.Model):
    assists=models.IntegerField(u'')
    date=models.BigIntegerField(u'') # Date that match was completed specified as epoch milliseconds.
    deaths=models.IntegerField(u'')
    gameId=models.BigIntegerField(u'')
    gameMode=models.CharField(u'')
    invalid=models.BooleanField(u'')
    kills=models.IntegerField(u'')
    mapId=models.IntegerField(u'')
    opposingTeamKills=models.IntegerField(u'')
    opposingTeamName=models.CharField(u'')
    win=models.BooleanField(u'')

class MatchList(models.Model):
    endIndex=models.IntegerField(u'')
    matches=models.TextField(u'')#Lista en JSON compuesta de valores tipo MatchReference
    startIndex=models.IntegerField(u'')
    totalGames=models.IntegerField(u'')

class MatchReference(models.Model):
    champion=models.BigIntegerField(u'')
    lane=models.CharField(u'') # Legal values: MID, MIDDLE, TOP, JUNGLE, BOT, BOTTOM
    matchId=models.BigIntegerField(u'')
    platformId=models.CharField(u'')
    queue=models.CharField(u'') # Legal values: RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5
    role=models.CharField(u'') # Legal values: DUO, NONE, SOLO, DUO_CARRY, DUO_SUPPORT
    season=models.CharField(u'') # Legal values: PRESEASON3, SEASON3, PRESEASON2014, SEASON2014, PRESEASON2015, SEASON2015
    timestamp=models.BigIntegerField(u'')

class MatchSummary(models.Model):
    mapId=models.IntegerField(u'') # Match map ID
    matchCreation=models.BigIntegerField(u'') # Match creation time. Designates when the team select lobby is created and/or the match is made through match making, not when the game actually starts.
    matchDuration=models.BigIntegerField(u'') # Match duration
    matchId=models.BigIntegerField(u'') # ID of the match
    matchMode=models.CharField(u'') # Match mode (Legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)
    matchType=models.CharField(u'') # Match type (Legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
    matchVersion=models.CharField(u'') # Match version
    participantIdentities=models.TextField(u'')#Lista en JSON compuesta de valores tipo ParticipantIdentity # Participant identity information
    participants=models.TextField(u'')#Lista en JSON compuesta de valores tipo Participant # Participant information
    platformId=models.CharField(u'') # Platform ID of the match
    queueType=models.CharField(u'') # Match queue type (Legal values: CUSTOM, NORMAL_5x5_BLIND, RANKED_SOLO_5x5, RANKED_PREMADE_5x5, BOT_5x5, NORMAL_3x3, RANKED_PREMADE_3x3, NORMAL_5x5_DRAFT, ODIN_5x5_BLIND, ODIN_5x5_DRAFT, BOT_ODIN_5x5, BOT_5x5_INTRO, BOT_5x5_BEGINNER, BOT_5x5_INTERMEDIATE, RANKED_TEAM_3x3, RANKED_TEAM_5x5, BOT_TT_3x3, GROUP_FINDER_5x5, ARAM_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF_5x5, ONEFORALL_MIRRORMODE_5x5, BOT_URF_5x5, NIGHTMARE_BOT_5x5_RANK1, NIGHTMARE_BOT_5x5_RANK2, NIGHTMARE_BOT_5x5_RANK5, ASCENSION_5x5, HEXAKILL, BILGEWATER_ARAM_5x5, KING_PORO_5x5, COUNTER_PICK, BILGEWATER_5x5)
    region=models.CharField(u'') # Region where the match was played
    season=models.CharField(u'') # Season match was played (Legal values: PRESEASON3, SEASON3, PRESEASON2014, SEASON2014, PRESEASON2015, SEASON2015)

class Message(models.Model):
    author=models.CharField(u'')
    content=models.CharField(u'')
    created_at=models.CharField(u'')
    exId=models.BigIntegerField(u'')
    severity=models.CharField(u'') # Legal values: Info, Alert, Error
    translations=models.TextField(u'')#Lista en JSON compuesta de valores tipo Translation
    updated_at=models.CharField(u'')

class MetaDataDto(models.Model):
    isRune=models.BooleanField(u'')
    tier=models.CharField(u'')
    exType=models.CharField(u'')

class MiniSeriesDto(models.Model):
#Informacion de las miniseries
    losses=models.IntegerField(u'Numero de partidas que perdió en promo')
    progress=models.CharField(u'Muestra la promocion actual (W=Victoria L=Derrota N=Falta Jugar)')
    target=models.IntegerField(u'Numero de victorias necesarias para promocionar')
    wins=models.IntegerField(u'Numero de partidas que ganó en promo')

class Observer(models.Model):
#Espectador
    encryptionKey=models.CharField(u'Key used to decrypt the spectator grid game data for playback')

class Participant(models.Model):
    championId=models.IntegerField(u'') # Champion ID
    highestAchievedSeasonTier=models.CharField(u'') # Highest ranked tier achieved for the previous season, if any, otherwise null. Used to display border in game loading screen. (Legal values: CHALLENGER, MASTER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, UNRANKED)
    masteries=models.TextField(u'')#Lista en JSON compuesta de valores tipo Mastery List of mastery information
    participantId=models.IntegerField(u'') # Participant ID
    runes=models.TextField(u'')#Lista en JSON compuesta de valores tipo Rune List of rune information
    spell1Id=models.IntegerField(u'') # First summoner spell ID
    spell2Id=models.IntegerField(u'') # Second summoner spell ID
    stats=#TODO#ParticipantStats# Participant statistics
    teamId=models.IntegerField(u'') # Team ID
    timeline=#TODO#ParticipantTimeline # Timeline data. Delta fields refer to values for the specified period (e.g., the gold per minute over the first 10 minutes of the game versus the second 20 minutes of the game. Diffs fields refer to the deltas versus the calculated lane opponent(s).

class ParticipantFrame(models.Model):
    currentGold=models.IntegerField(u'') # Participant's current gold
    dominionScore=models.IntegerField(u'') # Dominion score of the participant
    jungleMinionsKilled=models.IntegerField(u'') # Number of jungle minions killed by participant
    level=models.IntegerField(u'') # Participant's current level
    minionsKilled=models.IntegerField(u'') # Number of minions killed by participant
    participantId=models.IntegerField(u'') # Participant ID
    position=#TODO#Position # Participant's position
    teamScore=models.IntegerField(u'') # Team score of the participant
    totalGold=models.IntegerField(u'') # Participant's total gold
    xp=models.IntegerField(u'') # Experience earned by participant

class ParticipantIdentity(models.Model):
    participantId=models.IntegerField(u'') # Participant ID
    player Player#TODO # Player information

class ParticipantStats(models.Model):
    assists=models.BigIntegerField(u'') # Number of assists
    champLevel=models.BigIntegerField(u'') # Champion level achieved
    combatPlayerScore=models.BigIntegerField(u'') # If game was a dominion game, player's combat score, otherwise 0
    deaths=models.BigIntegerField(u'') # Number of deaths
    doubleKills=models.BigIntegerField(u'') # Number of double kills
    firstBloodAssist=models.BooleanField(u'') # Flag indicating if participant got an assist on first blood
    firstBloodKill=models.BooleanField(u'') # Flag indicating if participant got first blood
    firstInhibitorAssist=models.BooleanField(u'') # Flag indicating if participant got an assist on the first inhibitor
    firstInhibitorKill=models.BooleanField(u'') # Flag indicating if participant destroyed the first inhibitor
    firstTowerAssist=models.BooleanField(u'') # Flag indicating if participant got an assist on the first tower
    firstTowerKill=models.BooleanField(u'') # Flag indicating if participant destroyed the first tower
    goldEarned=models.BigIntegerField(u'') # Gold earned
    goldSpent=models.BigIntegerField(u'') # Gold spent
    inhibitorKills=models.BigIntegerField(u'') # Number of inhibitor kills
    item0=models.BigIntegerField(u'') # First item ID
    item1=models.BigIntegerField(u'') # Second item ID
    item2=models.BigIntegerField(u'') # Third item ID
    item3=models.BigIntegerField(u'') # Fourth item ID
    item4=models.BigIntegerField(u'') # Fifth item ID
    item5=models.BigIntegerField(u'') # Sixth item ID
    item6=models.BigIntegerField(u'') # Seventh item ID
    killingSprees=models.BigIntegerField(u'') # Number of killing sprees
    kills=models.BigIntegerField(u'') # Number of kills
    largestCriticalStrike=models.BigIntegerField(u'') # Largest critical strike
    largestKillingSpree=models.BigIntegerField(u'') # Largest killing spree
    largestMultiKill=models.BigIntegerField(u'') # Largest multi kill
    magicDamageDealt=models.BigIntegerField(u'') # Magical damage dealt
    magicDamageDealtToChampions=models.BigIntegerField(u'') # Magical damage dealt to champions
    magicDamageTaken=models.BigIntegerField(u'') # Magic damage taken
    minionsKilled=models.BigIntegerField(u'') # Minions killed
    neutralMinionsKilled=models.BigIntegerField(u'') # Neutral minions killed
    neutralMinionsKilledEnemyJungle=models.BigIntegerField(u'') # Neutral jungle minions killed in the enemy team's jungle
    neutralMinionsKilledTeamJungle=models.BigIntegerField(u'') # Neutral jungle minions killed in your team's jungle
    nodeCapture=models.BigIntegerField(u'') # If game was a dominion game, number of node captures
    nodeCaptureAssist=models.BigIntegerField(u'') # If game was a dominion game, number of node capture assists
    nodeNeutralize=models.BigIntegerField(u'') # If game was a dominion game, number of node neutralizations
    nodeNeutralizeAssist=models.BigIntegerField(u'') # If game was a dominion game, number of node neutralization assists
    objectivePlayerScore=models.BigIntegerField(u'') # If game was a dominion game, player's objectives score, otherwise 0
    pentaKills=models.BigIntegerField(u'') # Number of penta kills
    physicalDamageDealt=models.BigIntegerField(u'') # Physical damage dealt
    physicalDamageDealtToChampions=models.BigIntegerField(u'') # Physical damage dealt to champions
    physicalDamageTaken=models.BigIntegerField(u'') # Physical damage taken
    quadraKills=models.BigIntegerField(u'') # Number of quadra kills
    sightWardsBoughtInGame=models.BigIntegerField(u'') # Sight wards purchased
    teamObjective=models.BigIntegerField(u'') # If game was a dominion game, number of completed team objectives (i.e., quests)
    totalDamageDealt=models.BigIntegerField(u'') # Total damage dealt
    totalDamageDealtToChampions=models.BigIntegerField(u'') # Total damage dealt to champions
    totalDamageTaken=models.BigIntegerField(u'') # Total damage taken
    totalHeal=models.BigIntegerField(u'') # Total heal amount
    totalPlayerScore=models.BigIntegerField(u'') # If game was a dominion game, player's total score, otherwise 0
    totalScoreRank=models.BigIntegerField(u'') # If game was a dominion game, team rank of the player's total score (e.g., 1-5)
    totalTimeCrowdControlDealt=models.BigIntegerField(u'') # Total dealt crowd control time
    totalUnitsHealed=models.BigIntegerField(u'') # Total units healed
    towerKills=models.BigIntegerField(u'') # Number of tower kills
    tripleKills=models.BigIntegerField(u'') # Number of triple kills
    trueDamageDealt=models.BigIntegerField(u'') # True damage dealt
    trueDamageDealtToChampions=models.BigIntegerField(u'') # True damage dealt to champions
    trueDamageTaken=models.BigIntegerField(u'') # True damage taken
    unrealKills=models.BigIntegerField(u'') # Number of unreal kills
    visionWardsBoughtInGame=models.BigIntegerField(u'') # Vision wards purchased
    wardsKilled=models.BigIntegerField(u'') # Number of wards killed
    wardsPlaced=models.BigIntegerField(u'') # Number of wards placed
    winner=models.BooleanField(u'') # Flag indicating whether or not the participant won

class ParticipantTimeline(models.Model):
    ancientGolemAssistsPerMinCounts=#TODO#ParticipantTimelineData     # Ancient golem assists per minute timeline counts
    ancientGolemKillsPerMinCounts=#TODO#ParticipantTimelineData     # Ancient golem kills per minute timeline counts
    assistedLaneDeathsPerMinDeltas=#TODO#ParticipantTimelineData     # Assisted lane deaths per minute timeline data
    assistedLaneKillsPerMinDeltas=#TODO#ParticipantTimelineData     # Assisted lane kills per minute timeline data
    baronAssistsPerMinCounts=#TODO#ParticipantTimelineData     # Baron assists per minute timeline counts
    baronKillsPerMinCounts=#TODO#ParticipantTimelineData     # Baron kills per minute timeline counts
    creepsPerMinDeltas=#TODO#ParticipantTimelineData     # Creeps per minute timeline data
    csDiffPerMinDeltas=#TODO#ParticipantTimelineData     # Creep score difference per minute timeline data
    damageTakenDiffPerMinDeltas=#TODO#ParticipantTimelineData     # Damage taken difference per minute timeline data
    damageTakenPerMinDeltas=#TODO#ParticipantTimelineData     # Damage taken per minute timeline data
    dragonAssistsPerMinCounts=#TODO#ParticipantTimelineData     # Dragon assists per minute timeline counts
    dragonKillsPerMinCounts=#TODO#ParticipantTimelineData     # Dragon kills per minute timeline counts
    elderLizardAssistsPerMinCounts=#TODO#ParticipantTimelineData     # Elder lizard assists per minute timeline counts
    elderLizardKillsPerMinCounts=#TODO#ParticipantTimelineData     # Elder lizard kills per minute timeline counts
    goldPerMinDeltas=#TODO#ParticipantTimelineData     # Gold per minute timeline data
    inhibitorAssistsPerMinCounts=#TODO#ParticipantTimelineData     # Inhibitor assists per minute timeline counts
    inhibitorKillsPerMinCounts=#TODO#ParticipantTimelineData     # Inhibitor kills per minute timeline counts
    lane=models.CharField(u'') # Participant's lane (Legal values: MID, MIDDLE, TOP, JUNGLE, BOT, BOTTOM)
    role=models.CharField(u'') # Participant's role (Legal values: DUO, NONE, SOLO, DUO_CARRY, DUO_SUPPORT)
    towerAssistsPerMinCounts=#TODO#ParticipantTimelineData     # Tower assists per minute timeline counts
    towerKillsPerMinCounts=#TODO#ParticipantTimelineData     # Tower kills per minute timeline counts
    towerKillsPerMinDeltas=#TODO#ParticipantTimelineData     # Tower kills per minute timeline data
    vilemawAssistsPerMinCounts=#TODO#ParticipantTimelineData     # Vilemaw assists per minute timeline counts
    vilemawKillsPerMinCounts=#TODO#ParticipantTimelineData     # Vilemaw kills per minute timeline counts
    wardsPerMinDeltas=#TODO#ParticipantTimelineData     # Wards placed per minute timeline data
    xpDiffPerMinDeltas=#TODO#ParticipantTimelineData     # Experience difference per minute timeline data
    xpPerMinDeltas=#TODO#ParticipantTimelineData     # Experience per minute timeline data

class ParticipantTimelineData(models.Model):
    tenToTwenty=models.FloatField(u'') # Value per minute from 10 min to 20 min
    thirtyToEnd=models.FloatField(u'') # Value per minute from 30 min to the end of the game
    twentyToThirty=models.FloatField(u'') # Value per minute from 20 min to 30 min
    zeroToTen=models.FloatField(u'') # Value per minute from the beginning of the game to 10 min

class PassiveDto(models.Model):
#Datos de la pasiva del campeon
    description=models.CharField(u'Descripcion')
    image=models.TextField(u'')#Lista en JSON compuesta de valores tipo ImageDto
    name=models.CharField(u'Nombre de la pasiva')
    sanitizedDescription=models.CharField(u'Descripcion concreta')

class Player(models.Model):
    matchHistoryUri=models.CharField(u'') # Match history URI
    profileIcon=models.IntegerField(u'') # Profile icon ID
    summonerId=models.BigIntegerField(u'') # Summoner ID
    summonerName=models.CharField(u'') # Summoner name

class PlayerDto(models.Model):
#INFO de los pj que usa y su team
    championId=models.IntegerField("Id del campeon asociado al jugador")
    summonerId=models.BigIntegerField(u'Id del invocador')
    teamId=models.IntegerField(u'Id al equipo asociado al jugador')

class PlayerHistory(models.Model):
    matches=models.TextField(u'')#Lista en JSON compuesta de valores tipo MatchSummary # List of matches for the player


class PlayerStatsSummaryDto(models.Model):
    aggregatedStats=#TODO#AggregatedStatsDto# Aggregated stats.
    losses=models.IntegerField(u'') # Number of losses for this queue type. Returned for ranked queue types only.
    modifyDate=models.BigIntegerField(u'') # Date stats were last modified specified as epoch milliseconds.
    playerStatSummaryType=models.CharField(u'') # Player stats summary type. (Legal values: AramUnranked5x5, Ascension, CAP5x5, CoopVsAI, CoopVsAI3x3, CounterPick, FirstBlood1x1, FirstBlood2x2, Hexakill, KingPoro, NightmareBot, OdinUnranked, OneForAll5x5, RankedPremade3x3, RankedPremade5x5, RankedSolo5x5, RankedTeam3x3, RankedTeam5x5, SummonersRift6x6, Unranked, Unranked3x3, URF, URFBots, Bilgewater)
    wins=models.IntegerField(u'') # Number of wins for this queue type.

class PlayerStatsSummaryListDto(models.Model):
    playerStatSummaries=models.TextField(u'')#Lista en JSON compuesta de valores tipo PlayerStatsSummaryDto Collection of player stats summaries associated with the summoner.
    summonerId=models.BigIntegerField(u'') # Summoner ID


class Position(models.Model):
    x=models.IntegerField(u'')
    y=models.IntegerField(u'')

class RankedStatsDto(models.Model):
    champions=models.TextField(u'')#Lista en JSON compuesta de valores tipo ChampionStatsDto # Collection of aggregated stats summarized by champion
    modifyDate=models.BigIntegerField(u'') # Date stats were last modified specified as epoch milliseconds.
    summonerId=models.BigIntegerField(u'') # Summoner ID.

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

class RealmDto(models.Model):
    cdn=models.CharField(u'') # The base CDN url
    css=models.CharField(u'') # Latest changed version of Dragon Magic's css file
    dd=models.CharField(u'') # Latest changed version of Dragon Magic
    l=models.CharField(u'') # Default language for this realm
    lg=models.CharField(u'') # Legacy script mode for IE6 or older
    n=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, string # Latest changed version for each data type listed.
    profileiconmax=models.IntegerField(u'') # Special behavior number identifying the largest profileicon id that can be used under 500. Any profileicon that is requested between this number and 500 should be mapped to 0.
    store=models.CharField(u'') # Additional api data drawn from other sources that may be related to data dragon functionality.
    v=models.CharField(u'') # Current version of this file for this realm. 

class RecentGamesDto(models.Model):
#Juegos recientes de X jugador
    games=#TODO#SET#GameDto
    summonerId=models.BigIntegerField(u'Id del jugador')

class RecommendedDto(models.Model):
#Data de las recomendaciones para los campeones
    blocks=models.TextField(u'')#Lista en JSON compuesta de valores tipo BlockDto
    champion=models.CharField(u'Nombre del Campeon')
    exMap=models.CharField(u'Mapa')
    mode=models.CharField(u'Modo en el que se recomiendan(CLASSIC, ARAM, etc)')
    priority=models.BooleanField(u'Prioridad')
    title=models.CharField(u'Titulo de la Build')
    exType=models.CharField(u'Titulo del conjunto de items(iniciales, finales, etc)')

class RosterDto(models.Model):
    memberList=models.TextField(u'')#Lista en JSON compuesta de valores tipo TeamMemberInfoDto
    ownerId=models.BigIntegerField(u'')

class Rune(models.Model):
#Runas individuales
    runeId=models.BigIntegerField(u'Id de la runa')
    count=models.IntegerField(u'Cantidad de copias de esta runa')

class RuneDto(models.Model):
    colloq=models.CharField(u'')
    consumeOnFull=models.BooleanField(u'')
    consumed=models.BooleanField(u'')
    depth=models.IntegerField(u'')
    description=models.CharField(u'')
    exFrom=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    group=models.CharField(u'')
    hideFromAll=models.BooleanField(u'')
    exId=models.IntegerField(u'')
    image=#TODO#ImageDto
    inStore=models.BooleanField(u'')
    into=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    maps=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, boolean
    name=models.CharField(u'')
    plaintext=models.CharField(u'')
    requiredChampion=models.CharField(u'')
    rune=#TODO#MetaDataDto
    sanitizedDescription=models.CharField(u'')
    specialRecipe=models.IntegerField(u'')
    stacks=models.IntegerField(u'')
    stats=#TODO#BasicDataStatsDto
    tags=models.TextField(u'')#Lista en JSON compuesta de valores tipo string

class RuneListDto(models.Model):
    basic BasicDataDto
    data=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, RuneDto
    exType=models.CharField(u'')
    version=models.CharField(u'')

class RunePageDto(models.Model):
    current=models.BooleanField(u'') # Indicates if the page is the current page.
    exId=models.BigIntegerField(u'') # Rune page ID.
    name=models.CharField(u'') # Rune page name.
    slots=#TODO#SET#RuneSlotDto # Collection of rune slots associated with the rune page.

class RunePagesDto(models.Model):
    pages=#TODO#SET#RunePageDto # Collection of rune pages associated with the summoner.
    summonerId=models.BigIntegerField(u'') # Summoner ID.

class RuneSlotDto(models.Model):
    runeId=models.IntegerField(u'') # Rune ID associated with the rune slot. For static information correlating to rune IDs, please refer to the LoL Static Data API.
    runeSlotId=models.IntegerField(u'') # Rune slot ID.

class Service(models.Model):
    incidents=models.TextField(u'')#Lista en JSON compuesta de valores tipo Incident
    name=models.CharField(u'')
    slug=models.CharField(u'')
    status=models.CharField(u'') # Legal values: Online, Alert, Offline, Deploying

class Shard(models.Model):
    hostname=models.CharField(u'')
    locales=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    name=models.CharField(u'')
    region_tag=models.CharField(u'')
    slug=models.CharField(u'')


class ShardStatus(models.Model):
    hostname=models.CharField(u'')
    locales=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    name=models.CharField(u'')
    region_tag=models.CharField(u'')
    services=models.TextField(u'')#Lista en JSON compuesta de valores tipo Service
    slug=models.CharField(u'')

class SkinDto(models.Model):
#Data de los Skins
    exId=models.IntegerField(u'Id de la skin')
    name=models.CharField(u'Nombre de la skin')
    num=models.IntegerField(u'Numero de skin de este Pj(Default=0)')

class SpellVarsDto(models.Model):
#Data de los spells
    coeff=models.TextField(u'')#Lista en JSON compuesta de valores tipo double
    dyn=models.CharField(u'Si el spell tiene daño dinamico, especifica si el daño aumenta(+) o diminuye(-)')
    keyslink=models.CharField(u'Key del spell')
    link=models.CharField(u'Link del spell, donde se especifica si tiene un daño estatico o dinamico(que depende de otra variable)')
    ranksWith=models.CharField(u'Variable rara que solo tiene karma(value=KarmaMantra)')

class BasicDataStatsDto(models.Model):
    FlatArmorMod=models.FloatField(u'')
    FlatAttackSpeedMod=models.FloatField(u'')
    FlatBlockMod=models.FloatField(u'')
    FlatCritChanceMod=models.FloatField(u'')
    FlatCritDamageMod=models.FloatField(u'')
    FlatEXPBonus=models.FloatField(u'')
    FlatEnergyPoolMod=models.FloatField(u'')
    FlatEnergyRegenMod=models.FloatField(u'')
    FlatHPPoolMod=models.FloatField(u'')
    FlatHPRegenMod=models.FloatField(u'')
    FlatMPPoolMod=models.FloatField(u'')
    FlatMPRegenMod=models.FloatField(u'')
    FlatMagicDamageMod=models.FloatField(u'')
    FlatMovementSpeedMod=models.FloatField(u'')
    FlatPhysicalDamageMod=models.FloatField(u'')
    FlatSpellBlockMod=models.FloatField(u'')
    PercentArmorMod=models.FloatField(u'')
    PercentAttackSpeedMod=models.FloatField(u'')
    PercentBlockMod=models.FloatField(u'')
    PercentCritChanceMod=models.FloatField(u'')
    PercentCritDamageMod=models.FloatField(u'')
    PercentDodgeMod=models.FloatField(u'')
    PercentEXPBonus=models.FloatField(u'')
    PercentHPPoolMod=models.FloatField(u'')
    PercentHPRegenMod=models.FloatField(u'')
    PercentLifeStealMod=models.FloatField(u'')
    PercentMPPoolMod=models.FloatField(u'')
    PercentMPRegenMod=models.FloatField(u'')
    PercentMagicDamageMod=models.FloatField(u'')
    PercentMovementSpeedMod=models.FloatField(u'')
    PercentPhysicalDamageMod=models.FloatField(u'')
    PercentSpellBlockMod=models.FloatField(u'')
    PercentSpellVampMod=models.FloatField(u'')
    rFlatArmorModPerLevel=models.FloatField(u'')
    rFlatArmorPenetrationMod=models.FloatField(u'')
    rFlatArmorPenetrationModPerLevel=models.FloatField(u'')
    rFlatCritChanceModPerLevel=models.FloatField(u'')
    rFlatCritDamageModPerLevel=models.FloatField(u'')
    rFlatDodgeMod=models.FloatField(u'')
    rFlatDodgeModPerLevel=models.FloatField(u'')
    rFlatEnergyModPerLevel=models.FloatField(u'')
    rFlatEnergyRegenModPerLevel=models.FloatField(u'')
    rFlatGoldPer10Mod=models.FloatField(u'')
    rFlatHPModPerLevel=models.FloatField(u'')
    rFlatHPRegenModPerLevel=models.FloatField(u'')
    rFlatMPModPerLevel=models.FloatField(u'')
    rFlatMPRegenModPerLevel=models.FloatField(u'')
    rFlatMagicDamageModPerLevel=models.FloatField(u'')
    rFlatMagicPenetrationMod=models.FloatField(u'')
    rFlatMagicPenetrationModPerLevel=models.FloatField(u'')
    rFlatMovementSpeedModPerLevel=models.FloatField(u'')
    rFlatPhysicalDamageModPerLevel=models.FloatField(u'')
    rFlatSpellBlockModPerLevel=models.FloatField(u'')
    rFlatTimeDeadMod=models.FloatField(u'')
    rFlatTimeDeadModPerLevel=models.FloatField(u'')
    rPercentArmorPenetrationMod=models.FloatField(u'')
    rPercentArmorPenetrationModPerLevel=models.FloatField(u'')
    rPercentAttackSpeedModPerLevel=models.FloatField(u'')
    rPercentCooldownMod=models.FloatField(u'')
    rPercentCooldownModPerLevel=models.FloatField(u'')
    rPercentMagicPenetrationMod=models.FloatField(u'')
    rPercentMagicPenetrationModPerLevel=models.FloatField(u'')
    rPercentMovementSpeedModPerLevel=models.FloatField(u'')
    rPercentTimeDeadMod=models.FloatField(u'')
    rPercentTimeDeadModPerLevel=models.FloatField(u'')

class SummonerDto(models.Model):
    exId=models.BigIntegerField(u'') # Summoner ID.
    name=models.CharField(u'') # Summoner name.
    profileIconId=models.IntegerField(u'') # ID of the summoner icon associated with the summoner.
    revisionDate=models.BigIntegerField(u'') # Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change
    summonerLevel=models.BigIntegerField(u'') # Summoner level associated with the summoner.

class SummonerSpellDto(models.Model):
    cooldown=models.TextField(u'')#Lista en JSON compuesta de valores tipo double
    cooldownBurn=models.CharField(u'')
    cost=models.TextField(u'')#Lista en JSON compuesta de valores tipo int
    costBurn=models.CharField(u'')
    costType=models.CharField(u'')
    description=models.CharField(u'')
    effect=models.TextField(u'')#Lista en JSON compuesta de valores tipo object # This field is a List of List of Double.
    effectBurn=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    exId=models.IntegerField(u'')
    image=#TODO#ImageDto
    key=models.CharField(u'')
    leveltip=#TODO#LevelTipDto
    maxrank=models.IntegerField(u'')
    modes=models.TextField(u'')#Lista en JSON compuesta de valores tipo string
    name=models.CharField(u'')
    exRange=#TODO#object #This field is either a List of Integer or the String 'self' for spells that target one's own champion.
    rangeBurn=models.CharField(u'')
    resource=models.CharField(u'')
    sanitizedDescription=models.CharField(u'')
    sanitizedTooltip=models.CharField(u'')
    summonerLevel=models.IntegerField(u'')
    tooltip=models.CharField(u'')
    exVars=models.TextField(u'')#Lista en JSON compuesta de valores tipo SpellVarsDto

class SummonerSpellListDto(models.Model):
    data=models.TextField(u'')#Map en JSON compuesta de valores de los siguientes tipos: string, SummonerSpellDto
    exType=models.CharField(u'')
    version=models.CharField(u'')

class Team(models.Model):
    bans=models.TextField(u'')#Lista en JSON compuesta de valores tipo BannedChampion If game was draft mode, contains banned champion data, otherwise null
    baronKills=models.IntegerField(u'') # Number of times the team killed baron
    dominionVictoryScore=models.BigIntegerField(u'') # If game was a dominion game, specifies the points the team had at game end, otherwise null
    dragonKills=models.IntegerField(u'') # Number of times the team killed dragon
    firstBaron=models.BooleanField(u'') # Flag indicating whether or not the team got the first baron kill
    firstBlood=models.BooleanField(u'') # Flag indicating whether or not the team got first blood
    firstDragon=models.BooleanField(u'') # Flag indicating whether or not the team got the first dragon kill
    firstInhibitor=models.BooleanField(u'') # Flag indicating whether or not the team destroyed the first inhibitor
    firstTower=models.BooleanField(u'') # Flag indicating whether or not the team destroyed the first tower
    inhibitorKills=models.IntegerField(u'') # Number of inhibitors the team destroyed
    teamId=models.IntegerField(u'') # Team ID
    towerKills=models.IntegerField(u'') # Number of towers the team destroyed
    vilemawKills=models.IntegerField(u'') # Number of times the team killed vilemaw
    winner=models.BooleanField(u'') # Flag indicating whether or not the team won

class TeamDto(models.Model):
    createDate=models.BigIntegerField(u'') # Date that team was created specified as epoch milliseconds.
    fullId=models.CharField(u'')
    lastGameDate=models.BigIntegerField(u'') # Date that last game played by team ended specified as epoch milliseconds.
    lastJoinDate=models.BigIntegerField(u'') # Date that last member joined specified as epoch milliseconds.
    lastJoinedRankedTeamQueueDate=models.BigIntegerField(u'') # Date that team last joined the ranked team queue specified as epoch milliseconds.
    matchHistory=models.TextField(u'')#Lista en JSON compuesta de valores tipo MatchHistorySummaryDto
    modifyDate=models.BigIntegerField(u'') # Date that team was last modified specified as epoch milliseconds.
    name=models.CharField(u'')
    roster=#TODO#RosterDto
    secondLastJoinDate=models.BigIntegerField(u'') # Date that second to last member joined specified as epoch milliseconds.
    status=models.CharField(u'')
    tag=models.CharField(u'')
    teamStatDetails=models.TextField(u'')#Lista en JSON compuesta de valores tipo TeamStatDetailDto
    thirdLastJoinDate=models.BigIntegerField(u'') # Date that third to last member joined specified as epoch milliseconds.

class TeamMemberInfoDto(models.Model):
    inviteDate=models.BigIntegerField(u'') # Date that team member was invited to team specified as epoch milliseconds.
    joinDate=models.BigIntegerField(u'') # Date that team member joined team specified as epoch milliseconds.
    playerId=models.BigIntegerField(u'')
    status=models.CharField(u'')

class TeamStatDetailDto(models.Model):
    averageGamesPlayed=models.IntegerField(u'')
    losses=models.IntegerField(u'')
    teamStatType=models.CharField(u'')
    wins=models.IntegerField(u'')


class Timeline(models.Model):
    frameInterval=models.BigIntegerField(u'') # Time between each returned frame in milliseconds.
    frames=models.TextField(u'')#Lista en JSON compuesta de valores tipo Frame List of timeline frames for the game.


class Translation(models.Model):
    content=models.CharField(u'')
    locale=models.CharField(u'')
    updated_at=models.CharField(u'')
