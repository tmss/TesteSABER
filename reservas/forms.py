from django import forms
from reservas.models import *
from django.contrib.localflavor.br.forms import BRCPFField 

# Create your models here.
class cpfForm(forms.Form):
	cpf = BRCPFField(label=u'CPF')

		

class cadastroForm(forms.Form):
	SEXO_CHOICES = (
		('F', 'Feminino'),
		('M', 'Masculino'),
	)

	nome = forms.CharField(max_length=100)
	idade = forms.IntegerField()	
	sexo = forms.CharField(max_length=1, widget=forms.RadioSelect(choices=SEXO_CHOICES))
	aniversario = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), input_formats=['%d/%m/%Y'])
	email = forms.EmailField(max_length=50)
	profissao = forms.CharField(max_length=100)
	experiencia = forms.CharField(widget=forms.Textarea)
	def __init__(self, *args, **kwargs):
		super(cadastroForm, self).__init__(*args, **kwargs)
		self.fields['aniversario'].label = "Aniversario (dd/mm/aaaa)"