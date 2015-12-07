
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^home/$', 'lol.views.home', name='searchHome'),

                       url(r'^$', 'lol.views.home', name='home'),
                       url(r'^profile/$', 'lol.views.profile', name='profile'),

                       url(r'^profile/(?P<region>[a-z]+)/id=(?P<idSum>[0-9]+)$', 'lol.views.profile', name='profileById'),
                       url(r'^profile/(?P<region>[a-z]+)/id=(?P<idSum>[0-9]+)/(?P<info>[a-z]+)$', 'lol.views.profile', name='profileInfoById'),
                       url(r'^profile/(?P<region>[a-z]+)/(?P<summoner>.+)$', 'lol.views.profile', name='profileByName'),
                       url(r'^profile/(?P<region>[a-z]+)/(?P<summoner>.+)/(?P<info>[a-z]+)$', 'lol.views.profile', name='profileInfoByName'),

                       url(r'^chat/$', 'lol.views.chat', name='chat'),
                       #url(r'^chat/(?P<region>[a-z]+)$', 'lol.views.chat', name='chat'),
                       url(r'^chat/(?P<region>[a-z]+)/(?P<user>.+)&(?P<password>.+)$', 'lol.views.chat', name='chatLogin'),
                       #url(r'^chat/(?P<region>[a-z]+)/(?P<friend>.+)$', 'lol.views.chat', name='chatToFriend'),

                       url(r'^data/$', 'lol.views.data', name='data'),
                       #url(r'^static/(?P<section>[a-z]+)$', 'lol.views.static', name='staticAll'),
                       #url(r'^static/(?P<section>[a-z]+)/(?P<specific>.+)$', 'lol.views.static', name='staticSpecific'),

                      )
