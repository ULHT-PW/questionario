from django.urls import path
from . import views

app_name = 'sondagem'

urlpatterns = [
    path('<int:sessao_id>/pergunta/', views.pergunta_view, name='pergunta'),
    path('<int:pergunta_id>/votar/', views.votar_view, name='votar'),
    path('<int:pergunta_id>/resultados/', views.resultados_view, name='resultados'),
    path('obrigado/', views.obrigado_view, name='obrigado'),
    
]
