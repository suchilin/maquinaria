from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index' ),
    url(r'^perfil/$', perfil, name='perfil' ),
    url(r'^updateperfil/$', updateperfil, name='updateperfil' ),
    url(r'^unasolicitud/$', UnaSolicitud, name='unasolicitud' ),
    url(r'^unasolicitud/(?P<solicitud_id>\d+)/$', UnaSolicitud, name='unasolicitud' ),
    url(r'^add/$', add, name='add' ),
    url(r'^update/$', update, name='update' ),
    url(r'^ccdd/(?P<solicitud_id>\d+)/$', ccdd, name='ccdd' ),
    url(r'^centr/(?P<solicitud_id>\d+)/$', centr, name='centr' ),

)
