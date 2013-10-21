# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from reservas.forms import cadastroForm, cpfForm
from reservas.models import User

def cpf_form(request):
	if request.method == 'POST':
		form = cpfForm(request.POST)
		usr = User()
		if form.is_valid():
			usr.cpf = form.cleaned_data['cpf']
			usr.save()
			return HttpResponseRedirect('/cadastro/')
		else:
			return HttpResponse('cpf errado!')
	else:
		form = cpfForm()

	return render(request, 'cpf_form.html', {'form': form})

def cadastro(request):
	if request.method == 'POST':
		form = cadastroForm(request.POST)
		usr = User()
		if form.is_valid():
			usr.nome = form.cleaned_data['nome']
			usr.idade = form.cleaned_data['idade']
			#user.sexo = user.cleaned_data['sexo']
			usr.save()
			return HttpResponse('%s' % form.nome)
		else:
			return HttpResponse('erro!')
	else:
		user = cadastro()

	return render(request, 'cadastro.html')