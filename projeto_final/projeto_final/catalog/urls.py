from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('jogadores/', views.JogadorListView.as_view(), name='jogadores'),
    path('jogador/<int:pk>', views.JogadorDetailView.as_view(), name='jogador-detail'),
    path('treinador/', views.TreinadorListView.as_view(), name='treinador'),
    path('treinador/<int:pk>', views.TreinadorDetailView.as_view(), name='treinador-detail'),
    path('partidas/', views.PartidaListView.as_view(), name='partidas'),
    path('partida/<int:pk>', views.PartidaDetailView.as_view(), name='partida-detail'),
]

urlpatterns += [
    path('treinador/create/', views.TreinadorCreate.as_view(), name='treinador_create'),
    path('treinador/<int:pk>/update/', views.TreinadorUpdate.as_view(), name='treinador_update'),
    path('treinador/<int:pk>/delete/', views.TreinadorDelete.as_view(), name='treinador_delete'),
]

urlpatterns += [
    path('jogador/create/', views.JogadorCreate.as_view(), name='jogador_create'),
    path('jogador/<int:pk>/update/', views.JogadorUpdate.as_view(), name='jogador_update'),
    path('jogador/<int:pk>/delete/', views.JogadorDelete.as_view(), name='jogador_delete'),
]
