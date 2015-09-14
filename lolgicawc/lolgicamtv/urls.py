
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'lolgicamtv.views.home', name='home'),
]
