# coding: utf-8

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.conf import settings

from registration.forms import RegistrationFormUniqueEmail
from registration.models import RegistrationProfile

from pagamento.models import Payment

from cadastro.models import Member, BikeUsageSurvey
from cadastro.forms import MemberForm, BikeUsageForm

from datetime import datetime, date


def register(request):
    if request.method == 'POST':
        form = RegistrationFormUniqueEmail(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_user = form.save()
            messages.add_message(request, messages.SUCCESS, 'Registro feito com sucesso, por favor verifique seu email para continuar com o processo de associação.')
            return HttpResponseRedirect('/')
    else: 
        form = RegistrationFormUniqueEmail()
    return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

def activate(request, activation_key=None):
    if activation_key:
        activation_key = activation_key.lower() 
        user = RegistrationProfile.objects.activate_user(activation_key)
        if user:
            messages.add_message(request, messages.SUCCESS, 'Seu email foi verificado com sucesso! Faça o login para continuar com o processo de associação.')
            return HttpResponseRedirect(reverse(profile))
    messages.add_message(request, messages.ERROR, 'Não foi possivel ativar o cadastro')
    return render_to_response('activate_error.html', context_instance=RequestContext(request))

@login_required
def profile(request):
    msg = ''
    try:
        member = request.user.get_profile()
        msg = u'Olá %s! Atualize os seus dados cadastrais :-)' % request.user.get_full_name()
    except ObjectDoesNotExist:
        member = Member(user=request.user)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            messages.add_message(request, messages.SUCCESS, 'Seu perfil foi atualizado com sucesso!')
            if member.is_complete() and request.user.is_active:
                try:
                    BikeUsageSurvey.objects.get(member=member)
                    return HttpResponseRedirect(reverse("cadastro_pay"))
                except BikeUsageSurvery.DoesNotExist:
                    return HttpResponseRedirect(reverse('cadastro_survey'))
    else:
        form = MemberForm(instance=member)
    if not member.is_complete():
        msg = "Complete os dados do seu perfil!"
    if not form.fields['name'].initial:
        form.fields['name'].initial = request.user.get_full_name()
    if not form.fields['address_city'].initial:
        form.fields['address_city'].initial = u'São Paulo' 
    messages.add_message(request, messages.WARNING, msg)
    return render_to_response('profile.html', {'user': request.user, 'form': form}, context_instance=RequestContext(request))

def _has_profile(user):
    try:
        user.get_profile().is_complete()
    except ObjectDoesNotExist:
        return False
    return True

@login_required
@user_passes_test(_has_profile, login_url='/perfil/')
def survey(request):
    member = request.user.get_profile()
    form = None
    if not member.answered_survey():
        form = BikeUsageForm()
    if request.method == 'POST':
        form = BikeUsageForm(request.POST)
        if form.is_valid():
            try:
                BikeUsageSurvey.objects.get(member=member)
            except BikeUsageSurvey.DoesNotExist:
                bus = form.save(commit=False)
                bus.member = member
                bus.save()
                messages.add_message(request, messages.SUCCESS, 'Pesquisa preenchida com sucesso, obrigado!')
                return HttpResponseRedirect(reverse("cadastro_pay"))
            else:
                messages.add_message(request, messages.ERROR, 'Você já preencheu essa pesquisa!')
    return render_to_response('survey.html', {'user': request.user, 'form': form}, context_instance=RequestContext(request))

@login_required
@user_passes_test(_has_profile, login_url='/perfil/')
def pay(request):
    from django_pagseguro.pagseguro import ItemPagSeguro, CarrinhoPagSeguro
    user = request.user
    member = user.get_profile()
    if request.method == 'POST':
        p = Payment.objects.create(status="Aguardando", user=user)
        carrinho = CarrinhoPagSeguro(ref_transacao=p.pk)
        carrinho.set_cliente(email=user.email, cep=member.address_zip)
        valor = calculate_membership_fee(datetime.today())
        donations = request.POST['donation'].replace(",", ".")
        try:
            donations = float(donations)
        except ValueError: 
            donations = 0
        carrinho.add_item(ItemPagSeguro(cod=1, descr='Anuidade Ciclocidade', quant=1, valor=float(valor)))
        if donations > 0:
            carrinho.add_item(ItemPagSeguro(cod=1, descr='Doação Ciclocidade', quant=1, valor=float(donations)))
        payment_form = carrinho.form()
        return render_to_response("pay-forward.html", {'payment_form': payment_form}, context_instance=RequestContext(request))
    paids = user.payment_set.filter(paid=True)

    now = datetime.now()
    year = now.year if now.month >= 8 else now.year - 1
    last_year = paids.filter(created_at__gt=date(year, 8, 1))
    
    show_form = not bool(last_year.count())
    if not show_form:
        messages.add_message(request, messages.SUCCESS, 'Você esta em dia com o pagamento da anuidade!')
        year = None
    else:
        messages.add_message(request, messages.WARNING, 'Por favor, leia as instruções e efetue o pagamento da anuidade via PagSeguro')
        year = datetime.now().year
    return render_to_response("pay.html", {'paids': paids, 'show_form': show_form,  'year': year},
            context_instance=RequestContext(request))

def calculate_membership_fee(date):
    month = date.month
    if month < 8:
        return (8 - month) * 5
    return (12 - month + 8) * 5
