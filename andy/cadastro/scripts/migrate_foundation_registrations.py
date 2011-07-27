#!/usr/bin/env python

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.template.defaultfilters import slugify

from andy.cadastro.models import Member

try:
    import cPickle as pickle
except ImportError:
    import pickle

import re

def birth(registration):
    # :/
    dt = registration['dt_nascimento']
    if not dt or len(dt) < 6:
        return None
    if '/' in dt:
        try:
            d,m,y = dt.split("/")
        except ValueError:
            return None
    else:
        d,m,y = dt[:2], dt[2:4], dt[4:]
    if len(y) not in (2, 4):
        return None
    if len(y) == 2:
        y = "19" + y
    if len(d) < 2:
        d = "0" + d
    if len(m) < 2:
        m = "0" + m
    return "%s-%s-%s" % (y,m,d)

def phone_number(registration):
    t = registration['celular'] if not registration['celular'].isspace() else registration['telefone']
    t = "".join(t.split())
    return t[:15]

def sexo(registration):
    if sexo:
        return registration['sexo'][0]
    return None

def rg(registration):
    rg = registration['identidade']
    rg = ''.join(rg.split())
    return rg[:15]

def cpf(registration):
    return registration['cpf'][:15]

foundation_fields = ('profissao', 'cep', 'dt_nascimento', 'celular', 'sexo', 'estado', 'cpf', 'identidade', 'endereco', 'autorizacao')
membership_fields = ('profession', 'address_zip', birth, phone_number, sexo, 'address_state', cpf, rg, 'address_street', 'receive_news')
# from django core
email_re = re.compile(r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
                      r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
                      r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain

def run(registrations):
    member = [ migrate(registration) for registration in registrations if is_email(registration['email']) ]

def migrate(registration):
    new = {}
    for oldattr,newattr in zip(foundation_fields, membership_fields):
        if callable(newattr):
            new[newattr.func_name] = newattr(registration)
        else:
            new[newattr] = registration[oldattr]
    
    # user data 
    nome = registration['nome'].split()
    user = {'first_name': nome[0], 'last_name': ' '.join(nome[1:]), 'email': registration['email']}
    user['username'] = username(registration)

    try:
        u = User.objects.create(**user)
    except IntegrityError:
        u = User.objects.get(username=user['username'])
    
    new['user'] = u
    try: 
        m = Member.objects.get(user__id=u.id)
    except Member.DoesNotExist:
        m = Member.objects.create(**new)
    else:
        for field in new.keys():
            setattr(m, field, new[field])
        m.save()
    return m

def username(registration):
    if registration['apelido']:
        un = slugify(registration['apelido']).replace('-', '_')
        if len(un) > 2:
            return un
    return registration['email'].split("@")[0]
    
def is_email(email):
    return bool(email_re.match(email))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "%s <pickled registrations>" % sys.argv[0]
        sys.exit(1)
    try:
        registrations = pickle.load(open(sys.argv[1]))
    except:
        print "%s: invalid file" % sys.argv[1]
        sys.exit(2)
    run(registrations)
