from django.db import models
#Las variables que estaban reservadas cambiaron su nombre por: "ex" + "NOMBREdeVARIABLE"
#Las variables son:   format=exFormat, type=exType, id=exId, range=exRange, vars=exVars, map=exMap

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
    bannedChampions=models.CharField(BannedChampions)
    gameId=models.BigIntegerField(u'Id del Partido')
    gameLength=models.BigIntegerField(u'Cuantos Segundos lleva durando')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameQueueConfigId=models.BigIntegerField(u'Tipo de partida(RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)')#The queue type (queue types are documented on the Game Constants page)
    gameStartTime=models.BigIntegerField(u'Hora de inicio en milisegundos')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    mapId=models.BigIntegerField(u'Id del mapa')
    observers=models.CharField(Observer)
    participants=models.CharField(CurrentGameParicipant)
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
    masteries=models.CharField(Mastery)
    profileIconId=models.BigIntegerField(u'Id del icono de invocador que esta usando')
    runes=models.CharField(Rune)
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
    gameList=models.CharField(FeaturedGameInfo)

class FeaturedGamesInfo(models.Model):
#Datos de los juegos Importantes
    bannedChampions=models.CharField(BannedChampions)
    gameId=models.BigIntegerField(u'Id del Partido')
    gameLength=models.BigIntegerField(u'Cuantos Segundos lleva durando')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameQueueConfigId=models.BigIntegerField(u'Tipo de partida(RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)')
    gameStartTime=models.BigIntegerField(u'Hora de inicio en milisegundos')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    mapId=models.BigIntegerField(u'Id del mapa')
    observers=models.CharField(Observer)
    participants=models.CharField(CurrentGameParicipant)
    platformId=models.CharField(u'Id de la plataforma en la que esta siendo jugado')

#####################################################################################################

class RecentGamesDto(models.Model):
#Juegos recientes de X jugador
    games=models.CharField(GameDto)
    summonerId=models.BigIntegerField(u'Id del jugador')

class GameDto(models.Model):
#Informacion de los juegos recientes de X jugador
    championId=models.IntegerField(u'Id del Pj usado')
    createDate=models.BigIntegerField(u'Fecha en la que se grabo los datos del final del partido')
    fellowPlayers=models.CharField(PlayerDto)
    gameId=models.models.BigIntegerField(u'Id de la partida')
    gameMode=models.CharField(u'Modo(CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)')
    gameType=models.CharField(u'Tipo de Juego(CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)')
    invalid=models.BooleanField(u'Invalid flag(Supongo que es derrota evitada)')
    ipEarned=models.IntegerField(u'IP ganado')
    level=models.IntegerField(u'Nivel en el que termino')
    mapId=models.IntegerField(u'Id del mapa')
    spell1=models.IntegerField(u'Id del Summoner Spell 1')
    spell2=models.IntegerField(u'Id del Summoner Spell 2')
    stats=models.OneToOneField(RawStatsDto)#KDA y otros datos
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
    entries=models.CharField(LeagueEntryDto)
    name=models.CharField(u'Nombre expresado del jugador en esta liga')
    participantId=models.CharField(u'Id del perteneciente a esta liga (Sea un team o un jugador)')
    queue=models.CharField(u'Tipo de juego(RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)')
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
    miniSeries=models.OneToOneField(MiniSeriesDto)
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
    #Lista de la INFO de los campeones
    data=REFERENCIARaMAP(string,ChampionDto)
    exFormat=models.CharField(u'Formato')
    keys=REFERENCIARaMAP(string,string)
    exType=models.CharField(u'Qué está enlistado')
    version=models.CharField(u'Version de la Info')
    
class ChampionsDto(models.Model):
    #Datos del campeon
    allytips=models.CharField(string)#Tips para los aliados del Pj
    blurb=models.CharField(u'')
    enemytips=models.CharField(string)#Tips para los enemigos del Pj
    exId=models.IntegerField(u'Id del Pj')
    image=models.OneToOneField(ImageDto)
    info=models.OneToOneField(InfoDto)
    key=models.CharField(u'Nombre clave del Pj (cumple una funcion similar a la ID, pero no son lo mismo)')
    lore=models.CharField(u'Historia del Pj')
    name=models.CharField(u'Nombre del Pj')
    partype=models.CharField(u'Qué tiene en la segunda barra(Heat, Mana, Energy, None, Battlefury; los campeones que usan vida para pagar el coste de sus habilidades figuran como "partype:None")')
    passive=models.OneToOneField(PassiveDto)
    recommended=models.CharField(RecommendedDto)
    skins=models.CharField(SkinDto)
    spells=models.CharField(ChampionSpellDto)
    stats=models.OneToOneField(StatsDto)
    tags=models.CharField(string)#Roles que puede cumplir el Pj
    title=models.CharField(u'Titulo del Pj')
    
class ChampionsSpellDto(models.Model):
    #INFO de los spells
    altimages=models.CharField(ImageDto)
    cooldown=models.CharField(double)
    cooldownBurn=models.CharField(u'Cooldown a travez de los niveles de la habilidad')
    cost=models.CharField(int)
    costBurn=models.CharField(u'Coste de Energia/Mana/Furia/Heat  (no incluye coste de vida)')
    costType=models.CharField(u'Tipo de Coste pofcurrentHealth(vida)/Energia/Mana/Furia/Heat(calor)')
    description=models.CharField(u'Descripcion de la habilidad')
    effect=models.CharField(object)
    effectBurn=models.CharField(string)
    image=models.OneToOneField(ImageDto)
    key=models.CharField(u'Key de la habilidad')
    leveltip=models.OneToOneField(LevelTipDto)
    maxrank=models.IntegerField(u'Nivel maximo de la habilidad')
    name=models.CharField(u'Nombre de la habilidad')
    exRange=models.OBJECTO(u'Lista con los rango de la habilidad(This field is either a List of Integer or the String ''self'' for spells that target ones own champion)')
    rangeBurn=models.CharField(u'Rango a travez de los niveles de la habilidad')
    resource=models.CharField(u'Muestra el coste de la habilidad, obteniendolo desde la variable "cost"')
    sanitizedTooltip=models.CharField(u'Funcion concreta de la habilidad')
    sanitizedDescription=models.CharField(u'Descripcion concreta de lo que hace la habilidad')
    tooltip=models.CharField(u'Funcion de la habilidad')
    exVars=models.CharField(SpellsVarDto)
    
    
class ImageDto(models.Model)
    #Datos de las imagenes
    full=models.CharField(u'Nombre del archivo con la imagen completa')
    group=models.CharField(u'Grupo al que pertenece la imagen(ej: spell)')
    h=models.IntegerField(u'Desconocido')
    sprite=models.CharField(u'Nombre del archivo con la imagen que se va a mostrar')
    w=models.IntegerField(u'Desconocido')
    x=models.IntegerField(u'Desconocido')
    y=models.IntegerField(u'Desconocido')
    
class InfoDto(models.Model):
    #INFO basica de los campeones
    attack=models.IntegerField(u'Ataque segun Riot')
    defense=models.IntegerField(u'Defensa segun Riot')
    difficulty=models.IntegerField(u'Dificultad segun Riot')
    magic=models.IntegerField(u'Poder magico segun Riot')

class PassiveDto(models.Model):
    #Datos de la pasiva del campeon
    description=models.CharField(u'Descripcion')
    image=models.OneToOneField(ImageDto)#Icono de la pasiva
    name=models.CharField(u'Nombre de la pasiva')
    sanitizedDescription=models.CharField(u'Descripcion concreta')
    
