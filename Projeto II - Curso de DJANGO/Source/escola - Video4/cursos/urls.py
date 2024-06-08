from django.urls import path
from .views import CursoAPIView, CursosAPIView, AvaliacaoAPIView, AvaliacoesAPIView

urlpatterns = [
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes')
]