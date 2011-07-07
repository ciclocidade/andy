from django.contrib import admin 

from models import Member, BikeUsageSurvey

admin.site.register(Member, list_display=('name', 'created_at', 'birth', 'city_uf_str', 'cpf', 'education'), list_filter=('created_at', 'sexo', 'birth', 'address_state', 'education', 'receive_news'), search_fields=('user__first_name', 'user__last_name', 'user__email', 'cpf'))
admin.site.register(BikeUsageSurvey, list_display=('member', 'created_at'), list_filter=('created_at', 'bike_usage', 'frequency', 'source', 'expectations', 'volunteering'), search_fields=('member__user__first_name', 'member__user__last_name', 'member__user__email', 'member__cpf'))
