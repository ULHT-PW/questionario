from django.db import models

class Sessao(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return f'Sessão No. {self.numero}'

class Pergunta(models.Model):
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    texto_pergunta = models.CharField(max_length=200)
    ativa = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.texto_pergunta}'

	
class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    votos = models.IntegerField(default=0)
    texto_escolha =  models.CharField(max_length=200)

    def __str__(self):
        return f'{self.texto_escolha}'
