from django import forms
from django.contrib.localflavor.br.forms import BRCPFField 

SEXO_CHOICES = (
	('Feminino', 'F'),
	('Masculino', 'M'),
)

# Create your models here.
class cpfForm(forms.Form):
	cpf = BRCPFField(label=u'CPF')

class cadastroForm(forms.Form):
	nome = forms.CharField(max_length=100)
	idade = forms.IntegerField()
	#sexo = forms.CharField(max_length=2, widget=forms.Select(choices=SEXO_CHOICES))
