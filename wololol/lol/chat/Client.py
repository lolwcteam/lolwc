#!/usr/bin/env python
# -*- coding: utf-8 -*-
#TODO que detecte a usuarios conectados por clientes no oficiales como pidgin
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
    keepAliveV = None
    roster = None#La lista de contactos
    #Contactos
    friends = None
    #Buzon
    buzon = None#Lista de mensajes sin leer
    #Del roster
    jid = None #Jabber ID del conectado
    statusChat = None #chat, dnd (do not disturb) y away
    name = None#Nombre de invocador
    #De roster.getStatus()
    profileIcon = None#Número de icono de invocado
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
            self.close(connect)
        else:
            self.connected = True

    def __str__(self):
        return self.name

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
        #self.conn = xmpp.Client("pvp.net",debug=[])
        self.conn = xmpp.Client("pvp.net")
        if not self.conn.connect(server=("chat."+self.server+".lol.riotgames.com", 5223)):
            return "connect failed"
        if not self.conn.auth(self.user, "AIR_" + self.password, "xiff"):
            return "auth failed."
        self.conn.RegisterHandler("iq", self.iqHandler)
        self.conn.sendInitPresence(requestRoster=1)
        self.roster = self.conn.getRoster()
        self.conn.RegisterHandler("message", self.messageHandler)
        self.conn.RegisterHandler("presence", self.presenceHandler)
        self.conn.RegisterDisconnectHandler(self.disconnectHandler)
        self.refreshStatusFromProps()
        self.jid = self.conn.User
        self.statusChat = "chat"
        self.name = self.conn.Summoner
        self.keepAliveV = threading.Thread(target = self.keepAlive, args = (self.conn,))
        self.keepAliveV.start()
        return "connect stablished"

    def send(self, to, msg):
        #to es la id de a quien se quiere enviar
        to = "sum"+str(to)+"@pvp.net"
        if not to:
            print("No se encontro el contacto")
            return False
        else:
            userJid = self.jid
            message = xmpp.Message(to, msg)
            message.setAttr('type', 'chat')
            message.setAttr('from', str(userJid)+"@pvp.net")
            self.conn.send(message)
            return True

    def getIdFromJid(self, jid):
        ide = self.jid.split("sum")[-1].split("@pvp.net")[0]
        return unicode(ide)

    def getAll(self):
        friends = [None]*len(self.friends)
        for i in range(len(self.friends)):
            friends[i] = {
                "id":unicode(self.getIdFromJid(self.friends[i].jid)),
                "statusChat":unicode(self.friends[i].statusChat),
                "name":unicode(self.friends[i].name),
                "profileIcon":unicode(self.friends[i].profileIcon),
                "level":unicode(self.friends[i].level),
                "championMasteryScore":unicode(self.friends[i].championMasteryScore),
                "statusMsg":unicode(self.friends[i].statusMsg),
                "rankedLeagueName":unicode(self.friends[i].rankedLeagueName),
                "rankedLeagueDivision":unicode(self.friends[i].rankedLeagueDivision),
                "rankedLeagueTier":unicode(self.friends[i].rankedLeagueTier),
                "skinname":unicode(self.friends[i].skinname),
                "gameQueueType":unicode(self.friends[i].gameQueueType),
                "gameStatus":unicode(self.friends[i].gameStatus),
                "timeStamp":unicode(self.friends[i].timeStamp),
            }

        info = {
            "user":{
                "id":unicode(self.getIdFromJid(self.jid)),
                "statusChat":unicode(self.statusChat),
                "name":unicode(self.name),
                "profileIcon":unicode(self.profileIcon),
                "level":unicode(self.level),
                "championMasteryScore":unicode(self.championMasteryScore),
                "statusMsg":unicode(self.statusMsg),
                "rankedLeagueName":unicode(self.rankedLeagueName),
                "rankedLeagueDivision":unicode(self.rankedLeagueDivision),
                "rankedLeagueTier":unicode(self.rankedLeagueTier),
            },
            "friends":friends
        }
        return info

    def printAll(self):
        #print("------------------------")
        #print("My JID:" + unicode(self.jid))
        #print("My Status:" + unicode(self.statusChat))
        #print("My Name:" + unicode(self.name))
        #print("Buzon:"+ unicode(self.buzon))
        print("thread>"+unicode(self.keepAliveV.name)+"\tjid>"+unicode(self.jid)+"\testado>"+unicode(self.statusChat)+"\tname>"+unicode(self.name)+"\tbuzon>"+unicode(self.buzon))
        #friends = self.friends
        #for i in range(len(friends)):
        #    print("\tJid: "+unicode(friends[i].jid))
        #    print("\tEstado de Chat: "+unicode(friends[i].statusChat))
        #    print("\tSummoner: "+unicode(friends[i].name))
            #print("\tIcono: "+unicode(friends[i].profileIcon))
            #print("\tLevel: "+unicode(friends[i].level))
            #print("\tVictorias: "+unicode(friends[i].wins))
            #print("\tAbandonos: "+unicode(friends[i].leaves))
            #print("\todinWins: "+unicode(friends[i].odinWins))
            #print("\todinLeaves: "+unicode(friends[i].odinLeaves))
            #print("\tqueueType: "+unicode(friends[i].queueType))
            #print("\trankedLosses: "+unicode(friends[i].rankedLosses))
            #print("\trankedRating: "+unicode(friends[i].rankedRating))
            #print("\ttier: "+unicode(friends[i].tier))
            #print("\trankedSoloRestricted: "+unicode(friends[i].rankedSoloRestricted))
            #print("\tChamp Score: "+unicode(friends[i].championMasteryScore))
            #print("\tMensaje: "+unicode(friends[i].statusMsg))
            #print("\tNombre de Liga: "+unicode(friends[i].rankedLeagueName))
            #print("\tDivision: "+unicode(friends[i].rankedLeagueDivision))
            #print("\tLiga: "+unicode(friends[i].rankedLeagueTier))
            #print("\tRanked League Queue: "+unicode(friends[i].rankedLeagueQueue))
            #print("\tVictorias en Ranked: "+unicode(friends[i].rankedWins))
            #print("\tJugando: "+unicode(friends[i].skinname))
            #print("\tGame Queue Type: "+unicode(friends[i].gameQueueType))
            #print("\tEstado: "+unicode(friends[i].gameStatus))
            #if friends[i].timeStamp:
            #    minutos = unicode((time.time() - float(friends[i].timeStamp[0:10]+"."+friends[i].timeStamp[10:13]))/60)+" minutos"
            #else:
            #    minutos = "---"
            #print("\tDurante: "+ minutos + " > " + unicode(friends[i].timeStamp))
            #print("")
        #print("------------------------")

    def keepAlive(self, conn):
        while conn.isConnected():
            try:
                conn.Process(10)
                #self.printAll()
            except KeyboardInterrupt:
                print("#----KEEPALIVE DETENIDO----#")
                exit()
                break

    def close(self, why="Sin Motivo Aparente"):
        print("#----CLOSE> "+why+"----#")
        self.conn.sendPresence(jid=str(self.jid)+"pvp.net", typ="unavaible", requestRoster=0)
        self.conn.connected = False

    def presenceHandler(self, conn, presence):
        #print("#----Presence----#")
        #print(unicode(presence))
        jid = presence.getFrom().getStripped().split("@")[0]
        fulljid = presence.getFrom().getStripped()
        name = self.roster.getName(fulljid)
        if self.friends == None:
            self.friends = []
        friends = self.friends
        statusRaw = self.roster.getStatus(fulljid)
        chatStatus = self.roster.getShow(fulljid)
        priority = self.roster.getPriority(fulljid)
        pos = None
        #TODO si el usuario tiene una solicitud pendiente el jid se cambia por el de la solicitud (esta es una presence vacia con type="subscribe") agregar a este if la condicion si se encuentra
        if self.getIdFromJid(self.jid) != self.getIdFromJid(jid):
            if statusRaw != None:
                status = xmltodict.parse(unicode(statusRaw),encoding='utf-8')
                newFriend = False
            else:
                status = {"body":{}}
            if len(friends) != 0:
                for i in range(len(friends)):
                    if jid == friends[i].jid:
                        newFriend = False
                        pos = i
                        break
                    else:
                        newFriend = True
            else:
                newFriend = True
            if newFriend:
                self.addFriend(presence)
            else:
                friends[pos].jid = jid
                friends[pos].statusChat = chatStatus
                if chatStatus == None or chatStatus == "None":
                    self.removeFriend(jid)
                    return
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

    def messageHandler(self, conn, msg):
        print("#----Message----#")
        if self.getIdFromJid(msg.getTo()) == self.getIdFromJid(self.jid):
            user = self.roster.getName(str(msg.getFrom()))
            text = msg.getBody()
            if text != None:
                if self.buzon == None:
                    self.buzon = []
                self.buzon.append((user, text))

    def cleanBuzon(self):
        self.buzon = []

    def iqHandler(self, conn, event):#TODO
        return
        #print("#----Iq----#")
        #print(unicode(event))

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
        if statusRawXml != None:
            profileIcon = None
            level = None
            wins = None
            leaves = None
            odinWins = None
            odinLeaves = None
            queueType= None
            rankedLosses = None
            rankedRating = None
            tier = None
            rankedSoloRestricted = None
            championMasteryScore = None
            statusMsg = None
            rankedLeagueName = None
            rankedLeagueDivision = None
            rankedLeagueTier = None
            rankedLeagueQueue = None
            rankedWins = None
            skinname = None
            gameQueueType = None
            gameStatus = None
            timeStamp = None
            status = xmltodict.parse(statusRawXml, encoding='utf-8')
            if "profileIcon" in status["body"]:
                profileIcon = status["body"]["profileIcon"]
            if "level" in status["body"]:
                level = status["body"]["level"]
            if "wins" in status["body"]:
                wins = status["body"]["wins"]
            if "leaves" in status["body"]:
                leaves = status["body"]["leaves"]
            if "odinWins" in status["body"]:
                odinWins = status["body"]["odinWins"]
            if "odinLeaves" in status["body"]:
                odinLeaves = status["body"]["odinLeaves"]
            if "queueType" in status["body"]:
                queueType = status["body"]["queueType"]
            if "rankedLosses" in status["body"]:
                rankedLosses = status["body"]["rankedLosses"]
            if "rankedRating" in status["body"]:
                rankedRating = status["body"]["rankedRating"]
            if "tier" in status["body"]:
                tier = status["body"]["tier"]
            if "rankedSoloRestricted" in status["body"]:
                rankedSoloRestricted = status["body"]["rankedSoloRestricted"]
            if "championMasteryScore" in status["body"]:
                championMasteryScore = status["body"]["championMasteryScore"]
            if "statusMsg" in status["body"]:
                statusMsg = status["body"]["statusMsg"]
            if "rankedLeagueName" in status["body"]:
                rankedLeagueName = status["body"]["rankedLeagueName"]
            if "rankedLeagueDivision" in status["body"]:
                rankedLeagueDivision = status["body"]["rankedLeagueDivision"]
            if "rankedLeagueTier" in status["body"]:
                rankedLeagueTier = status["body"]["rankedLeagueTier"]
            if "rankedLeagueQueue" in status["body"]:
                rankedLeagueQueue = status["body"]["rankedLeagueQueue"]
            if "rankedWins" in status["body"]:
                rankedWins = status["body"]["rankedWins"]
            if "skinname" in status["body"]:
                skinname = status["body"]["skinname"]
            if "gameQueueType" in status["body"]:
                gameQueueType = status["body"]["gameQueueType"]
            if "gameStatus" in status["body"]:
                gameStatus = status["body"]["gameStatus"]
            if "timeStamp" in status["body"]:
                timeStamp = status["body"]["timeStamp"]
            newFriend = Friend.Friend(jid, statusChat, name, profileIcon, level, wins, leaves, odinWins, odinLeaves, queueType, rankedLosses, rankedRating, tier, rankedSoloRestricted, championMasteryScore, statusMsg, rankedLeagueName, rankedLeagueDivision, rankedLeagueTier, rankedLeagueQueue, rankedWins, skinname, gameQueueType, gameStatus, timeStamp)
            self.friends.append(newFriend)

    def removeFriend(self, friendJid):

        for i in range(len(self.friends)):
            if self.friends[i].jid == friendJid:
                self.friends.pop(i)
                break

    def getStatusRawDict(self):
        statusUser = OrderedDict([(u'body', OrderedDict([
         (u'profileIcon', unicode(self.profileIcon)),
         (u'level', unicode(self.level)),
         (u'wins', unicode(self.wins)),
         (u'leaves', unicode(self.leaves)),
         (u'odinWins', unicode(self.odinWins)),
         (u'odinLeaves', unicode(self.odinLeaves)),
         (u'queueType', unicode(self.queueType)),
         (u'rankedLosses', unicode(self.rankedLosses)),
         (u'rankedRating', unicode(self.rankedRating)),
         (u'tier', unicode(self.tier)),
         (u'rankedSoloRestricted', unicode(self.rankedSoloRestricted)),
         (u'championMasteryScore', unicode(self.championMasteryScore)),
         (u'statusMsg', unicode(self.statusMsg)),
         (u'rankedLeagueName', unicode(self.rankedLeagueName)),
         (u'rankedLeagueDivision', unicode(self.rankedLeagueDivision)),
         (u'rankedLeagueTier', unicode(self.rankedLeagueTier)),
         (u'rankedLeagueQueue', unicode(self.rankedLeagueQueue)),
         (u'rankedWins', unicode(self.rankedWins)),
         (u'skinname', unicode(self.skinname)),
         (u'gameQueueType', unicode(self.gameQueueType)),
         (u'gameStatus', unicode(self.gameStatus)),
         (u'timeStamp', unicode(self.timeStamp))
         ]))])
        return statusUser

    def getStatusRawXml(self):
        statusUserDict = self.getStatusRawDict()
        statusUserXml = xmltodict.unparse(statusUserDict)
        return statusUserXml

    def refreshStatusFromProps(self):
        statusUserXml = self.getStatusRawXml()
        pres = xmpp.Presence()
        pres.setStatus(statusUserXml)
        self.conn.send(pres)

    def setRiotStatus():#TODO
        print("TODO")
        #get valores de rito
        #editStatus con esos valores
        #refreshStatus
    def setTier(self):
        self.tier = "pataso"
