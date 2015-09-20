class Friend(object):
    #Del roster
    jid = None #Jabber ID del conectado
    statusRawXml = None #El status en xml directo
    statusChat = None #chat, dnd (do not disturb) y away
    name = None #Nombre de invocador
    #De roster.getStatus()
    profileIcon = None #Número de icono de invocado
    level = None #Level
    wins = None #?Victorias en general (de normal, ranked, todo?)    
    leaves = None #Cantidad de abandonos
    odinWins = None #?Cantidad de victorias en Odin? 3v3?
    odinLeaves = None #?Cantidad de abandonos en Odin
    queueType= None #?INDEFINIDO siempre da None
    rankedLosses = None #?INDEFINIDO siempre da 0
    rankedRating = None #?INDEFINIDO siempre da 0
    tier = None #?Alguna liga quizás la del elo más alto (DIAMOND, BRONZE, etc)
    rankedSoloRestricted = None #?INDEFINIDO generalmente false
    championMasteryScore = None #Mastery Champ Score
    statusMsg = None #Mensaje de estado
    rankedLeagueName = None #Nombre de la liga, Leona Urfriders, etc
    rankedLeagueDivision = None #Division de la anterior I, IV, V
    rankedLeagueTier = None #Liga solo queue, BRONZE, GOLD
    rankedLeagueQueue = None #? suele decir RANKED_SOLO_5x5
    rankedWins = None #Victorias en ranked
    skinname = None #si inGame, el champ jugado
    gameQueueType = None #?Generalmente dice NORMAL
    gameStatus = None #inGame, outOfGame, champSelect, hostingNormalGame
    timeStamp = None #?si inGame, timestamp de cuando empezo, si no INDEFINIDO
    
    def __init__(self, jid, statusRawXml, statusChat, name, profileIcon, level, wins, leaves, odinWins, odinLeaves, queueType, rankedLosses, rankedRating, tier, rankedSoloRestricted, championMasteryScore, statusMsg, rankedLeagueName, rankedLeagueDivision, rankedLeagueTier, rankedLeagueQueue, rankedWins, skinname, gameQueueType, gameStatus, timeStamp):
        self.jid = jid
        self.statusRawXml = statusRawXml
        self.statusChat = statusChat
        self.name = name
        self.profileIcon = profileIcon
        self.level = level
        self.wins = wins
        self.leaves = leaves
        self.odinWins = odinWins
        self.odinLeaves = odinLeaves
        self.queueType = queueType
        self.rankedLosses = rankedLosses
        self.rankedRating = rankedRating
        self.tier = tier
        self.rankedSoloRestricted = rankedSoloRestricted
        self.championMasteryScore = championMasteryScore
        self.statusMsg = statusMsg
        self.rankedLeagueName = rankedLeagueName
        self.rankedLeagueDivision = rankedLeagueDivision
        self.rankedLeagueTier = rankedLeagueTier
        self.rankedLeagueQueue = rankedLeagueQueue
        self.rankedWins = rankedWins
        self.skinname = skinname
        self.gameQueueType = gameQueueType
        self.gameStatus = gameStatus
        self.timeStamp = timeStamp