class RecommendedDto(models.Model):
    #Data de las recomendaciones para los campeones
    blockseffectBurn=models.CharField(BlockDto)
    champion=models.CharField(u'Nombre del Campeon')
    exMap=models.CharField(u'Mapa')
    mode=models.CharField(u'Modo en el que se recomiendan(CLASSIC, ARAM, etc)')
    priority=models.BooleanField(u'Prioridad')
    title=models.CharField(u'Titulo de la Build')
    exType=models.CharField(u'Titulo del conjunto de items(iniciales, finales, etc)')
    
class SkinDto(models.Model):
    #Data de los Skins
    exId=models.IntegerField(u'Id de la skin')
    name=models.CharField(u'Nombre de la skin')
    num=models.IntegerField(u'Numero de skin de este Pj(Default=0)')
    
class StatsDto (models.Model):#Estos Valores deberian ser Double
    #Data de las estadisticas del campeon
    armor=models.FloatField(u'Armadura')
    armorperlevel=models.FloatField(u'Armadura ganada por nivel')
    attackdamage=models.FloatField(u'AD')
    attackdamageperlevel=models.FloatField(u'AD ganado por nivel')
    crit=models.FloatField(u'Probabilidad de critico')
    critperlevel=models.FloatField(u'Probabilidad de critico por nivel')
    hp=models.FloatField(u'Vida')
    hpperlevel=models.FloatField(u'Vida por nivel')
    hpregen=models.FloatField(u'Regeneracion de vida')
    hpregenperlevel=models.FloatField(u'Regeneracion de vida')
    movespeed=models.FloatField(u'Velocidad de movimiento')
    mp=models.FloatField(u'Mana/Energia/etc')
    mpperlevel=models.FloatField(u'Ganancia de Mana/Energia/etc por nivel')
    mpregen=models.FloatField(u'Regeneracion Mana/Energia/etc')
    mpregenperlevel=models.FloatField(u'Regeneracion de Mana/Energia/etc por nivel')
    spellblock=models.FloatField(u'Defensa magica')
    spellblockperlevel=models.FloatField(u'Defensa magica por nivel')
    
class LevelTipDto(models.Model):
    #This object contains champion level tip data.
    effect=models.CharField(string)
    label=models.CharField(string)
    
class SpellVarsDto(models.Model):
    #Data de los spells	
    coeff=models.CharField(double)
    dyn=models.CharField(u'Si el spell tiene daño dinamico, especifica si el daño aumenta(+) o diminuye(-)')
    keyslink=models.CharField(u'Key del spell')
    link=models.CharField(u'Link del spell, donde se especifica si tiene un daño estatico o dinamico(que depende de otra variable)')
    ranksWith=models.CharField(u'Variable rara que solo tiene karma(value=KarmaMantra)')
    
class BlockDto(models.Model):
    #Datos de los items recomendados
    items=models.CharField(BlockItemDto)
    recMath=models.BooleanGield(u'Item con "Unica Pasiva"')
    exType=models.CharField(u'Tipo de los items')
    
class BlockItemDto(models.Model):
    count=models.IntegerField(u'Cantidad de el item a comprar')
    exId=models.IntegerField(u'ID del item')   

#####################################################################################################

class ItemListDto(models.Model):
    basic	BasicDataDto	
    data	Map[string, ItemDto]
    groups	List[GroupDto]
    tree	List[ItemTreeDto]
    exType	string	
    version	string
    
class BasicDataDto(models.Model):
    colloq	string	
    consumeOnFull	boolean	
    consumed	boolean	
    depth	int	
    description	string	
    exFrom	List[string]	
    gold	GoldDto	Data Dragon includes the gold field for basic data, which is shared by both rune and item. However, only items have a gold field on them, representing their gold cost in the store. Since runes are not sold in the store, they have no gold cost.
    group	string	
    hideFromAll	boolean	
    exId	int	
    image	ImageDto	
    inStore	boolean	
    into	List[string]	
    maps	Map[string, boolean]	
    name	string	
    plaintext	string	
    requiredChampion	string	
    rune	MetaDataDto	
    sanitizedDescription	string	
    specialRecipe	int	
    stacks	int	
    stats	BasicDataStatsDto	
    tags	List[string]
    
class GroupDto(models.Model):
    MaxGroupOwnable	string	
    key	string
    
class ItemDto(models.Model):
    colloq	string	
    consumeOnFull	boolean	
    consumed	boolean	
    depth	int	
    description	string	
    effect	Map[string, string]	
    from	List[string]	
    gold	GoldDto	Data Dragon includes the gold field for basic data, which is shared by both rune and item. However, only items have a gold field on them, representing their gold cost in the store. Since runes are not sold in the store, they have no gold cost.
    group	string	
    hideFromAll	boolean	
    id	int	
    image	ImageDto	
    inStore	boolean	
    into	List[string]	
    maps	Map[string, boolean]	
    name	string	
    plaintext	string	
    requiredChampion	string	
    rune	MetaDataDto	
    sanitizedDescription	string	
    specialRecipe	int	
    stacks	int	
    stats	BasicDataStatsDto	
    tags	List[string]
    
class ItemTreeDto(models.Model):
    header	string	
    tags	List[string]
    
class BasicDataStatsDto(models.Model):
    FlatArmorMod	double	
    FlatAttackSpeedMod	double	
    FlatBlockMod	double	
    FlatCritChanceMod	double	
    FlatCritDamageMod	double	
    FlatEXPBonus	double	
    FlatEnergyPoolMod	double	
    FlatEnergyRegenMod	double	
    FlatHPPoolMod	double	
    FlatHPRegenMod	double	
    FlatMPPoolMod	double	
    FlatMPRegenMod	double	
    FlatMagicDamageMod	double	
    FlatMovementSpeedMod	double	
    FlatPhysicalDamageMod	double	
    FlatSpellBlockMod	double	
    PercentArmorMod	double	
    PercentAttackSpeedMod	double	
    PercentBlockMod	double	
    PercentCritChanceMod	double	
    PercentCritDamageMod	double	
    PercentDodgeMod	double	
    PercentEXPBonus	double	
    PercentHPPoolMod	double	
    PercentHPRegenMod	double	
    PercentLifeStealMod	double	
    PercentMPPoolMod	double	
    PercentMPRegenMod	double	
    PercentMagicDamageMod	double	
    PercentMovementSpeedMod	double	
    PercentPhysicalDamageMod	double	
    PercentSpellBlockMod	double	
    PercentSpellVampMod	double	
    rFlatArmorModPerLevel	double	
    rFlatArmorPenetrationMod	double	
    rFlatArmorPenetrationModPerLevel	double	
    rFlatCritChanceModPerLevel	double	
    rFlatCritDamageModPerLevel	double	
    rFlatDodgeMod	double	
    rFlatDodgeModPerLevel	double	
    rFlatEnergyModPerLevel	double	
    rFlatEnergyRegenModPerLevel	double	
    rFlatGoldPer10Mod	double	
    rFlatHPModPerLevel	double	
    rFlatHPRegenModPerLevel	double	
    rFlatMPModPerLevel	double	
    rFlatMPRegenModPerLevel	double	
    rFlatMagicDamageModPerLevel	double	
    rFlatMagicPenetrationMod	double	
    rFlatMagicPenetrationModPerLevel	double	
    rFlatMovementSpeedModPerLevel	double	
    rFlatPhysicalDamageModPerLevel	double	
    rFlatSpellBlockModPerLevel	double	
    rFlatTimeDeadMod	double	
    rFlatTimeDeadModPerLevel	double	
    rPercentArmorPenetrationMod	double	
    rPercentArmorPenetrationModPerLevel	double	
    rPercentAttackSpeedModPerLevel	double	
    rPercentCooldownMod	double	
    rPercentCooldownModPerLevel	double	
    rPercentMagicPenetrationMod	double	
    rPercentMagicPenetrationModPerLevel	double	
    rPercentMovementSpeedModPerLevel	double	
    rPercentTimeDeadMod	double	
    rPercentTimeDeadModPerLevel    double
    
