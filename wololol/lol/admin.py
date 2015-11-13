from django.contrib import admin
from lol.models import SummonerInfo, MostPlayedChampInfo, SummonerProfile

admin.site.register(SummonerInfo)
admin.site.register(MostPlayedChampInfo)
admin.site.register(SummonerProfile)
# Register your models here.
