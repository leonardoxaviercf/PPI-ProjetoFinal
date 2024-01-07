from django.contrib import admin
from catalog.models import Posicao, Jogador, Partida, Treinador

admin.site.register(Posicao)
# admin.site.register(Partida)
# admin.site.register(Jogador)
# admin.site.register(Treinador)
class TreinadorAdmin(admin.ModelAdmin):
    list_display=('nome', 'idade', 'email')

admin.site.register(Treinador, TreinadorAdmin)

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display=('nome', 'numeroDaCamisa')

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display=('local', 'adversario', 'placar', 'dataHora')

# Register your models here.
