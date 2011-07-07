# coding: utf-8
from django import forms
from django.contrib.localflavor.br.forms import BRStateSelect, BRCPFField, BRZipCodeField, BRPhoneNumberField
from django.contrib.localflavor.br.br_states import STATE_CHOICES

SP_BRStateSelect = (('SP', u"São Paulo"),) + STATE_CHOICES

from models import Member

class MemberForm(forms.ModelForm):
    # account info
    password1 = forms.CharField(label=u"senha", widget=forms.PasswordInput(), required=False)
    password2 = forms.CharField(label=u"senha (novamente)", widget=forms.PasswordInput(), required=False)
    
    # profile info
    name = forms.CharField(label=u"Nome completo")
    phone_number = BRPhoneNumberField(label="Telefone")
    address_zip = BRZipCodeField(label="CEP")
    cpf = BRCPFField(label="CPF")
    
    def save(self, *args, **kwargs):
        member = super(MemberForm, self).save(*args, **kwargs)
        first_name = self.cleaned_data['name'].split()[0]
        last_name = " ".join(self.cleaned_data['name'].split()[1:])
        member.user.first_name = first_name
        member.user.last_name = last_name
        if self.cleaned_data['password1'] and self.cleaned_data['password1'] == self.cleaned_data['password2']:
            member.user.set_password(self.cleaned_data['password1'])
        member.user.save()
        return member

    def clean(self, *args, **kwargs):
        self.cleaned_data = super(MemberForm, self).clean(*args, **kwargs)
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
        return self.cleaned_data

    class Meta:
        model = Member
        exclude = ( 'user',
                    'created_at',)
        widgets = {'address_state': forms.fields.Select(choices=SP_BRStateSelect) }
