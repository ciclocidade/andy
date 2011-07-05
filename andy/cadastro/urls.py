from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cadastro.views',
        url(r'registrar/', 'register', name='cadastro_register'),
        url(r'perfil/', 'profile', name='cadastro_profile'),
        url(r'contas/ativar/(?P<activation_key>\w+)/$', 'activate', name='cadastro_activate'),
)
