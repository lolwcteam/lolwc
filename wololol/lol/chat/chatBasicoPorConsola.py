#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmpp
import xmltodict
import time
from collections import OrderedDict
import threading

#pip install git+https://github.com/ArchipelProject/xmpppy
#se cree un objeto de coneccion con user y pass
#objetos con nombre, estado de coneccion y con historial de chat
conn = xmpp.Client("pvp.net")
server = "la2"
msg = False
user = "rayder38"
password = "caca123"

userJid = 'sum426174@pvp.net'
statusUser = OrderedDict([(u'body', OrderedDict([(u'profileIcon', u'612'), (u'level', u'30'), (u'wins', u'101'), (u'leaves', u'33'), (u'odinWins', u'0'), (u'odinLeaves', u'0'), (u'queueType', None), (u'rankedLosses', u'0'), (u'rankedRating', u'0'), (u'tier', u'DIAMOND'), (u'rankedSoloRestricted', u'false'), (u'championMasteryScore', u'967'), (u'statusMsg', u'FAFITA 2x1'), (u'rankedLeagueName', u"Tu mama en tanga's league"), (u'rankedLeagueDivision', u'XL'), (u'rankedLeagueTier', u'BRONZE'), (u'rankedLeagueQueue', u'RANKED_SOLO_5x5'), (u'rankedWins', u'9999'), (u'skinname', u'Riven'), (u'gameQueueType', u'NORMAL'), (u'gameStatus', u'inGame'), (u'timeStamp', u'1442268254517')]))])
statusUserStr = xmltodict.unparse(statusUser)

conectadosJid = []
conectadosRaw = []#Todo en xml de pechaso
conectadosName = []
conectadosChatEstado = []
conectadosEstado = []
conectadosChamp = []
conectadosTiempo = []
conectadosTipoDeCola = []
conectadosChampScore = []
conectadosRankedLeagueQueue = []
conectadosRankedWins = []
conectadosGameQueueType = []
conectadosIcono = []
conectadosMensaje = []
conectadosLevel = []
conectadosLiga = []
conectadosDivision = []
conectadosLigaNombre = []
conectadosVictorias = []
if not conn.connect(server=("chat."+server+".lol.riotgames.com", 5223)):
    print("connect failed.")
    exit()

if not conn.auth(user, "AIR_" + password, "xiff"):
    print ("auth failed.")
    exit()

roster = None

def message_handler(conn, msg):
    if unicode(msg) != "None":
        print("#----Message----#")
        print(unicode(msg))
        user = roster.getName(unicode(msg.getFrom()))
        text = msg.getBody()
        print ("["+user+"] "+"text")
        reply = msg.buildReply("[ECHO] %s" % (text))
        reply.setType("chat")
        conn.send(reply)

