# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

EDUCATIONS = (
        ('FC', u'Fundamental Completo'),
        ('MI', u'Médio Incompleto'),
        ('MC', u'Médio Completo'),
        ('SI', u'Superior Incompleto'),
        ('SC', u'Superior Completo'),
        ('MD', u'Mestrado/Doutorado'),
    )

class Member(models.Model):
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(u"Data de cadastro", auto_now_add=True)
    sexo = models.CharField(u"Sexo", choices=(("F", "Feminino"), ("M", "Masculino")), max_length=2, default="F")
    birth = models.DateField(u"Data de Nascimento")
    phone_number = models.CharField(u"Telefone", max_length=15)
    address_street = models.CharField(u"Endereço", max_length=150)
    address_state = models.CharField(u"Estado", max_length=30)
    address_city = models.CharField(u"Cidade", max_length=30)
    address_zip = models.CharField(u"CEP", max_length=9)
    address_etc = models.CharField(u"Complemento", max_length=50, blank=True, default='')
    education = models.CharField(u'Escolaridade', max_length=2, choices=EDUCATIONS)
    profession = models.CharField(u'Profissão/Ocupação', max_length=100)
    rg = models.IntegerField(u'RG')
    cpf = models.IntegerField(u'CPF')
    receive_news = models.BooleanField(u'Deseja receber informativo?', default=True)
    #phone_number_2
    #organizations = 
    #bicycle_usage
    #bicycle_frequency

    class Meta:
        verbose_name = "Associado"

    def is_complete(self):
        required_fields = ( 'user',
                            'created_at',
                            'sexo',
                            'birth',
                            'phone_number',
                            'address_street',
                            'address_state',
                            'address_city',
                            'address_zip',
                            'education',
                            'cpf')
        return all(getattr(self, field) for field in required_fields)

        
    @property
    def name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email
