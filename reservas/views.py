# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from reservas.forms import cadastroForm, cpfForm
from reservas.models import User

def cpf_form(request):
	if request.method == 'POST':
		form = cpfForm(request.POST)
		usr = User()
		if form.is_valid():
			try:
				if User.objects.get(cpf=form.cleaned_data['cpf']):
					return HttpResponse('CPF existente!<br><a href="">Voltar</a>')
			except:
				usr.cpf = form.cleaned_data['cpf']
				usr.save()
				return HttpResponseRedirect('/cadastro/' + usr.cpf)
		else:
			return render(request, 'cpf_form.html', {'form': form})
	else:
		form = cpfForm()

	return render(request, 'cpf_form.html', {'form': form})

def cadastro(request, cpf):
	if request.method == 'POST':
		form = cadastroForm(request.POST)
		usr = User.objects.get(cpf=cpf)
		if form.is_valid():
			usr.nome = form.cleaned_data['nome']
			usr.idade = form.cleaned_data['idade']
			usr.sexo = form.cleaned_data['sexo']
			usr.email = form.cleaned_data['email']
			usr.aniversario = form.cleaned_data['aniversario']
			usr.profissao = form.cleaned_data['profissao']
			usr.experiencia = form.cleaned_data['experiencia']
			usr.save()
			return HttpResponseRedirect('/resultados/')
	else:
		form = cadastroForm()

	return render(request, 'cadastro.html', {'form': form})

def resultados(request):
	context = {}
	context['feminino'] = User.objects.all().filter(sexo='F')
	context['masculino'] = User.objects.all().filter(sexo='M')
	return render(request,'resultados.html', context)