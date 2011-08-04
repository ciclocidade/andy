# coding: utf-8

from pagamento.models import Payment
from django_pagseguro.signals import (pagamento_cancelado, pagamento_aprovado, 
                                     pagamento_em_analise, pagamento_aguardando,
                                     pagamento_devolvido)

import logging

def update_payment(pk, status):
    p = Payment.objects.get(pk=pk)
    p.status = status
    p.save()
    return p

def pagseguro_approved(sender, **kwargs):
    logging.debug("signal pagseguro_approved received")
    p = update_payment(sender.referencia, "Aprovado")
    p.paid = True
    p.save()
    logging.debug("signal pagseguro_approved finished")

def pagseguro_waiting(sender, **kwargs):
    logging.debug("signal pagseguro_waiting received")
    p = update_payment(sender.referencia, "Aguardando")
    logging.debug("signal pagseguro_waiting finished")

def pagseguro_canceled(sender, **kwargs):
    logging.debug("signal pagseguro_canceled received")
    p = update_payment(sender.referencia, "Cancelado")
    logging.debug("signal pagseguro_canceled finished")

pagamento_aprovado.connect(pagseguro_approved)
pagamento_aguardando.connect(pagseguro_waiting)
pagamento_em_analise.connect(pagseguro_waiting)
pagamento_devolvido.connect(pagseguro_canceled)
pagamento_cancelado.connect(pagseguro_canceled)
