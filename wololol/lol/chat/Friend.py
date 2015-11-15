#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Friend(object):
    #Del roster
    jid = None #Jabber ID del conectado
    statusChat = None #chat, dnd (do not disturb) y away
    name = None #Nombre de invocador
    #De roster.getStatus()
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

    def __init__(self, jid, statusChat, name, profileIcon, level, wins, leaves, odinWins, odinLeaves, queueType, rankedLosses, rankedRating, tier, rankedSoloRestricted, championMasteryScore, statusMsg, rankedLeagueName, rankedLeagueDivision, rankedLeagueTier, rankedLeagueQueue, rankedWins, skinname, gameQueueType, gameStatus, timeStamp):
        self.jid = jid
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



    #jid
    #statusChat
    #name

    #profileIcon
    #level
    #wins
    #leaves
    #odinWins
    #odinLeaves
    #queueType
    #rankedLosses
    #rankedRating
    #tier
    #rankedSoloRestricted
    #championMasteryScore
    #statusMsg
    #rankedLeagueName
    #rankedLeagueDivision
    #rankedLeagueTier
    #rankedLeagueQueue
    #rankedWins
    #skinname
    #gameQueueType
    #gameStatus
    #timeStamp
