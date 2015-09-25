#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmpp
import xmltodict
import time
import threading
import Friend
from collections import OrderedDict

class Cliente(object):
    #Generales
    server = None#servidor
    user = None#usuario
    password = None#contraseña
    connected = None#True si esta conectado
    connection = None#El objeto xmpp de coneccion
    roster = "pato"#La lista de contactos
    #Contactos
    friends = []
    #Del roster
    jid = None #Jabber ID del conectado
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
            return "connect failed"
        if not self.conn.auth(self.user, "AIR_" + self.password, "xiff"):
            return "auth failed."      
        self.conn.sendInitPresence(requestRoster=1)
        self.roster = self.conn.getRoster()
        self.conn.RegisterHandler("message", self.messageHandler)
        self.conn.RegisterHandler("presence", self.presenceHandler)
        self.conn.RegisterHandler("iq", self.iqHandler)
        self.conn.RegisterDisconnectHandler(self.disconnectHandler)          
        listen = threading.Thread(target = self.listen, args = (self.conn,))
        keepAlive = threading.Thread(target = self.keepAlive, args = (self.conn,))
        listen.start()
        keepAlive.start()
        return "connect stablished"
    
    def listen(self, conn):
        userJid = self.jid
        while True:    
            try:
                
                cmd = raw_input("Ingrese contacto y mensaje para enviar\n>")
                cmd = cmd.split("-")
                msg = cmd[1]
                to = None
                for i in range(len(friends)):
                    if friends[i].name == cmd[0]:
                        to = friends[i].jid
                        print(to)
                if not to:
                    print("No se encontro el contacto")
                else:
                    print(to,msg)
                    message = xmpp.Message(to, msg)
                    message.setAttr('type', 'chat')
                    message.setAttr('from', userJid)
                    conn.send(message)
            except KeyboardInterrupt:
                print("#----LISTEN DETENIDO----#")
                break     
            
    def keepAlive(self, conn):
        while conn.isConnected():
            try:
                conn.Process(10)
                print("------------------------")
                friends = self.friends
                for i in range(len(friends)):
                    print("\tJid: "+unicode(friends[i].jid))
                    print("\tEstado de Chat: "+unicode(friends[i].statusChat))                
                    print("\tSummoner: "+unicode(friends[i].name))
                    print("\tIcono: "+unicode(friends[i].profileIcon))
                    print("\tLevel: "+unicode(friends[i].level))
                    print("\tVictorias: "+unicode(friends[i].wins))
                    print("\tAbandonos: "+unicode(friends[i].leaves))
                    print("\todinWins: "+unicode(friends[i].odinWins))
                    print("\todinLeaves: "+unicode(friends[i].odinLeaves))
                    print("\tqueueType: "+unicode(friends[i].queueType))
                    print("\trankedLosses: "+unicode(friends[i].rankedLosses))
                    print("\trankedRating: "+unicode(friends[i].rankedRating))
                    print("\ttier: "+unicode(friends[i].tier))
                    print("\trankedSoloRestricted: "+unicode(friends[i].rankedSoloRestricted))
                    print("\tChamp Score: "+unicode(friends[i].championMasteryScore))
                    print("\tMensaje: "+unicode(friends[i].statusMsg))
                    print("\tNombre de Liga: "+unicode(friends[i].rankedLeagueName))
                    print("\tDivision: "+unicode(friends[i].rankedLeagueDivision))
                    print("\tLiga: "+unicode(friends[i].rankedLeagueTier))
                    print("\tRanked League Queue: "+unicode(friends[i].rankedLeagueQueue))
                    print("\tVictorias en Ranked: "+unicode(friends[i].rankedWins))
                    print("\tJugando: "+unicode(friends[i].skinname))
                    print("\tGame Queue Type: "+unicode(friends[i].gameQueueType))
                    print("\tEstado: "+unicode(friends[i].gameStatus))
                    if friends[i].timestamp:
                        minutos = unicode((time.time() - float(friends[i].timestamp[0:10]+"."+friends[i].timestamp[10:13]))/60)+" minutos"
                    else:
                        minutos = "---"
                    print("\tDurante: "+ minutos + " > " + unicode(friends[i].timeStamp))
                    print("")             
                print("------------------------")
                print("Ingrese contacto y mensaje para enviar con un guion entre medio\n>")
            except KeyboardInterrupt:
                print("#----KEEPALIVE DETENIDO----#")            
                break
        
    def presenceHandler(self, conn, presence):#TODO
        print("#----Presence----#")
        print(unicode(presence))
        jid = presence.getFrom().getStripped()
        name = self.roster.getName(jid)
        friends = self.friends
        print("JID: "+unicode(jid))
        print("NAME:"+unicode(name))
        statusRaw = self.roster.getStatus(jid)
        chatStatus = self.roster.getShow(jid)
        pos = None
        if statusRaw != None:
            status = xmltodict.parse(statusRaw,encoding='utf-8')
            newFriend = False
            for i in range(len(friends)):
                if jid == friends[i]:
                    newFriend = False
                    pos = i
                else:
                    newFriend = True
                    
            if newFriend:
                addFriend(presence)
            else:
                #for i in range(len(friends)):
                    #if friends[i].jid == jid:
                        #pos = i
                friends[pos].jid = jid
                friends[pos].statusChat = chatStatus
                friends[pos].name = name
                if "profileIcon" in status["body"]:
                    friends[pos].profileIcon = status["body"]["profileIcon"]
                else:
                    friends[pos].profileIcon = None
                if "level" in status["body"]:
                    friends[pos].level =  status["body"]["level"]
                else:
                    friends[pos].level = None
                if "wins" in status["body"]:
                    friends[pos].wins = status["body"]["wins"]
                else:
                    friends[pos].wins = None
                if "leaves" in status["body"]:
                    friends[pos].leaves = status["body"]["leaves"]
                else:
                    friends[pos].leaves = None
                if "odinWins" in status["body"]:
                    friends[pos].odinWins =  status["body"]["odinWins"]
                else:
                    friends[pos].odinWins = None
                if "odinLeaves" in status["body"]:
                    friends[pos].odinLeaves = status["body"]["odinLeaves"]
                else:
                    friends[pos].odinLeaves = None    
                if "queueType" in status["body"]:
                    friends[pos].queueType = status["body"]["queueType"]
                else:
                    friends[pos].queueType = None
                if "rankedLosses" in status["body"]:
                    friends[pos].rankedLosses = status["body"]["rankedLosses"]
                else:
                    friends[pos].rankedLosses = None
                if "rankedRating" in status["body"]:
                    friends[pos].rankedRating = status["body"]["rankedRating"]
                else:
                    friends[pos].rankedRating = None     
                if "tier" in status["body"]:
                    friends[pos].tier = status["body"]["tier"]
                else:
                    friends[pos].tier = None
                if "rankedSoloRestricted" in status["body"]:
                    friends[pos].rankedSoloRestricted = status["body"]["rankedSoloRestricted"]
                else:
                    friends[pos].rankedSoloRestricted = None                    
                if "championMasteryScore" in status["body"]:
                    friends[pos].championMasteryScore = status["body"]["championMasteryScore"]
                else:
                    friends[pos].championMasteryScore = None   
                if "statusMsg" in status["body"]:
                    friends[pos].statusMsg = status["body"]["statusMsg"]
                else:
                    friends[pos].statusMsg = None    
                if "rankedLeagueName" in status["body"]:
                    friends[pos].rankedLeagueName = status["body"]["rankedLeagueName"]
                else:
                    friends[pos].rankedLeagueName = None    
                if "rankedLeagueDivision" in status["body"]:
                    friends[pos].rankedLeagueDivision = status["body"]["rankedLeagueDivision"]
                else:
                    friends[pos].rankedLeagueDivision = None    
                if "rankedLeagueTier" in status["body"]:
                    friends[pos].rankedLeagueTier = status["body"]["rankedLeagueTier"]
                else:
                    friends[pos].rankedLeagueTier = None    
                if "rankedLeagueQueue" in status["body"]:
                    friends[pos].rankedLeagueQueue = status["body"]["rankedLeagueQueue"]
                else:
                    friends[pos].rankedLeagueQueue = None    
                if "rankedWins" in status["body"]:
                    friends[pos].rankedWins = status["body"]["rankedWins"]
                else:
                    friends[pos].rankedWins = None    
                if "skinname" in status["body"]:
                    friends[pos].skinname = status["body"]["skinname"]
                else:
                    friends[pos].skinname = None    
                if "gameQueueType" in status["body"]:
                    friends[pos].gameQueueType = status["body"]["gameQueueType"]
                else:
                    friends[pos].gameQueueType = None
                if "gameStatus" in status["body"]:
                    friends[pos].gameStatus = status["body"]["gameStatus"]
                else:
                    friends[pos].gameStatus = None
                if "timeStamp" in status["body"]:
                    friends[pos].timeStamp = status["body"]["timeStamp"]
                else:
                    friends[pos].timeStamp = None

    def messageHandler(self, conn, message):#TODO
        user = self.roster.getName(str(msg.getFrom()))
        text = msg.getBody()
        print("["+user+"]"+" > "+text)

    def iqHandler(self, conn, event):#TODO
        print("#----Iq----#")
        print(unicode(event))

    def disconnectHandler(self, conn, event):#TODO
        print("#----Desconectado----#")
        print(unicode(event))

    def sendReply(self, conn, msg, text):
        reply = msg.buildReply(text)
        reply.setType("chat")
        self.conn.send(reply)

    def addFriend(self, friendPresence):
        jid = friendPresence.getFrom().getStripped()
        statusRawXml = self.roster.getStatus(jid)
        statusChat = self.roster.getShow(jid)
        name = self.roster.getName(jid)
        if statusRaw != None:
            status = xmltodict.parse(statusRaw, encoding='utf-8')
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

            newFriend = Friend.Friend(jid, statusChat, name, profileIcon, level, wins, leaves, odinWins, odinLeaves, queueType, rankedLosses, rankedRating, tier, rankedSoloRestricted, championMasteryScore, statusMsg, rankedLeagueName, rankedLeagueDivision, rankedLeagueTier, rankedLeagueQueue, rankedWins, skinname, gameQueueType, gameStatus, timeStamp)

            self.friends.append(newFriend)

    def removeFriend(self, friendJid):
        for i in range(len(self.friends)):
            if friends[i].jid == friendJid:
                self.friends.pop(i)

    def getStatusRawDict(self):
        statusUser = OrderedDict([(u'body', OrderedDict([(u'profileIcon', self.profileIcon), (u'level', self.level), (u'wins', self.wins), (u'leaves', self.leaves), (u'odinWins', self.odinWins), (u'odinLeaves', self.odinLeaves), (u'queueType', self.queueType), (u'rankedLosses', self.rankedLosses), (u'rankedRating', self.rankedRating), (u'tier', self.tier), (u'rankedSoloRestricted', self.rankedSoloRestricted), (u'championMasteryScore', self.championMasteryScore), (u'statusMsg', self.statusMsg), (u'rankedLeagueName', self.rankedLeagueName), (u'rankedLeagueDivision', self.rankedLeagueDivision), (u'rankedLeagueTier', self.rankedLeagueTier), (u'rankedLeagueQueue', self.rankedLeagueQueue), (u'rankedWins', self.rankedWins), (u'skinname', self.skinname), (u'gameQueueType', self.gameQueueType), (u'gameStatus', self.gameStatus), (u'timeStamp', self.timeStamp)]))])    
        return statusUser

    def getStatusRawXml(self):
        statusUserDict = getStatusRawDict()
        statusUserXml = xmltodict.unparse(statusUserDict)        
        return statusUserXml

    def refreshStatusFromProps(self):
        statusUserXml = getStatusRawXml()
        pres = xmpp.Presence()
        pres.setStatus(statusUserStr)
        conn.send(pres)

    def setRiotStatus():#TODO
        print("TODO")
        #get valores de rito
        #editStatus con esos valores
        #refreshStatus

    def editStatus(status):#Diccionario con los nuevos atributos a modificar#TODO
        keys = status.keys()
        values = status.values()
        statusDict = getStatusRawDict()
        for i in range(len(status)):
            statusDict["body"][keys[i]] = values[i]