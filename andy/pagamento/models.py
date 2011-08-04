from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    created_at = models.DateTimeField(u"Data", auto_now_add=True)
    paid = models.BooleanField(u"Pago", default=False)
    user = models.ForeignKey(User, null=True)
    status = models.CharField(u"Status", max_length=20, default="Aprovado", choices=(
                            ('Cancelado', 'Cancelado'),
                            ('Aguardando', 'Aguardando'),
                            ('Aprovado', 'Aprovadao')))

    class Meta:
        verbose_name = u"Anuidade"
