# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

EDUCATIONS = (
        ('FI', u'Fundamental Incompleto'),
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
    birth = models.DateField(u"Data de Nascimento", null=True)
    phone_number = models.CharField(u"Telefone", max_length=15)
    address_street = models.CharField(u"Endereço", max_length=150)
    address_state = models.CharField(u"Estado", max_length=30)
    address_city = models.CharField(u"Cidade", max_length=30)
    address_zip = models.CharField(u"CEP", max_length=9)
    address_etc = models.CharField(u"Complemento", max_length=50, blank=True, default='')
    education = models.CharField(u'Escolaridade', max_length=2, choices=EDUCATIONS)
    profession = models.CharField(u'Profissão/Ocupação', max_length=100)
    rg = models.CharField(u'RG', max_length=15)
    cpf = models.CharField(u'CPF', max_length=15)
    organizations = models.TextField(u"Organizações", default="", blank=True, null=True)
    receive_news = models.BooleanField(u'Recebe informativo', default=True, blank=True)

    class Meta:
        verbose_name = "Associado"
    
    def answered_survey(self):
        try:
            BikeUsageSurvey.objects.get(member=self)
        except BikeUsageSurvey.DoesNotExist:
            return False
        return True

    def city_uf_str(self):
        return "%s/%s" % (self.address_city, self.address_state)
    
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

    def __unicode__(self):
        return self.name

    @property
    def name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email


from multiselectmodelfield import MultiSelectField
class BikeUsageSurvey(models.Model):
    FREQUENCY_CHOICES = [ (i,i) for i in (u"5 a 7 vezes por semana",
                         u"2 a 4 vezes por semana",
                         u"uma vez por semana",
                         u"eventualmente",
                         u"não utilizo a bicicleta") ]
    SOURCE_CHOICES = [ (i,i) for i in (u"sites, blogs ou mecanismos de busca na internet",
                      u"facebook, twitter ou listas de e-mail",
                      u"indicação de amigos / conhecidos",
                      u"eventos / atividades",
                      u"panfleto",
                      u"participei do ato de fundação",
                      u"instituição ou grupo",
                      u"outros") ]
    USAGE_CHOICES = [ (i,i) for i in (
                     u"ir ao trabalho às vezes",
                     u"ir ao trabalho todos os dias",
                     u"fazer outros deslocamentos no meu dia-a-dia",
                     u"como instrumento de trabalho (ex: entregas, vigilância, etc)",
                     u"lazer",
                     u"esporte (amador ou profissional)",
                     u"não utilizo a bicicleta") ]
    EXPECTATIONS_CHOICES = [ (i,i) for i in (
                    u"conhecer direitos e leis a serem defendidos junto a órgãos públicos e outras instituições",
                    u"contribuir para a construção de políticas públicas relativas à mobilidade urbana",
                    u"espaços de discussão sobre o uso da bicicleta na cidade (dicas, problemas, experiências, trajetos e outros)",
                    u"atividades culturais e educativas que promovam o uso da bicicleta (encontros, passeios, seminários, oficinas)",
                    u"aprofundamento teórico, estudo e produção de conhecimento",
                    u"conhecer dicas e técnicas sobre compra, uso e manutenção de bicicletas") ]
    VOLUNTEERING_CHOICES = [ (i,i) for i in (
                    u"sim, participando de projetos específicos e pontuais nas minhas áreas de interesse ou atuação",
                    u"sim, participando da Coordenadoria de Cultura da Bicicleta e Formação do Ciclista",
                    u"sim, participando da Coordenadoria de Participação Pública",
                    u"sim, participando da Coordenadoria de Pesquisa",
                    u"sim, participando da Coordenadoria de Comunicação",
                    u"sim, participando da Coordenadoria de Tecnologia",
                    u"sim, participando da Coordenadoria de Relações com Associados e Voluntários",
                    u"sim, participando da Coordenadoria de Desenvolvimento Institucional",
                    u"sim, representando a associação no meu bairro, grupo ou entidade",
                    u"não, não tenho disponibilidade") ]
    CITY_REGION = [ (i.split("(")[0].strip(),i) for i in (
		    u"ARICANDUVA (Aricanduva, Carrão, Vila Formosa)",
		    u"BUTANTÃ (Butantã, Morumbi, Vila Sônia, Raposo Tavares, Rio Pequeno)",
		    u"CAMPO LIMPO, Campo Limpo, Capão Redondo, Vila Andrade)",
		    u"CAPELA DO SOCORRO (Socorro, Grajaú, Cidade Dutra)",
		    u"CASA VERDE (Casa Verde, Cachoeirinha, Limão)",
		    u"CIDADE ADEMAR (Cidade Ademar, Pedreira)",
		    u"CIDADE TIRADENTES (Cidade Tiradentes)",
		    u"ERMELINO MATARAZZO (Ermelino Matarazzo, Ponte Rasa)",
		    u"FREGUESIA DO Ó (Freguesia do Ó, Brasilândia)",
		    u"GUAIANASES (Guaianases, Lajeado)",
		    u"IPIRANGA (Ipiranga, Cursino, Sacomã)",
		    u"ITAIM PAULISTA (Itaim Paulista, Vila Curuçá)",
		    u"ITAQUERA (Itaquera, Parque do Carmo, José Bonifácio, Cidade Líder)",
		    u"JABAQUARA (Jabaquara)",
		    u"JAÇANÃ (Tremembé, Jaçanã)",
		    u"LAPA (Lapa, Barra Funda, Perdizes, Vila Leopoldina, Jaguaré, Jaraguá)",
		    u"M'BOI MIRIM (Jardim Ângela, Jardim São Luís)",
		    u"MÓOCA (Mooca, Brás, Belém, Pari, Água Rasa, Tatuapé)",
		    u"PARELHEIROS (Parelheiros, Marsilac)",
		    u"PENHA (Penha, Cangaíba, Vila Matilde, Artur Alvim)",
		    u"PERUS (Anhangüera, Perus)",
		    u"PINHEIROS (Alto de Pinheiros, Pinheiros, Itaim Bibi, Jardim Paulista)",
		    u"PIRITUBA (Pirituba, São Domingos, Jaraguá)",
		    u"SANTANA (Santana, Tucuruvi, Mandaqui)",
		    u"SANTO AMARO (Santo Amaro, Campo Belo, Campo Grande)",
		    u"SÃO MATEUS (São Mateus, São Rafael, Iguatemi)",
		    u"SÃO MIGUEL (São Miguel Paulista, Jardim Helena, Vila Jacuí)",
		    u"SÉ (Bom Retiro, Santa Cecília, Consolação, República, Sé, Bela Vista, Liberdade, Cambuci)",
		    u"VILA MARIA (Vila Maria, Vila Guilherme, Vila Medeiros)",
		    u"VILA MARIANA (Vila Mariana, Saúde, Moema)",
		    u"VILA PRUDENTE (Vila Prudente, Sapopemba, São Lucas)" ) ]
    CITY_METRO = [ (i,i) for i in (
		u"ARUJÁ",
		u"BARUERI",
		u"BIRITIBA-MIRIM",
		u"CAIEIRAS",
		u"CAJAMAR",
		u"CARAPICUÍBA",
		u"COTIA",
		u"DIADEMA",
		u"EMBU",
		u"EMBU GUAÇU",
		u"FERRAZ DE VASCONCELOS",
		u"FRANCISCO MORATO",
		u"FRANCO DA ROCHA",
		u"GUARAREMA",
		u"GUARULHOS",
		u"ITAPECERICA DA SERRA",
		u"ITAPEVI",
		u"ITAQUAQUECETUBA",
		u"JANDIRA",
		u"JUQUITIBA",
		u"MAIRIPORÃ",
		u"MAUÁ",
		u"MOGI DAS CRUZES",
		u"OSASCO",
		u"PIRAPORA DO BOM JESUS",
		u"POÁ",
		u"RIBEIRÃO PIRES",
		u"RIO GRANDE DA SERRA",
		u"SALESÓPOLIS",
		u"SANTA ISABEL",
		u"SANTANA DE PARNAÍBA",
		u"SANTO ANDRÉ",
		u"SÃO BERNARDO DO CAMPO",
		u"SÃO CAETANO DO SUL",
		u"SÃO LOURENÇO DA SERRA",
		u"SUZANO",
		u"TABOÃO DA SERRA",
		u"VARGEM GRANDE PAULISTA" ) ]

    member = models.OneToOneField(Member, verbose_name="Associado")
    created_at = models.DateTimeField(u"Data", auto_now_add=True)
    bike_usage = MultiSelectField(u"Uso da bicicleta", choices=USAGE_CHOICES)
    frequency = models.CharField(u"Frequência que usa a bicicleta", choices=FREQUENCY_CHOICES, max_length=255)
    source = models.CharField(u"Como soube da associação", choices=SOURCE_CHOICES, max_length=255)
    expectations = MultiSelectField(u"Expectativa Ciclocidade", choices=EXPECTATIONS_CHOICES)
    city_region = MultiSelectField(u"Por onde você pedala (distritos/subprefeituras)", choices=CITY_REGION, default="", blank=True)
    city_metro  = MultiSelectField(u"Por onde você pedala (região metropolitana)", choices=CITY_METRO, default="", blank=True)
    volunteering = MultiSelectField(u"Voluntário", choices=VOLUNTEERING_CHOICES)
    
    class Meta:
        verbose_name = u"Pesquisa hábitos e interesses"
        verbose_name_plural = u"Pesquisas hábitos e interesses"

    def __unicode__(self):
        return self.member.name

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^cadastro\.multiselectmodelfield\.MultiSelectField"])