class GoldDto(models.Model):
    base	int	
    purchasable	boolean	
    sell	int	
    total	int
    
class ImageDto(models.Model):
    full	string	
    group	string	
    h	int	
    sprite	string	
    w	int	
    x	int	
    y	int
    
class MetaDataDto(models.Model):
    isRune	boolean	
    tier	string	
    exType	string
    
#####################################################################################################

class LanguageStringsDto(models.Model):
    data	Map[string, string]	
    exType	string	
    version	string
    
#####################################################################################################
#PARTE DE LA API SIN BASE DE DATOS.............GET /api/lol/static-data/{region}/v1.2/languages    
#####################################################################################################

class MapDataDto(models.Model):
    data	Map[string, MapDetailsDto]	
    exType	string	
    version	string
    
class MapDetailsDto(models.Model):
    image	ImageDto	
    mapId	long	
    mapName	string	
    unpurchasableItemList	List[long]
    
class ImageDto(models.Model):
    full	string	
    group	string	
    h	int	
    sprite	string	
    w	int	
    x	int	
    y	int
    
#####################################################################################################

class MasteryListDto(models.Model):
    data	Map[string, MasteryDto]	
    tree	MasteryTreeDto	
    exType	string	
    version	string

class MasteryDto(models.Model):
    description	List[string]	
    exId	int	
    image	ImageDto	
    masteryTree	string	Legal values: Defense, Offense, Utility
    name	string	
    prereq	string	
    ranks	int	
    sanitizedDescription	List[string]
    
class MasteryTreeDto(models.Model):
    Defense	List[MasteryTreeListDto]	
    Offense	List[MasteryTreeListDto]	
    Utility	List[MasteryTreeListDto]
    
class ImageDto(models.Model):
    full	string	
    group	string	
    h	int	
    sprite	string	
    w	int	
    x	int	
    y	int
    
class MasteryTreeListDto(models.Model):
    masteryTreeItems	List[MasteryTreeItemDto]
    
class MasteryTreeItemDto(models.Model):
    masteryId	int	
    prereq	string
    
#####################################################################################################

class RealmDto(models.Model):
    cdn	string	The base CDN url.
    css	string	Latest changed version of Dragon Magic's css file.
    dd	string	Latest changed version of Dragon Magic.
    l	string	Default language for this realm.
    lg	string	Legacy script mode for IE6 or older.
    n	Map[string, string]	Latest changed version for each data type listed.
    profileiconmax	int	Special behavior number identifying the largest profileicon id that can be used under 500. Any profileicon that is requested between this number and 500 should be mapped to 0.
    store	string	Additional api data drawn from other sources that may be related to data dragon functionality.
    v	string	Current version of this file for this realm.    
    
#####################################################################################################

class RuneListDto(models.Model):
    basic	BasicDataDto	
    data	Map[string, RuneDto]	
    exType	string	
    version	string

class BasicDataDto(models.Model):
    colloq	string	
    consumeOnFull	boolean	
    consumed	boolean	
    depth	int	
    description	string	
    exFrom	List[string]	
    gold	GoldDto	Data Dragon includes the gold field for basic data, which is shared by both rune and item. However, only items have a gold field on them, representing their gold cost in the store. Since runes are not sold in the store, they have no gold cost.
    group	string	
    hideFromAll	boolean	
    exId	int	
    image	ImageDto	
    inStore	boolean	
    into	List[string]	
    maps	Map[string, boolean]	
    name	string	
    plaintext	string	
    requiredChampion	string	
    rune	MetaDataDto	
    sanitizedDescription	string	
    specialRecipe	int	
    stacks	int	
    stats	BasicDataStatsDto	
    tags	List[string]

class RuneDto(models.Model):
    colloq	string	
    consumeOnFull	boolean	
    consumed	boolean	
    depth	int	
    description	string	
    exFrom	List[string]	
    group	string	
    hideFromAll	boolean	
    exId	int	
    image	ImageDto	
    inStore	boolean	
    into	List[string]	
    maps	Map[string, boolean]	
    name	string	
    plaintext	string	
    requiredChampion	string	
    rune	MetaDataDto	
    sanitizedDescription	string	
    specialRecipe	int	
    stacks	int	
    stats	BasicDataStatsDto	
    tags	List[string]

class BasicDataStatsDto(models.Model):
    FlatArmorMod	double	
    FlatAttackSpeedMod	double	
    FlatBlockMod	double	
    FlatCritChanceMod	double	
    FlatCritDamageMod	double	
    FlatEXPBonus	double	
    FlatEnergyPoolMod	double	
    FlatEnergyRegenMod	double	
    FlatHPPoolMod	double	
    FlatHPRegenMod	double	
    FlatMPPoolMod	double	
    FlatMPRegenMod	double	
    FlatMagicDamageMod	double	
    FlatMovementSpeedMod	double	
    FlatPhysicalDamageMod	double	
    FlatSpellBlockMod	double	
    PercentArmorMod	double	
    PercentAttackSpeedMod	double	
    PercentBlockMod	double	
    PercentCritChanceMod	double	
    PercentCritDamageMod	double	
    PercentDodgeMod	double	
    PercentEXPBonus	double	
    PercentHPPoolMod	double	
    PercentHPRegenMod	double	
    PercentLifeStealMod	double	
    PercentMPPoolMod	double	
    PercentMPRegenMod	double	
    PercentMagicDamageMod	double	
    PercentMovementSpeedMod	double	
    PercentPhysicalDamageMod	double	
    PercentSpellBlockMod	double	
    PercentSpellVampMod	double	
    rFlatArmorModPerLevel	double	
    rFlatArmorPenetrationMod	double	
    rFlatArmorPenetrationModPerLevel	double	
    rFlatCritChanceModPerLevel	double	
    rFlatCritDamageModPerLevel	double	
    rFlatDodgeMod	double	
    rFlatDodgeModPerLevel	double	
    rFlatEnergyModPerLevel	double	
    rFlatEnergyRegenModPerLevel	double	
    rFlatGoldPer10Mod	double	
    rFlatHPModPerLevel	double	
    rFlatHPRegenModPerLevel	double	
    rFlatMPModPerLevel	double	
    rFlatMPRegenModPerLevel	double	
    rFlatMagicDamageModPerLevel	double	
    rFlatMagicPenetrationMod	double	
    rFlatMagicPenetrationModPerLevel	double	
    rFlatMovementSpeedModPerLevel	double	
    rFlatPhysicalDamageModPerLevel	double	
    rFlatSpellBlockModPerLevel	double	
    rFlatTimeDeadMod	double	
    rFlatTimeDeadModPerLevel	double	
    rPercentArmorPenetrationMod	double	
    rPercentArmorPenetrationModPerLevel	double	
    rPercentAttackSpeedModPerLevel	double	
    rPercentCooldownMod	double	
    rPercentCooldownModPerLevel	double	
    rPercentMagicPenetrationMod	double	
    rPercentMagicPenetrationModPerLevel	double	
    rPercentMovementSpeedModPerLevel	double	
    rPercentTimeDeadMod	double	
    rPercentTimeDeadModPerLevel	double

class GoldDto(models.Model):
    base	int	
    purchasable	boolean	
    sell	int	
    total	int

class ImageDto(models.Model):
    full	string	
    group	string	
    h	int	
    sprite	string	
    w	int	
    x	int	
    y	int

class MetaDataDto(models.Model):
    isRune	boolean	
    tier	string	
    exType	string

#####################################################################################################

class SummonerSpellListDto(models.Model):
    data	Map[string, SummonerSpellDto]	
    exType	string	
    version	string

