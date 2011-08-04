# coding: utf-8

from pagamento.models import Payment
from django_pagseguro.signals import (pagamento_cancelado, pagamento_aprovado, 
                                     pagamento_em_analise, pagamento_aguardando,
                                     pagamento_devolvido)

def update_payment(pk, status):
    p = Payment.objects.get(pk=sender.referencia)
    p.status = status
    p.save()

def pagseguro_approved(sender, **kwargs):
    p = update_payment(sender.referencia, "Aprovado")
    p.paid = True
    p.save()

def pagseguro_waiting(sender, **kwargs):
    p = update_payment(sender.referencia, "Aguardando")

def pagseguro_canceled(sender, **kwargs):
    p = update_payment(sender.referencia, "Cancelado")

pagamento_aprovado.connect(pagseguro_approved)
pagamento_aguardando.connect(pagseguro_waiting)
pagamento_em_analise.connect(pagseguro_waiting)
pagamento_devolvido.connect(pagseguro_canceled)
pagamento_cancelado.connect(pagseguro_canceled)
