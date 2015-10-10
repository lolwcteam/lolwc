
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),

                       url(r'^profile/(?P<region>[a-z]+)/(?P<summoner>.+)$', 'lolProfile.views.profile', name='profileByName'),
                       url(r'^profile/(?P<region>[a-z]+)/(?P<summoner>.+)/(?P<info>[a-z]+)$', 'lolProfile.views.profile', name='profileInfoByName'),
                       url(r'^profile/(?P<region>[a-z]+)/id=(?P<idSum>[0-9]+)$', 'lolProfile.views.profile', name='profileById'),
                       url(r'^profile/(?P<region>[a-z]+)/id=(?P<idSum>[0-9]+)/(?P<info>[a-z]+)$', 'lolProfile.views.profile', name='profileInfoById'),

                       url(r'^chat/(?P<region>[a-z]+)$', 'lolProfile.views.chat', name='chat'),
                       url(r'^chat/(?P<region>[a-z]+)/(?P<friend>.+)$', 'lolProfile.views.chat', name='chatToFriend'),

                       url(r'^static/$', 'lolProfile.views.static', name='static'),
                       url(r'^static/(?P<section>[a-z]+)$', 'lolProfile.views.static', name='staticAll'),
                       url(r'^static/(?P<section>[a-z]+)/(?P<specific>.+)$', 'lolProfile.views.static', name='staticSpecific'),

                      )
