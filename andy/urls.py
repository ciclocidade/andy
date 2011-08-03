from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django_pagseguro.urls import pagseguro_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^$', 'andy.views.login', name="index"),
    url(r'^', include('cadastro.urls')),
)

urlpatterns += pagseguro_urlpatterns()
