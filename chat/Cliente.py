import xmpp
import xmltodict
import time
import Friend
from collections import OrderedDict

class Cliente(object):
    #Generales
    state = None
    server = None
    user = None
    password = None
    connected = None
    connection = None
    roster = None
    #Contactos
    friends = []
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

    def __init__(self, user, password, server):
        self.user = user
        self.password = password
        self.setServer(server)
        connect = self.connect()
        if connect != "connect stablished":
            self.connected = False
            print(connect)
            exit()
        else:
            print(connect)
            self.connected = True
            

    def setServer(self, server):
        serverList = {"br":"br1",
                      "eune":"eun1",
                      "euw":"euw1",
                      "kr":"kr",
                      "lan":"la1",
                      "las":"la2",
                      "na":"na1",
                      "oce":"oc1",
                      "tr":"tr1",
                      "ru":"ru",
                      "pbe":"pbe1"}
        self.server = serverList[server]

    def connect(self):
        self.conn = xmpp.Client("pvp.net")
        if not self.conn.connect(server=("chat."+self.server+".lol.riotgames.com", 5223)):
            return "connect failed":
        if not self.conn.auth(self.user, "AIR_" + self.password, "xiff"):
            return "auth failed."
        conn.RegisterHandler("message", self.recvMessage)
        conn.sendInitPresence(requestRoster=1)
        self.roster = self.conn.getRoster()
        return "connect stablished"

    def sendReply(self, conn, msg, text):
        reply = msg.buildReply(text)
        reply.setType("chat")
        self.conn.send(reply)
    
    def presenceHandler(self, conn, presence):
        print("TODO")
    
    def messageHandler(self, conn, message):
        user = roster.getName(str(msg.getFrom()))
        text = msg.getBody()
        
    def iq_handler(self, conn, event):
        print("#----Iq----#")
        print(unicode(event))

    def disconnect_handler(self, conn, event):
        print("#----Desconectado----#")
        print(unicode(event))
    
    def addFriend(self, friendPresence):
        jid = friendPresence.getFrom().getStripped()
        statusRawXml = self.roster.getStatus(jid)
        statusChat = self.roster.getShow(jid)
        name = self.roster.getName(jid)
        if statusRaw != None:
            status = xmltodict.parse(statusRaw,encoding='utf-8')
            profileIcon = status["body"]["profileIcon"]
            level = status["body"]["level"]
            wins = status["body"]["wins"]
            leaves = status["body"]["leaves"]
            odinWins = status["body"]["odinWins"]
            odinLeaves = status["body"]["odinLeaves"]
            queueType = status["body"]["queueType"]
            rankedLosses = status["body"]["rankedLosses"]
            rankedRating = status["body"]["rankedRating"]
            tier = status["body"]["tier"]
            rankedSoloRestricted = status["body"]["rankedSoloRestricted"]
            championMasteryScore = status["body"]["championMasteryScore"]
            statusMsg = status["body"]["statusMsg"]
            rankedLeagueName = status["body"]["rankedLeagueName"]
            rankedLeagueDivision = status["body"]["rankedLeagueDivision"]
            rankedLeagueTier = status["body"]["rankedLeagueTier"]
            rankedLeagueQueue = status["body"]["rankedLeagueQueue"]
            rankedWins = status["body"]["rankedWins"]
            skinname = status["body"]["skinname"]
            gameQueueType = status["body"]["gameQueueType"]
            gameStatus = status["body"]["gameStatus"]
            timeStamp = status["body"]["timeStamp"]
            
            newFriend = Friend.Friend(jid, statusRawXml, statusChat, name, profileIcon, level, wins, leaves, odinWins, odinLeaves, queueType, rankedLosses, rankedRating, tier, rankedSoloRestricted, championMasteryScore, statusMsg, rankedLeagueName, rankedLeagueDivision, rankedLeagueTier, rankedLeagueQueue, rankedWins, skinname, gameQueueType, gameStatus, timeStamp)
            
            self.friends.append(newFriend)
            
    def removeFriend(self, friendJid):
        for i in range(len(self.friends)):
            if friends[i].jid == friendJid:
                self.friends.pop(i)
        
    def refreshStatus(self):
        statusUser = OrderedDict([(u'body', OrderedDict([(u'profileIcon', self.profileIcon), (u'level', self.level), (u'wins', self.wins), (u'leaves', self.leaves), (u'odinWins', self.odinWins), (u'odinLeaves', self.odinLeaves), (u'queueType', self.queueType), (u'rankedLosses', self.rankedLosses), (u'rankedRating', self.rankedRating), (u'tier', self.tier), (u'rankedSoloRestricted', self.rankedSoloRestricted), (u'championMasteryScore', self.championMasteryScore), (u'statusMsg', self.statusMsg), (u'rankedLeagueName', self.rankedLeagueName), (u'rankedLeagueDivision', self.rankedLeagueDivision), (u'rankedLeagueTier', self.rankedLeagueTier), (u'rankedLeagueQueue', self.rankedLeagueQueue), (u'rankedWins', self.rankedWins), (u'skinname', self.skinname), (u'gameQueueType', self.gameQueueType), (u'gameStatus', self.gameStatus), (u'timeStamp', self.timeStamp)]))])
        statusUserStr = xmltodict.unparse(statusUser)
        pres = xmpp.Presence()
        pres.setStatus(statusUserStr)
        conn.send(pres)
        
    def setRiotStatus():
        print("TODO")
        #get valores de rito
        #editStatus con esos valores
        #refreshStatus
        
    def editStatus(jid = None, statusRawXml = None, statusChat = None, name = None, profileIcon = None, level = None, wins = None, leaves = None, odinWins = None, odinLeaves = None, queueType = None, rankedLosses = None, rankedRating = None, tier = None, rankedSoloRestricted = None, championMasteryScore = None, statusMsg = None, rankedLeagueName = None, rankedLeagueDivision = None, rankedLeagueTier = None, rankedLeagueQueue = None, rankedWins = None, skinname = None, gameQueueType = None, gameStatus = None, timeStamp = None):
        print("TODO")
        #Va a tomar los atributos que se les pasen, los que sean diferentes de el valor anterior(no de diferentes de None) los va a actualizar, junto al statusRawXml