def presence_handler(conn, event):
    print("#----Presence----#")
    print(unicode(event))
    jid = event.getFrom().getStripped()
    name = roster.getName(jid)
    print("JID: "+unicode(jid))
    print("NAME:"+unicode(name))
    statusRaw = roster.getStatus(jid)
    chatStatus = roster.getShow(jid)
    if statusRaw != None:
        status = xmltodict.parse(statusRaw,encoding='utf-8')

        if not jid in conectadosJid:
            conectadosRaw.append(statusRaw)
            conectadosJid.append(jid)
            conectadosChatEstado.append(chatStatus)
            conectadosName.append(name)
            if "gameStatus" in status["body"]:
                conectadosEstado.append(status["body"]["gameStatus"])
            else:
                conectadosEstado.append(None)
            if "skinname" in status["body"]:
                conectadosChamp.append(status["body"]["skinname"])
            else:
                conectadosChamp.append(None)
            if "timeStamp" in status["body"]:
                conectadosTiempo.append(status["body"]["timeStamp"])
            else:
                conectadosTiempo.append(None)
            if "queueType" in status["body"]:
                conectadosTipoDeCola.append(status["body"]["queueType"])
            else:
                conectadosTipoDeCola.append(None)
            if "championMasteryScore" in status["body"]:
                conectadosChampScore.append(status["body"]["championMasteryScore"])
            else:
                conectadosChampScore.append(None)
            if "rankedLeagueQueue" in status["body"]:
                conectadosRankedLeagueQueue.append(status["body"]["rankedLeagueQueue"])
            else:
                conectadosRankedLeagueQueue.append(None)
            if "rankedWins" in status["body"]:
                conectadosRankedWins.append(status["body"]["rankedWins"])
            else:
                conectadosRankedWins.append(None)
            if "gameQueueType" in status["body"]:
                conectadosGameQueueType.append(status["body"]["gameQueueType"])
            else:
                conectadosGameQueueType.append(None)
            if "profileIcon" in status["body"]:
                conectadosIcono.append(status["body"]["profileIcon"])
            else:
                conectadosIcono.append(None)
            if "statusMsg" in status["body"]:
                conectadosMensaje.append(status["body"]["statusMsg"])
            else:
                conectadosMensaje.append(None)
            if "level" in status["body"]:
                conectadosLevel.append(status["body"]["level"])
            else:
                conectadosLevel.append(None)
            if "rankedLeagueTier" in status["body"]:
                conectadosLiga.append(status["body"]["rankedLeagueTier"])
            else:
                conectadosLiga.append(None)
            if "rankedLeagueDivision" in status["body"]:
                conectadosDivision.append(status["body"]["rankedLeagueDivision"])
            else:
                conectadosDivision.append(None)
            if "rankedLeagueName" in status["body"]:
                conectadosLigaNombre.append(status["body"]["rankedLeagueName"])
            else:
                conectadosLigaNombre.append(None)
            if "wins" in status["body"]:
                conectadosVictorias.append(status["body"]["wins"])
            else:
                conectadosVictorias.append(None)
        else:
            pos = conectadosJid.index(jid)
            conectadosRaw[pos] = statusRaw
            conectadosJid[pos] = jid
            conectadosChatEstado[pos] = chatStatus
            conectadosName[pos] = name
            if "gameStatus" in status["body"]:
                conectadosEstado[pos] = status["body"]["gameStatus"]
            else:
                conectadosEstado[pos] = None
            if "skinname" in status["body"]:
                conectadosChamp[pos] = status["body"]["skinname"]
            else:
                conectadosChamp[pos] = None
            if "timeStamp" in status["body"]:
                conectadosTiempo[pos] = status["body"]["timeStamp"]
            else:
                conectadosTiempo[pos] = None
            if "queueType" in status["body"]:
                conectadosTipoDeCola[pos] = status["body"]["queueType"]
            else:
                conectadosTipoDeCola[pos] = None
            if "championMasteryScore" in status["body"]:
                conectadosChampScore[pos] = status["body"]["championMasteryScore"]
            else:
                conectadosChampScore[pos] = None
            if "rankedLeagueQueue" in status["body"]:
                conectadosRankedLeagueQueue[pos] = status["body"]["rankedLeagueQueue"]
            else:
                conectadosRankedLeagueQueue[pos] = None
            if "rankedWins" in status["body"]:
                conectadosRankedWins[pos] = status["body"]["rankedWins"]
            else:
                conectadosRankedWins[pos] = None
            if "gameQueueType" in status["body"]:
                conectadosGameQueueType[pos] = status["body"]["gameQueueType"]
            else:
                conectadosGameQueueType[pos] = None
            if "profileIcon" in status["body"]:
                conectadosIcono[pos] = status["body"]["profileIcon"]
            else:
                conectadosIcono[pos] = None
            if "statusMsg" in status["body"]:
                conectadosMensaje[pos] = status["body"]["statusMsg"]
            else:
                conectadosMensaje[pos] = None
            if "level" in status["body"]:
                conectadosLevel[pos] =  status["body"]["level"]
            else:
                conectadosLevel[pos] = None
            if "rankedLeagueTier" in status["body"]:
                conectadosLiga[pos] = status["body"]["rankedLeagueTier"]
            else:
                conectadosLiga[pos] = None
            if "rankedLeagueDivision" in status["body"]:
                conectadosDivision[pos] = status["body"]["rankedLeagueDivision"]
            else:
                conectadosDivision[pos] = None
            if "rankedLeagueName" in status["body"]:
                conectadosLigaNombre[pos] = status["body"]["rankedLeagueName"]
            else:
                conectadosLigaNombre[pos] = None
            if "wins" in status["body"]:
                conectadosVictorias[pos] = status["body"]["wins"]
            else:
                conectadosVictorias[pos] = None
            #except:
                #print()
                #conectadosJid.pop(pos)
                #conectadosEstado.pop(pos)
                #conectadosChamp.pop(pos)
                #conectadosTiempo.pop(pos)
                #conectadosTipoDeCola.pop(pos)
                #conectadosChampScore.pop(pos)
                #conectadosRankedLeagueQueue.pop(pos)
                #conectadosRankedWins.pop(pos)
                #conectadosGameQueueType.pop(pos)
                #conectadosIcono.pop(pos)
                #conectadosMensaje.pop(pos)
                #conectadosLevel.pop(pos)
                #conectadosLiga.pop(pos)
                #conectadosDivision.pop(pos)
                #conectadosLigaNombre.pop(pos)
                #conectadosVictorias.pop(pos)

