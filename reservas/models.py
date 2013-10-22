from django.db import models

class User(models.Model):
	SEXO_CHOICES = (
		('F', 'Feminino'),
		('M', 'Masculino'),
	)

	cpf = models.CharField(max_length=20, primary_key=True)
	nome = models.CharField(max_length=100)
	idade = models.IntegerField(null=True)
	sexo = models.CharField(max_length=1,choices=SEXO_CHOICES)
	aniversario = models.DateField(blank=True, null=True)
	email = models.EmailField(max_length=50)
	profissao = models.CharField(max_length=100)
	experiencia = models.TextField()
	def __unicode__(self):
		return unicode(self.cpf)