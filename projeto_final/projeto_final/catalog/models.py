from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Posicao(models.Model):
    nome=models.CharField(max_length=200, help_text='Insira a posição do jogador.')

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome=models.CharField(max_length=200, help_text='Insira o nome do jogador.')
    treinador=models.ForeignKey('Treinador', on_delete=models.SET_NULL, null=True)
    numeroDaCamisa=models.CharField(max_length=200, help_text='Insira o número da camisa.')
    posicao=models.ManyToManyField(Posicao, help_text='Insira a posição do jogador.')

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('jogador-detail', args=[str(self.id)])

class Partida(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único para partida dentro do histórico de partidas.')
    local=models.CharField(max_length=200, default='IFRN - campus Natal-Central', help_text='Local da partida.')
    adversario=models.CharField(max_length=200, help_text='Insira o nome do time adversário.')
    dataHora=models.DateField(null=True, blank=True)
    placar=models.CharField(max_length=200, blank=True, help_text='Insira o placar da partida.')

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('partida-detail', args=[str(self.id)])


class Treinador(models.Model):
    nome=models.CharField(max_length=200, help_text='Insira o nome do treinador.')
    idade=models.CharField(max_length=200, help_text='Insira a idade do treinador.')
    email=models.CharField(max_length=200, help_text='Insira o e-mail do treinador.')
    
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('treinador-detail', args=[str(self.id)])

    