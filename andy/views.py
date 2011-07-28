# coding: utf-8

from django.http import HttpResponseRedirect
from django.contrib.auth.views import login as auth_login
from django.core.urlresolvers import reverse

from cadastro.views import profile

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('cadastro_profile'))
    return auth_login(request, template_name="index.html")