class SummonerSpellDto(models.Model):
    cooldown	List[double]	
    cooldownBurn	string	
    cost	List[int]	
    costBurn	string	
    costType	string	
    description	string	
    effect	List[object]	This field is a List of List of Double.
    effectBurn	List[string]	
    exId	int	
    image	ImageDto	
    key	string	
    leveltip	LevelTipDto	
    maxrank	int	
    modes	List[string]	
    name	string	
    exRange	object	This field is either a List of Integer or the String 'self' for spells that target one's own champion.
    rangeBurn	string	
    resource	string	
    sanitizedDescription	string	
    sanitizedTooltip	string	
    summonerLevel	int	
    tooltip	string	
    exVars	List[SpellVarsDto]

class ImageDto(models.Model):
    full	string	
    group	string	
    h	int	
    sprite	string	
    w	int	
    x	int	
    y	int

class LevelTipDto(models.Model):
    effect	List[string]	
    label	List[string]

class SpellVarsDto(models.Model):
    coeff	List[double]	
    dyn	string	
    key	string	
    link	string	
    ranksWith	string

    
#####################################################################################################
#PARTE DE LA API SIN BASE DE DATOS.............GET /api/lol/static-data/{region}/v1.2/versions    
#####################################################################################################

class Shard(models.Model):
    hostname	string	
    locales	List[string]	
    name	string	
    region_tag	string	
    slug	string

#####################################################################################################

class ShardStatus(models.Model):
    hostname	string	
    locales	List[string]	
    name	string	
    region_tag	string	
    services	List[Service]	
    slug	string

class Service(models.Model):
    incidents	List[Incident]	
    name	string	
    slug	string	
    status	string	Legal values: Online, Alert, Offline, Deploying

class Incident(models.Model):
    active	boolean	
    created_at	string	
    exId	long	
    updates	List[Message]

class Message(models.Model):
    author	string	
    content	string	
    created_at	string	
    exId	long	
    severity	string	Legal values: Info, Alert, Error
    translations	List[Translation]	
    updated_at	string

class Translation(models.Model):
    content	string	
    locale	string	
    updated_at	string

#####################################################################################################

