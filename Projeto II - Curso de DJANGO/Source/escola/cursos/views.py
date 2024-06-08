# Create your views here.

from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

# Duas classes para cada objeto
# Não pode deixar tudo junto pq temos endpoints de individuo (objetos unicos) e os de coleção
# que trabalham com conuntos. No caso os que estão no pluração são para verbos HTTP de coleção.
# E os singulares são os individuais (RETRIAVE, UPDATE, DESTROI)

# CRUD
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    #Endpoins individuais
    queryset = Curso.objects.all()
    serialize_class = CursoSerializer

class CursosAPIView(generics.ListCreateAPIView):
    #Endpoins coletivos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# CRUD
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
