from django.db import models
from django.contrib.localflavor.br.forms import BRCPFField 

class User(models.Model):
	cpf = BRCPFField(label=u'CPF')
	nome = models.CharField(max_length=100)
	idade = models.IntegerField(blank=True)