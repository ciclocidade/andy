from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django_pagseguro.urls import pagseguro_urlpatterns
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from cadastro.forms import PasswordResetForm

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^password/reset/$', password_reset, { 'template_name': 'password_reset.html',
                                                'email_template_name': 'emails/password_reset.txt',
                                                'from_email': 'no-reply@ciclocidade.org.br',
                                                'password_reset_form': PasswordResetForm}, name='password_reset'),
    url(r'^password/done/$', password_reset_done, { 'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    url(r'^password/confirm/(?P<uidb36>\w+)/(?P<token>[\w-]+)/$', password_reset_confirm, { 'template_name': 'password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password/complete/$', password_reset_complete, { 'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^$', 'andy.views.login', name="index"),
    url(r'^', include('cadastro.urls')),
)

urlpatterns += pagseguro_urlpatterns()
