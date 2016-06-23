from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^', include('solicitudes.urls', namespace='solicitudes')),
    (r'^idetec/accounts/', include('registration.backends.default.urls')),
    url(r'^idetec/grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^idetec/admin/', include(admin.site.urls)),
    url(r'^idetec/solicitudes/', include('solicitudes.urls', namespace='solicitudes')),
    url(r'^idetec/dbupdater/', include('dbupdater.urls', namespace='dbupdater')),

)

urlpatterns += staticfiles_urlpatterns()
