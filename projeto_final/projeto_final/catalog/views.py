from django.shortcuts import render
from catalog.models import Posicao, Jogador, Partida, Treinador
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    numeroDePosicoes=Posicao.objects.all().count
    numeroDePartidas=Partida.objects.all().count
    numeroDeJogadores=Jogador.objects.count()
    numeroDeTreinadores=Treinador.objects.count()
    numeroDeVisitas=request.session.get('numeroDeVisitas', 0)
    request.session['numeroDeVisitas']=numeroDeVisitas+1
    
    context={       
        'numeroDePosicoes':numeroDePosicoes,
        'numeroDePartidas':numeroDePartidas,
        'numeroDeJogadores':numeroDeJogadores,
        'numeroDeTreinadores':numeroDeTreinadores,
        'numeroDeVisitas':numeroDeVisitas
    }
    
    return render(request,'index.html',context=context)

class JogadorListView(generic.ListView):
    model=Jogador
    paginate_by=6
    
class JogadorDetailView(generic.DetailView):
    model=Jogador
    
class TreinadorListView(generic.ListView):
    model=Treinador   
    
class TreinadorDetailView(generic.DetailView):
    model=Treinador

class PartidaListView(generic.ListView):
    model=Partida

class PartidaDetailView(generic.DetailView):
    model=Partida

class TreinadorCreate(CreateView):
    model = Treinador
    fields = '__all__'

class TreinadorUpdate(UpdateView):
    model = Treinador
    fields = ['nome', 'idade', 'email']

class TreinadorDelete(DeleteView):
    model = Treinador
    success_url = reverse_lazy('treinadores')
    
class JogadorCreate(CreateView):
    model = Jogador
    fields = '__all__'

class JogadorUpdate(UpdateView):
    model = Jogador
    fields = ['nome', 'treinador', 'numeroDaCamisa', 'posicao']

class JogadorDelete(DeleteView):
    model = Jogador
    success_url = reverse_lazy('jogadores')