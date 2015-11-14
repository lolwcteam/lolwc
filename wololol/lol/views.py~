 #Al quitar alguna linea al trabajar, transformenla en un comentario con 3 numerales
import json
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from riotwatcher import getApiSummoner, getCacheSummoner
#from ovejawatcher import getSummoner

#ReturnJSON: return HttpResponse(json.dumps(valores), content_type="application/json")


def profile(request, summoner = None, idSum = None, region = None, info = None):
    context = RequestContext(request)
    #si todo none, mostrar buscador
    #si server e id/summoner, pedir get cache summoner
    #si getCacheSummoner == None pedir api summoner
    #getApiSummoner y reemplazar las variables en el html
    # if request.method == "POST":
    #     print(summoner, idSum, region, info)
    #     info = getApiSummoner(summoner = summoner, idSum = idSum, region = region)
    #     return HttpResponse(json.dumps(info), content_type="application/json")
    info = getApiSummoner(summoner = 'Sad Jocker King', region = 'las')
    #info = getSummoner(summoner = 'Sad Jocker King', region = 'las')
    return render_to_response('profile.html', {"info":info}, context)

def chat(request, region = None, friend = None):
    print("#-----chat-----#")

def static(request, section = None, specific = None):
    print("#-----static-----#")

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)
