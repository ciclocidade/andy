from django.contrib import admin 

from pagamento.models import Payment

admin.site.register(Payment, list_display=('user', 'user__email', 'created_at', 'status', 'paid'), list_filter=('created_at', 'status', 'paid'), search_fields=('user__first_name', 'user__last_name', 'user__email'))
