#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from ovejawatcherFinal import getSummoner, refreshSummoner
from chat import Cliente
#ReturnJSON: return HttpResponse(json.dumps(valores), content_type="application/json")

clientes = []

def profile(request, summoner = None, idSum = None, region = None, info = None):
    context = RequestContext(request)
    info = getSummoner(summoner = summoner, region = region)
    return render_to_response('profile.html', {"info":info}, context)

def chat(request, user = None, password = None, region = None, friend = None):
    context = RequestContext(request)
    global clientes
    if request.method == "POST":
        if "message" in request.POST:
            if request.POST["message"] == "ready":
                for i in clientes:
                    if i.getIdFromJid(i.jid) == request.POST["id"]:
                        info = i.getAll()
                        #TODO que funcione ingresando user y pass por link
                        return HttpResponse(json.dumps(info), content_type="application/json")
            # if request.POST["message"] == "statusMsg":
            # if request.POST["message"] == "statusMsg":
            # if request.POST["message"] == "statusMsg":
            # if request.POST["message"] == "statusMsg":
        else:
            region = request.POST["server"]
            user = request.POST["user"]
            password = request.POST["password"]

    if user != None and password != None and region != None:
        cliente = Cliente(user, password, region)
        if cliente.connected:
            for i in range(len(clientes)):
                if clientes[i].jid == cliente.jid:
                    clientes.pop(i)
                    break
            clientes.append(cliente)
            info={
                #TODO returnear serverStatus
                "message":"<h1 class='green-text'>Conectando a "+cliente.name+"...</h1><p class='center white-text'>Espere mientras se conecta al servidor de Riot Games</p>",
                "typ":"loginCorrect",
                "name":unicode(cliente.name),
                "id":str(cliente.getIdFromJid(cliente.jid)),
                "profileIcon":str(cliente.profileIcon),
                "level":str(cliente.level),
                "league":str(cliente.rankedLeagueTier).capitalize() + " " + str(cliente.rankedLeagueDivision),
                "promo":str(cliente.rankedLeagueName),
                "score":str(cliente.championMasteryScore),
                "statusMsg":unicode(cliente.statusMsg)
                }

            if request.method == "POST":
                return HttpResponse(json.dumps(info), content_type="application/json")
            return render_to_response('chat.html', {"info":info}, context)

        else:
            info={
                #TODO returnear serverStatus
                "message":"<h1 class='red-text'>No fue posible conectarse</h1><p class='center red-text'>Revisa tu usario y contraseña</p>",
                "typ":"authError",
                }
            if request.method == "POST":
                return HttpResponse(json.dumps(info), content_type="application/json")
            return render_to_response('chat.html', {"info":info}, context)
    else:
        return render_to_response('chat.html', context)

#TODO cambiar nombre static
def data(request, section = None, specific = None):
    context = RequestContext(request)
    return render_to_response('underConstruction.html', context)

def home(request):
    context = RequestContext(request)
    from random import randint
    import os
    amount = len(os.listdir("./lol/static/img/home"))
    image = randint(1,amount)
    return render_to_response('home.html',{"homeImage":str(image)}, context)