def iq_handler(conn, event):
    print("#----Iq----#")
    print(unicode(event))

def disconnect_handler(conn, event):
    print("#----Desconectado----#")

roster = conn.getRoster()
conn.RegisterHandler("message", message_handler)
conn.RegisterHandler("presence", presence_handler)
conn.RegisterHandler("iq", iq_handler)
conn.RegisterDisconnectHandler(disconnect_handler)
pres = xmpp.Presence()
pres.setStatus(statusUserStr)
conn.send(pres)
#conn.sendInitPresence(requestRoster=1)

def worker(conn):
    global userJid
    while True:
        try:

            cmd = raw_input("Ingrese contacto y mensaje para enviar\n>")
            cmd = cmd.split("-")
            msg = cmd[1]
            to = None
            for i in range(len(conectadosJid)):
                if conectadosName[i] == cmd[0]:
                    to = conectadosJid[i]
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
            print("#----ERROR DE WORKER----#")
            break
t = threading.Thread(target=worker, args=(conn,))
t.start()

while conn.isConnected():
    try:
        conn.Process(10)
        print("------------------------")
        for i in range(len(conectadosJid)):
            print("\tJid: "+unicode(conectadosJid[i]))
            print("\tSummoner: "+unicode(conectadosName[i]))
            print("\tEstado de Chat: "+unicode(conectadosChatEstado[i]))
            print("\tEstado: "+unicode(conectadosEstado[i]))
            print("\tJugando: "+unicode(conectadosChamp[i]))
            print("\tTipo de Cola: "+unicode(conectadosTipoDeCola[i]))
            print("\tChamp Score: "+unicode(conectadosChampScore[i]))
            print("\tRanked League Queue: "+unicode(conectadosRankedLeagueQueue[i]))
            print("\tVictorias en Ranked: "+unicode(conectadosRankedWins[i]))
            print("\tGame Queue Type: "+unicode(conectadosGameQueueType[i]))
            if conectadosTiempo[i]:
                minutos = unicode((time.time() - float(conectadosTiempo[i][0:10]+"."+conectadosTiempo[i][10:13]))/60)+" minutos"
            else:
                minutos = "---"

            print("\tDurante: "+ minutos + " > " + unicode(conectadosTiempo[i]))
            print("\tIcono: "+unicode(conectadosIcono[i]))
            print("\tMensaje: "+unicode(conectadosMensaje[i]))
            print("\tLevel: "+unicode(conectadosLevel[i]))
            print("\tLiga: "+unicode(conectadosLiga[i]))
            print("\tDivision: "+unicode(conectadosDivision[i]))
            print("\tNombre de Liga: "+unicode(conectadosLigaNombre[i]))
            print("\tVictorias: "+unicode(conectadosVictorias[i]))
            print("")
        print("------------------------")
        print("Ingrese contacto y mensaje para enviar con un guion entre medio\n>")
    except KeyboardInterrupt:
        break
