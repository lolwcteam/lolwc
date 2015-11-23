from django.contrib import admin
from lol.models import SummonerInfo, MostPlayedChampInfo, SummonerProfile, History

admin.site.register(SummonerInfo)
admin.site.register(MostPlayedChampInfo)
admin.site.register(SummonerProfile)
admin.site.register(History)
# Register your models here.