class MatchDetail(models.Model):
    mapId	int	Match map ID
    matchCreation	long	Match creation time. Designates when the team select lobby is created and/or the match is made through match making, not when the game actually starts.
    matchDuration	long	Match duration
    matchId	long	ID of the match
    matchMode	string	Match mode (Legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)
    matchType	string	Match type (Legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
    matchVersion	string	Match version
    participantIdentities	List[ParticipantIdentity]	Participant identity information
    participants	List[Participant]	Participant information
    platformId	string	Platform ID of the match
    queueType	string	Match queue type (Legal values: CUSTOM, NORMAL_5x5_BLIND, RANKED_SOLO_5x5, RANKED_PREMADE_5x5, BOT_5x5, NORMAL_3x3, RANKED_PREMADE_3x3, NORMAL_5x5_DRAFT, ODIN_5x5_BLIND, ODIN_5x5_DRAFT, BOT_ODIN_5x5, BOT_5x5_INTRO, BOT_5x5_BEGINNER, BOT_5x5_INTERMEDIATE, RANKED_TEAM_3x3, RANKED_TEAM_5x5, BOT_TT_3x3, GROUP_FINDER_5x5, ARAM_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF_5x5, ONEFORALL_MIRRORMODE_5x5, BOT_URF_5x5, NIGHTMARE_BOT_5x5_RANK1, NIGHTMARE_BOT_5x5_RANK2, NIGHTMARE_BOT_5x5_RANK5, ASCENSION_5x5, HEXAKILL, BILGEWATER_ARAM_5x5, KING_PORO_5x5, COUNTER_PICK, BILGEWATER_5x5)
    region	string	Region where the match was played
    season	string	Season match was played (Legal values: PRESEASON3, SEASON3, PRESEASON2014, SEASON2014, PRESEASON2015, SEASON2015)
    teams	List[Team]	Team information
    timeline	Timeline	Match timeline data (not included by default)

class Participant(models.Model):
    championId	int	Champion ID
    highestAchievedSeasonTier	string	Highest ranked tier achieved for the previous season, if any, otherwise null. Used to display border in game loading screen. (Legal values: CHALLENGER, MASTER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, UNRANKED)
    masteries	List[Mastery]	List of mastery information
    participantId	int	Participant ID
    runes	List[Rune]	List of rune information
    spell1Id	int	First summoner spell ID
    spell2Id	int	Second summoner spell ID
    stats	ParticipantStats	Participant statistics
    teamId	int	Team ID
    timeline	ParticipantTimeline	Timeline data. Delta fields refer to values for the specified period (e.g., the gold per minute over the first 10 minutes of the game versus the second 20 minutes of the game. Diffs fields refer to the deltas versus the calculated lane opponent(s).

class ParticipantIdentity(models.Model):
    participantId	int	Participant ID
    player	Player	Player information

class Team(models.Model):
    bans	List[BannedChampion]	If game was draft mode, contains banned champion data, otherwise null
    baronKills	int	Number of times the team killed baron
    dominionVictoryScore	long	If game was a dominion game, specifies the points the team had at game end, otherwise null
    dragonKills	int	Number of times the team killed dragon
    firstBaron	boolean	Flag indicating whether or not the team got the first baron kill
    firstBlood	boolean	Flag indicating whether or not the team got first blood
    firstDragon	boolean	Flag indicating whether or not the team got the first dragon kill
    firstInhibitor	boolean	Flag indicating whether or not the team destroyed the first inhibitor
    firstTower	boolean	Flag indicating whether or not the team destroyed the first tower
    inhibitorKills	int	Number of inhibitors the team destroyed
    teamId	int	Team ID
    towerKills	int	Number of towers the team destroyed
    vilemawKills	int	Number of times the team killed vilemaw
    winner	boolean	Flag indicating whether or not the team won

class Timeline(models.Model):
    frameInterval	long	Time between each returned frame in milliseconds.
    frames	List[Frame]	List of timeline frames for the game.

class Mastery(models.Model):
    masteryId	long	Mastery ID
    rank	long	Mastery rank

class ParticipantStats(models.Model):
    assists	long	Number of assists
    champLevel	long	Champion level achieved
    combatPlayerScore	long	If game was a dominion game, player's combat score, otherwise 0
    deaths	long	Number of deaths
    doubleKills	long	Number of double kills
    firstBloodAssist	boolean	Flag indicating if participant got an assist on first blood
    firstBloodKill	boolean	Flag indicating if participant got first blood
    firstInhibitorAssist	boolean	Flag indicating if participant got an assist on the first inhibitor
    firstInhibitorKill	boolean	Flag indicating if participant destroyed the first inhibitor
    firstTowerAssist	boolean	Flag indicating if participant got an assist on the first tower
    firstTowerKill	boolean	Flag indicating if participant destroyed the first tower
    goldEarned	long	Gold earned
    goldSpent	long	Gold spent
    inhibitorKills	long	Number of inhibitor kills
    item0	long	First item ID
    item1	long	Second item ID
    item2	long	Third item ID
    item3	long	Fourth item ID
    item4	long	Fifth item ID
    item5	long	Sixth item ID
    item6	long	Seventh item ID
    killingSprees	long	Number of killing sprees
    kills	long	Number of kills
    largestCriticalStrike	long	Largest critical strike
    largestKillingSpree	long	Largest killing spree
    largestMultiKill	long	Largest multi kill
    magicDamageDealt	long	Magical damage dealt
    magicDamageDealtToChampions	long	Magical damage dealt to champions
    magicDamageTaken	long	Magic damage taken
    minionsKilled	long	Minions killed
    neutralMinionsKilled	long	Neutral minions killed
    neutralMinionsKilledEnemyJungle	long	Neutral jungle minions killed in the enemy team's jungle
    neutralMinionsKilledTeamJungle	long	Neutral jungle minions killed in your team's jungle
    nodeCapture	long	If game was a dominion game, number of node captures
    nodeCaptureAssist	long	If game was a dominion game, number of node capture assists
    nodeNeutralize	long	If game was a dominion game, number of node neutralizations
    nodeNeutralizeAssist	long	If game was a dominion game, number of node neutralization assists
    objectivePlayerScore	long	If game was a dominion game, player's objectives score, otherwise 0
    pentaKills	long	Number of penta kills
    physicalDamageDealt	long	Physical damage dealt
    physicalDamageDealtToChampions	long	Physical damage dealt to champions
    physicalDamageTaken	long	Physical damage taken
    quadraKills	long	Number of quadra kills
    sightWardsBoughtInGame	long	Sight wards purchased
    teamObjective	long	If game was a dominion game, number of completed team objectives (i.e., quests)
    totalDamageDealt	long	Total damage dealt
    totalDamageDealtToChampions	long	Total damage dealt to champions
    totalDamageTaken	long	Total damage taken
    totalHeal	long	Total heal amount
    totalPlayerScore	long	If game was a dominion game, player's total score, otherwise 0
    totalScoreRank	long	If game was a dominion game, team rank of the player's total score (e.g., 1-5)
    totalTimeCrowdControlDealt	long	Total dealt crowd control time
    totalUnitsHealed	long	Total units healed
    towerKills	long	Number of tower kills
    tripleKills	long	Number of triple kills
    trueDamageDealt	long	True damage dealt
    trueDamageDealtToChampions	long	True damage dealt to champions
    trueDamageTaken	long	True damage taken
    unrealKills	long	Number of unreal kills
    visionWardsBoughtInGame	long	Vision wards purchased
    wardsKilled	long	Number of wards killed
    wardsPlaced	long	Number of wards placed
    winner	boolean	Flag indicating whether or not the participant won

class ParticipantTimeline(models.Model):
    ancientGolemAssistsPerMinCounts	ParticipantTimelineData	Ancient golem assists per minute timeline counts
    ancientGolemKillsPerMinCounts	ParticipantTimelineData	Ancient golem kills per minute timeline counts
    assistedLaneDeathsPerMinDeltas	ParticipantTimelineData	Assisted lane deaths per minute timeline data
    assistedLaneKillsPerMinDeltas	ParticipantTimelineData	Assisted lane kills per minute timeline data
    baronAssistsPerMinCounts	ParticipantTimelineData	Baron assists per minute timeline counts
    baronKillsPerMinCounts	ParticipantTimelineData	Baron kills per minute timeline counts
    creepsPerMinDeltas	ParticipantTimelineData	Creeps per minute timeline data
    csDiffPerMinDeltas	ParticipantTimelineData	Creep score difference per minute timeline data
    damageTakenDiffPerMinDeltas	ParticipantTimelineData	Damage taken difference per minute timeline data
    damageTakenPerMinDeltas	ParticipantTimelineData	Damage taken per minute timeline data
    dragonAssistsPerMinCounts	ParticipantTimelineData	Dragon assists per minute timeline counts
    dragonKillsPerMinCounts	ParticipantTimelineData	Dragon kills per minute timeline counts
    elderLizardAssistsPerMinCounts	ParticipantTimelineData	Elder lizard assists per minute timeline counts
    elderLizardKillsPerMinCounts	ParticipantTimelineData	Elder lizard kills per minute timeline counts
    goldPerMinDeltas	ParticipantTimelineData	Gold per minute timeline data
    inhibitorAssistsPerMinCounts	ParticipantTimelineData	Inhibitor assists per minute timeline counts
    inhibitorKillsPerMinCounts	ParticipantTimelineData	Inhibitor kills per minute timeline counts
    lane	string	Participant's lane (Legal values: MID, MIDDLE, TOP, JUNGLE, BOT, BOTTOM)
    role	string	Participant's role (Legal values: DUO, NONE, SOLO, DUO_CARRY, DUO_SUPPORT)
    towerAssistsPerMinCounts	ParticipantTimelineData	Tower assists per minute timeline counts
    towerKillsPerMinCounts	ParticipantTimelineData	Tower kills per minute timeline counts
    towerKillsPerMinDeltas	ParticipantTimelineData	Tower kills per minute timeline data
    vilemawAssistsPerMinCounts	ParticipantTimelineData	Vilemaw assists per minute timeline counts
    vilemawKillsPerMinCounts	ParticipantTimelineData	Vilemaw kills per minute timeline counts
    wardsPerMinDeltas	ParticipantTimelineData	Wards placed per minute timeline data
    xpDiffPerMinDeltas	ParticipantTimelineData	Experience difference per minute timeline data
    xpPerMinDeltas	ParticipantTimelineData	Experience per minute timeline data

class Rune(models.Model):
    rank	long	Rune rank
    runeId	long	Rune ID

class Player(models.Model):
    matchHistoryUri	string	Match history URI
    profileIcon	int	Profile icon ID
    summonerId	long	Summoner ID
    summonerName	string	Summoner name

class BannedChampion(models.Model):
    championId	int	Banned champion ID
    pickTurn	int	Turn during which the champion was banned

class Frame(models.Model):
    events	List[Event]	List of events for this frame.
    participantFrames	Map[string, ParticipantFrame]	Map of each participant ID to the participant's information for the frame.
    timestamp	long	Represents how many milliseconds into the game the frame occurred.

class ParticipantTimelineData(models.Model):
    tenToTwenty	double	Value per minute from 10 min to 20 min
    thirtyToEnd	double	Value per minute from 30 min to the end of the game
    twentyToThirty	double	Value per minute from 20 min to 30 min
    zeroToTen	double	Value per minute from the beginning of the game to 10 min

class Event(models.Model):
    ascendedType	string	The ascended type of the event. Only present if relevant. Note that CLEAR_ASCENDED refers to when a participants kills the ascended player. (Legal values: CHAMPION_ASCENDED, CLEAR_ASCENDED, MINION_ASCENDED)
    assistingParticipantIds	List[int]	The assisting participant IDs of the event. Only present if relevant.
    buildingType	string	The building type of the event. Only present if relevant. (Legal values: INHIBITOR_BUILDING, TOWER_BUILDING)
    creatorId	int	The creator ID of the event. Only present if relevant.
    eventType	string	Event type. (Legal values: ASCENDED_EVENT, BUILDING_KILL, CAPTURE_POINT, CHAMPION_KILL, ELITE_MONSTER_KILL, ITEM_DESTROYED, ITEM_PURCHASED, ITEM_SOLD, ITEM_UNDO, PORO_KING_SUMMON, SKILL_LEVEL_UP, WARD_KILL, WARD_PLACED)
    itemAfter	int	The ending item ID of the event. Only present if relevant.
    itemBefore	int	The starting item ID of the event. Only present if relevant.
    itemId	int	The item ID of the event. Only present if relevant.
    killerId	int	The killer ID of the event. Only present if relevant. Killer ID 0 indicates a minion.
    laneType	string	The lane type of the event. Only present if relevant. (Legal values: BOT_LANE, MID_LANE, TOP_LANE)
    levelUpType	string	The level up type of the event. Only present if relevant. (Legal values: EVOLVE, NORMAL)
    monsterType	string	The monster type of the event. Only present if relevant. (Legal values: BARON_NASHOR, BLUE_GOLEM, DRAGON, RED_LIZARD, VILEMAW)
    participantId	int	The participant ID of the event. Only present if relevant.
    pointCaptured	string	The point captured in the event. Only present if relevant. (Legal values: POINT_A, POINT_B, POINT_C, POINT_D, POINT_E)
    position	Position	The position of the event. Only present if relevant.
    skillSlot	int	The skill slot of the event. Only present if relevant.
    teamId	int	The team ID of the event. Only present if relevant.
    timestamp	long	Represents how many milliseconds into the game the event occurred.
    towerType	string	The tower type of the event. Only present if relevant. (Legal values: BASE_TURRET, FOUNTAIN_TURRET, INNER_TURRET, NEXUS_TURRET, OUTER_TURRET, UNDEFINED_TURRET)
    victimId	int	The victim ID of the event. Only present if relevant.
    wardType	string	The ward type of the event. Only present if relevant. (Legal values: SIGHT_WARD, TEEMO_MUSHROOM, UNDEFINED, VISION_WARD, YELLOW_TRINKET, YELLOW_TRINKET_UPGRADE)

class ParticipantFrame(models.Model):
    currentGold	int	Participant's current gold
    dominionScore	int	Dominion score of the participant
    jungleMinionsKilled	int	Number of jungle minions killed by participant
    level	int	Participant's current level
    minionsKilled	int	Number of minions killed by participant
    participantId	int	Participant ID
    position	Position	Participant's position
    teamScore	int	Team score of the participant
    totalGold	int	Participant's total gold
    xp	int	Experience earned by participant

class Position(models.Model):
    x	int	
    y	int

#####################################################################################################

class PlayerHistory(models.Model):
    matches	List[MatchSummary]	List of matches for the player

class MatchSummary(models.Model):
    mapId	int	Match map ID
    matchCreation	long	Match creation time. Designates when the team select lobby is created and/or the match is made through match making, not when the game actually starts.
    matchDuration	long	Match duration
    matchId	long	ID of the match
    matchMode	string	Match mode (Legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)
    matchType	string	Match type (Legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
    matchVersion	string	Match version
    participantIdentities	List[ParticipantIdentity]	Participant identity information
    participants	List[Participant]	Participant information
    platformId	string	Platform ID of the match
    queueType	string	Match queue type (Legal values: CUSTOM, NORMAL_5x5_BLIND, RANKED_SOLO_5x5, RANKED_PREMADE_5x5, BOT_5x5, NORMAL_3x3, RANKED_PREMADE_3x3, NORMAL_5x5_DRAFT, ODIN_5x5_BLIND, ODIN_5x5_DRAFT, BOT_ODIN_5x5, BOT_5x5_INTRO, BOT_5x5_BEGINNER, BOT_5x5_INTERMEDIATE, RANKED_TEAM_3x3, RANKED_TEAM_5x5, BOT_TT_3x3, GROUP_FINDER_5x5, ARAM_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF_5x5, ONEFORALL_MIRRORMODE_5x5, BOT_URF_5x5, NIGHTMARE_BOT_5x5_RANK1, NIGHTMARE_BOT_5x5_RANK2, NIGHTMARE_BOT_5x5_RANK5, ASCENSION_5x5, HEXAKILL, BILGEWATER_ARAM_5x5, KING_PORO_5x5, COUNTER_PICK, BILGEWATER_5x5)
    region	string	Region where the match was played
    season	string	Season match was played (Legal values: PRESEASON3, SEASON3, PRESEASON2014, SEASON2014, PRESEASON2015, SEASON2015)

class Participant(models.Model):
    championId	int	Champion ID
    highestAchievedSeasonTier	string	Highest ranked tier achieved for the previous season, if any, otherwise null. Used to display border in game loading screen. (Legal values: CHALLENGER, MASTER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, UNRANKED)
    masteries	List[Mastery]	List of mastery information
    participantId	int	Participant ID
    runes	List[Rune]	List of rune information
    spell1Id	int	First summoner spell ID
    spell2Id	int	Second summoner spell ID
    stats	ParticipantStats	Participant statistics
    teamId	int	Team ID
    timeline	ParticipantTimeline	Timeline data. Delta fields refer to values for the specified period (e.g., the gold per minute over the first 10 minutes of the game versus the second 20 minutes of the game. Diffs fields refer to the deltas versus the calculated lane opponent(s).

class ParticipantIdentity(models.Model):
    participantId	int	Participant ID
    player	Player	Player information

class Mastery(models.Model):
    masteryId	long	Mastery ID
    rank	long	Mastery rank

class ParticipantStats(models.Model):
    assists	long	Number of assists
    champLevel	long	Champion level achieved
    combatPlayerScore	long	If game was a dominion game, player's combat score, otherwise 0
    deaths	long	Number of deaths
    doubleKills	long	Number of double kills
    firstBloodAssist	boolean	Flag indicating if participant got an assist on first blood
    firstBloodKill	boolean	Flag indicating if participant got first blood
    firstInhibitorAssist	boolean	Flag indicating if participant got an assist on the first inhibitor
    firstInhibitorKill	boolean	Flag indicating if participant destroyed the first inhibitor
    firstTowerAssist	boolean	Flag indicating if participant got an assist on the first tower
    firstTowerKill	boolean	Flag indicating if participant destroyed the first tower
    goldEarned	long	Gold earned
    goldSpent	long	Gold spent
    inhibitorKills	long	Number of inhibitor kills
    item0	long	First item ID
    item1	long	Second item ID
    item2	long	Third item ID
    item3	long	Fourth item ID
    item4	long	Fifth item ID
    item5	long	Sixth item ID
    item6	long	Seventh item ID
    killingSprees	long	Number of killing sprees
    kills	long	Number of kills
    largestCriticalStrike	long	Largest critical strike
    largestKillingSpree	long	Largest killing spree
    largestMultiKill	long	Largest multi kill
    magicDamageDealt	long	Magical damage dealt
    magicDamageDealtToChampions	long	Magical damage dealt to champions
    magicDamageTaken	long	Magic damage taken
    minionsKilled	long	Minions killed
    neutralMinionsKilled	long	Neutral minions killed
    neutralMinionsKilledEnemyJungle	long	Neutral jungle minions killed in the enemy team's jungle
    neutralMinionsKilledTeamJungle	long	Neutral jungle minions killed in your team's jungle
    nodeCapture	long	If game was a dominion game, number of node captures
    nodeCaptureAssist	long	If game was a dominion game, number of node capture assists
    nodeNeutralize	long	If game was a dominion game, number of node neutralizations
    nodeNeutralizeAssist	long	If game was a dominion game, number of node neutralization assists
    objectivePlayerScore	long	If game was a dominion game, player's objectives score, otherwise 0
    pentaKills	long	Number of penta kills
    physicalDamageDealt	long	Physical damage dealt
    physicalDamageDealtToChampions	long	Physical damage dealt to champions
    physicalDamageTaken	long	Physical damage taken
    quadraKills	long	Number of quadra kills
    sightWardsBoughtInGame	long	Sight wards purchased
    teamObjective	long	If game was a dominion game, number of completed team objectives (i.e., quests)
    totalDamageDealt	long	Total damage dealt
    totalDamageDealtToChampions	long	Total damage dealt to champions
    totalDamageTaken	long	Total damage taken
    totalHeal	long	Total heal amount
    totalPlayerScore	long	If game was a dominion game, player's total score, otherwise 0
    totalScoreRank	long	If game was a dominion game, team rank of the player's total score (e.g., 1-5)
    totalTimeCrowdControlDealt	long	Total dealt crowd control time
    totalUnitsHealed	long	Total units healed
    towerKills	long	Number of tower kills
    tripleKills	long	Number of triple kills
    trueDamageDealt	long	True damage dealt
    trueDamageDealtToChampions	long	True damage dealt to champions
    trueDamageTaken	long	True damage taken
    unrealKills	long	Number of unreal kills
    visionWardsBoughtInGame	long	Vision wards purchased
    wardsKilled	long	Number of wards killed
    wardsPlaced	long	Number of wards placed
    winner	boolean	Flag indicating whether or not the participant won

class ParticipantTimeline(models.Model):
    ancientGolemAssistsPerMinCounts	ParticipantTimelineData	Ancient golem assists per minute timeline counts
    ancientGolemKillsPerMinCounts	ParticipantTimelineData	Ancient golem kills per minute timeline counts
    assistedLaneDeathsPerMinDeltas	ParticipantTimelineData	Assisted lane deaths per minute timeline data
    assistedLaneKillsPerMinDeltas	ParticipantTimelineData	Assisted lane kills per minute timeline data
    baronAssistsPerMinCounts	ParticipantTimelineData	Baron assists per minute timeline counts
    baronKillsPerMinCounts	ParticipantTimelineData	Baron kills per minute timeline counts
    creepsPerMinDeltas	ParticipantTimelineData	Creeps per minute timeline data
    csDiffPerMinDeltas	ParticipantTimelineData	Creep score difference per minute timeline data
    damageTakenDiffPerMinDeltas	ParticipantTimelineData	Damage taken difference per minute timeline data
    damageTakenPerMinDeltas	ParticipantTimelineData	Damage taken per minute timeline data
    dragonAssistsPerMinCounts	ParticipantTimelineData	Dragon assists per minute timeline counts
    dragonKillsPerMinCounts	ParticipantTimelineData	Dragon kills per minute timeline counts
    elderLizardAssistsPerMinCounts	ParticipantTimelineData	Elder lizard assists per minute timeline counts
    elderLizardKillsPerMinCounts	ParticipantTimelineData	Elder lizard kills per minute timeline counts
    goldPerMinDeltas	ParticipantTimelineData	Gold per minute timeline data
    inhibitorAssistsPerMinCounts	ParticipantTimelineData	Inhibitor assists per minute timeline counts
    inhibitorKillsPerMinCounts	ParticipantTimelineData	Inhibitor kills per minute timeline counts
    lane	string	Participant's lane (Legal values: MID, MIDDLE, TOP, JUNGLE, BOT, BOTTOM)
    role	string	Participant's role (Legal values: DUO, NONE, SOLO, DUO_CARRY, DUO_SUPPORT)
    towerAssistsPerMinCounts	ParticipantTimelineData	Tower assists per minute timeline counts
    towerKillsPerMinCounts	ParticipantTimelineData	Tower kills per minute timeline counts
    towerKillsPerMinDeltas	ParticipantTimelineData	Tower kills per minute timeline data
    vilemawAssistsPerMinCounts	ParticipantTimelineData	Vilemaw assists per minute timeline counts
    vilemawKillsPerMinCounts	ParticipantTimelineData	Vilemaw kills per minute timeline counts
    wardsPerMinDeltas	ParticipantTimelineData	Wards placed per minute timeline data
    xpDiffPerMinDeltas	ParticipantTimelineData	Experience difference per minute timeline data
    xpPerMinDeltas	ParticipantTimelineData	Experience per minute timeline data

class Rune(models.Model):
    rank	long	Rune rank
    runeId	long	Rune ID

class Player(models.Model):
    matchHistoryUri	string	Match history URI
    profileIcon	int	Profile icon ID
    summonerId	long	Summoner ID
    summonerName	string	Summoner name

class ParticipantTimelineData(models.Model):
    tenToTwenty	double	Value per minute from 10 min to 20 min
    thirtyToEnd	double	Value per minute from 30 min to the end of the game
    twentyToThirty	double	Value per minute from 20 min to 30 min
    zeroToTen	double	Value per minute from the beginning of the game to 10 min

#####################################################################################################

class MatchList(models.Model):
    endIndex	int	
    matches	List[MatchReference]	
    startIndex	int	
    totalGames	int

class MatchReference(models.Model):
    champion	long	
    lane	string	Legal values: MID, MIDDLE, TOP, JUNGLE, BOT, BOTTOM
    matchId	long	
    platformId	string	
    queue	string	Legal values: RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5
    role	string	Legal values: DUO, NONE, SOLO, DUO_CARRY, DUO_SUPPORT
    season	string	Legal values: PRESEASON3, SEASON3, PRESEASON2014, SEASON2014, PRESEASON2015, SEASON2015
    timestamp	long

#####################################################################################################

class RankedStatsDto(models.Model):
    champions	List[ChampionStatsDto]	Collection of aggregated stats summarized by champion.
    modifyDate	long	Date stats were last modified specified as epoch milliseconds.
    summonerId	long	Summoner ID.

class ChampionStatsDto(models.Model):
    exId	int	Champion ID. Note that champion ID 0 represents the combined stats for all champions. For static information correlating to champion IDs, please refer to the LoL Static Data API.
    stats	AggregatedStatsDto	Aggregated stats associated with the champion.

class AggregatedStatsDto(models.Model):
    averageAssists	int	Dominion only.
    averageChampionsKilled	int	Dominion only.
    averageCombatPlayerScore	int	Dominion only.
    averageNodeCapture	int	Dominion only.
    averageNodeCaptureAssist	int	Dominion only.
    averageNodeNeutralize	int	Dominion only.
    averageNodeNeutralizeAssist	int	Dominion only.
    averageNumDeaths	int	Dominion only.
    averageObjectivePlayerScore	int	Dominion only.
    averageTeamObjective	int	Dominion only.
    averageTotalPlayerScore	int	Dominion only.
    botGamesPlayed	int	
    killingSpree	int	
    maxAssists	int	Dominion only.
    maxChampionsKilled	int	
    maxCombatPlayerScore	int	Dominion only.
    maxLargestCriticalStrike	int	
    maxLargestKillingSpree	int	
    maxNodeCapture	int	Dominion only.
    maxNodeCaptureAssist	int	Dominion only.
    maxNodeNeutralize	int	Dominion only.
    maxNodeNeutralizeAssist	int	Dominion only.
    maxNumDeaths	int	Only returned for ranked statistics.
    maxObjectivePlayerScore	int	Dominion only.
    maxTeamObjective	int	Dominion only.
    maxTimePlayed	int	
    maxTimeSpentLiving	int	
    maxTotalPlayerScore	int	Dominion only.
    mostChampionKillsPerSession	int	
    mostSpellsCast	int	
    normalGamesPlayed	int	
    rankedPremadeGamesPlayed	int	
    rankedSoloGamesPlayed	int	
    totalAssists	int	
    totalChampionKills	int	
    totalDamageDealt	int	
    totalDamageTaken	int	
    totalDeathsPerSession	int	Only returned for ranked statistics.
    totalDoubleKills	int	
    totalFirstBlood	int	
    totalGoldEarned	int	
    totalHeal	int	
    totalMagicDamageDealt	int	
    totalMinionKills	int	
    totalNeutralMinionsKilled	int	
    totalNodeCapture	int	Dominion only.
    totalNodeNeutralize	int	Dominion only.
    totalPentaKills	int	
    totalPhysicalDamageDealt	int	
    totalQuadraKills	int	
    totalSessionsLost	int	
    totalSessionsPlayed	int	
    totalSessionsWon	int	
    totalTripleKills	int	
    totalTurretsKilled	int	
    totalUnrealKills	int


#####################################################################################################

class PlayerStatsSummaryListDto(models.Model):
    playerStatSummaries	List[PlayerStatsSummaryDto]	Collection of player stats summaries associated with the summoner.
    summonerId	long	Summoner ID.

class PlayerStatsSummaryDto(models.Model):
    aggregatedStats	AggregatedStatsDto	Aggregated stats.
    losses	int	Number of losses for this queue type. Returned for ranked queue types only.
    modifyDate	long	Date stats were last modified specified as epoch milliseconds.
    playerStatSummaryType	string	Player stats summary type. (Legal values: AramUnranked5x5, Ascension, CAP5x5, CoopVsAI, CoopVsAI3x3, CounterPick, FirstBlood1x1, FirstBlood2x2, Hexakill, KingPoro, NightmareBot, OdinUnranked, OneForAll5x5, RankedPremade3x3, RankedPremade5x5, RankedSolo5x5, RankedTeam3x3, RankedTeam5x5, SummonersRift6x6, Unranked, Unranked3x3, URF, URFBots, Bilgewater)
    wins	int	Number of wins for this queue type.

class AggregatedStatsDto(models.Model):
    averageAssists	int	Dominion only.
    averageChampionsKilled	int	Dominion only.
    averageCombatPlayerScore	int	Dominion only.
    averageNodeCapture	int	Dominion only.
    averageNodeCaptureAssist	int	Dominion only.
    averageNodeNeutralize	int	Dominion only.
    averageNodeNeutralizeAssist	int	Dominion only.
    averageNumDeaths	int	Dominion only.
    averageObjectivePlayerScore	int	Dominion only.
    averageTeamObjective	int	Dominion only.
    averageTotalPlayerScore	int	Dominion only.
    botGamesPlayed	int	
    killingSpree	int	
    maxAssists	int	Dominion only.
    maxChampionsKilled	int	
    maxCombatPlayerScore	int	Dominion only.
    maxLargestCriticalStrike	int	
    maxLargestKillingSpree	int	
    maxNodeCapture	int	Dominion only.
    maxNodeCaptureAssist	int	Dominion only.
    maxNodeNeutralize	int	Dominion only.
    maxNodeNeutralizeAssist	int	Dominion only.
    maxNumDeaths	int	Only returned for ranked statistics.
    maxObjectivePlayerScore	int	Dominion only.
    maxTeamObjective	int	Dominion only.
    maxTimePlayed	int	
    maxTimeSpentLiving	int	
    maxTotalPlayerScore	int	Dominion only.
    mostChampionKillsPerSession	int	
    mostSpellsCast	int	
    normalGamesPlayed	int	
    rankedPremadeGamesPlayed	int	
    rankedSoloGamesPlayed	int	
    totalAssists	int	
    totalChampionKills	int	
    totalDamageDealt	int	
    totalDamageTaken	int	
    totalDeathsPerSession	int	Only returned for ranked statistics.
    totalDoubleKills	int	
    totalFirstBlood	int	
    totalGoldEarned	int	
    totalHeal	int	
    totalMagicDamageDealt	int	
    totalMinionKills	int	
    totalNeutralMinionsKilled	int	
    totalNodeCapture	int	Dominion only.
    totalNodeNeutralize	int	Dominion only.
    totalPentaKills	int	
    totalPhysicalDamageDealt	int	
    totalQuadraKills	int	
    totalSessionsLost	int	
    totalSessionsPlayed	int	
    totalSessionsWon	int	
    totalTripleKills	int	
    totalTurretsKilled	int	
    totalUnrealKills	int

#####################################################################################################

class SummonerDto(models.Model):
    exId	long	Summoner ID.
    name	string	Summoner name.
    profileIconId	int	ID of the summoner icon associated with the summoner.
    revisionDate	long	Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change
    summonerLevel	long	Summoner level associated with the summoner.

#####################################################################################################

class MasteryPagesDto(models.Model):
    pages	Set[MasteryPageDto]	Collection of mastery pages associated with the summoner.
    summonerId	long	Summoner ID.

class MasteryPageDto(models.Model):
    current	boolean	Indicates if the mastery page is the current mastery page.
    exId	long	Mastery page ID.
    masteries	List[MasteryDto]	Collection of masteries associated with the mastery page.
    name	string	Mastery page name.

class MasteryDto(models.Model):
    exId	int	Mastery ID. For static information correlating to masteries, please refer to the LoL Static Data API.
    rank	int	Mastery rank (i.e., the number of points put into this mastery).
    
#####################################################################################################
#PARTE DE LA API SIN BASE DE DATOS.............GET /api/lol/{region}/v1.4/summoner/{summonerIds}/name
#####################################################################################################

class RunePagesDto(models.Model):
    pages	Set[RunePageDto]	Collection of rune pages associated with the summoner.
    summonerId	long	Summoner ID.

class RunePageDto(models.Model):
    current	boolean	Indicates if the page is the current page.
    exId	long	Rune page ID.
    name	string	Rune page name.
    slots	Set[RuneSlotDto]	Collection of rune slots associated with the rune page.

class RuneSlotDto(models.Model):
    runeId	int	Rune ID associated with the rune slot. For static information correlating to rune IDs, please refer to the LoL Static Data API.
    runeSlotId	int	Rune slot ID.
    
#####################################################################################################

class TeamDto(models.Model):
    createDate	long	Date that team was created specified as epoch milliseconds.
    fullId	string	
    lastGameDate	long	Date that last game played by team ended specified as epoch milliseconds.
    lastJoinDate	long	Date that last member joined specified as epoch milliseconds.
    lastJoinedRankedTeamQueueDate	long	Date that team last joined the ranked team queue specified as epoch milliseconds.
    matchHistory	List[MatchHistorySummaryDto]	
    modifyDate	long	Date that team was last modified specified as epoch milliseconds.
    name	string	
    roster	RosterDto	
    secondLastJoinDate	long	Date that second to last member joined specified as epoch milliseconds.
    status	string	
    tag	string	
    teamStatDetails	List[TeamStatDetailDto]	
    thirdLastJoinDate	long	Date that third to last member joined specified as epoch milliseconds.

class MatchHistorySummaryDto(models.Model):
    assists	int	
    date	long	Date that match was completed specified as epoch milliseconds.
    deaths	int	
    gameId	long	
    gameMode	string	
    invalid	boolean	
    kills	int	
    mapId	int	
    opposingTeamKills	int	
    opposingTeamName	string	
    win	boolean

class RosterDto(models.Model):
    memberList	List[TeamMemberInfoDto]	
    ownerId	long

class TeamStatDetailDto(models.Model):
    averageGamesPlayed	int	
    losses	int	
    teamStatType	string	
    wins	int

class TeamMemberInfoDto(models.Model):
    inviteDate	long	Date that team member was invited to team specified as epoch milliseconds.
    joinDate	long	Date that team member joined team specified as epoch milliseconds.
    playerId	long	
    status	string
    
#####################################################################################################

class TeamDto(models.Model):
    createDate	long	Date that team was created specified as epoch milliseconds.
    fullId	string	
    lastGameDate	long	Date that last game played by team ended specified as epoch milliseconds.
    lastJoinDate	long	Date that last member joined specified as epoch milliseconds.
    lastJoinedRankedTeamQueueDate	long	Date that team last joined the ranked team queue specified as epoch milliseconds.
    matchHistory	List[MatchHistorySummaryDto]	
    modifyDate	long	Date that team was last modified specified as epoch milliseconds.
    name	string	
    roster	RosterDto	
    secondLastJoinDate	long	Date that second to last member joined specified as epoch milliseconds.
    status	string	
    tag	string	
    teamStatDetails	List[TeamStatDetailDto]	
    thirdLastJoinDate	long	Date that third to last member joined specified as epoch milliseconds.

class MatchHistorySummaryDto(models.Model):
    assists	int	
    date	long	Date that match was completed specified as epoch milliseconds.
    deaths	int	
    gameId	long	
    gameMode	string	
    invalid	boolean	
    kills	int	
    mapId	int	
    opposingTeamKills	int	
    opposingTeamName	string	
    win	boolean

class RosterDto(models.Model):
    memberList	List[TeamMemberInfoDto]	
    ownerId	long

class TeamStatDetailDto(models.Model):
    averageGamesPlayed	int	
    losses	int	
    teamStatType	string	
    wins	int

class TeamMemberInfoDto(models.Model):
    inviteDate	long	Date that team member was invited to team specified as epoch milliseconds.
    joinDate	long	Date that team member joined team specified as epoch milliseconds.
    playerId	long	
    status	string
