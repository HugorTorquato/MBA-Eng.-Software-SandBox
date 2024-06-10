# Create your views here.

from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

# Look for them latter on
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Import para a permissão local funcionar
from rest_framework import permissions
from .permissions import EhSuperUsuario

# Duas classes para cada objeto
# Não pode deixar tudo junto pq temos endpoints de individuo (objetos unicos) e os de coleção
# que trabalham com conuntos. No caso os que estão no pluração são para verbos HTTP de coleção.
# E os singulares são os individuais (RETRIAVE, UPDATE, DESTROI)

# CRUD

# =========================== API'S V1
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    #Endpoins individuais
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursosAPIView(generics.ListCreateAPIView):
    #Endpoins coletivos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# CRUD
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        endpoint_argument_curso = self.kwargs.get('curso_pk')
        endpoint_argument_avaliacao = self.kwargs.get('avaliacao_pk')
        if endpoint_argument_curso:
            return get_object_or_404(
                self.get_queryset(), 
                curso_id=endpoint_argument_curso, 
                pk=endpoint_argument_avaliacao
            )
        return get_object_or_404(self.get_queryset(), pk=endpoint_argument_avaliacao)

    

class AvaliacoesAPIView(generics.ListCreateAPIView):

    #queryset can get values from an object list
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        # pega or argumentos do endpoint URI
        endpoint_argument = self.kwargs.get('curso_pk')
        if endpoint_argument:
            return self.queryset.filter(curso_id = endpoint_argument)
        return self.queryset.all()



# =========================== API'S V2

class CursoViweSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):

        #curso = self.get_object() # Listar um curso especifico

        # Criar as permissoes para o curso
        #permission_classes = (permissions.DjangoModelPermissions,) # User vai ter de estar autenticado para ver os dados
        permission_classes = (EhSuperUsuario, permissions.DjangoModelPermissions,)


        #Pagintion
        self.pagination_class.page_size = 2 # quantidade de registro que quero mostrar por página
        avaliacoes = Avaliacao.objects.filter(curso_id = pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes.all(), many=True)

        return Response(serializer.data)

""" #Viewset padrão   
class AvaliacaoViewSet(viewsets.ModelViewSet):
    # Não vai listar cusos de uma avaliação, somente as avaliações conhecidas 





        queryset = Avaliacao.objects.all()
        serializer_class = AvaliacaoSerializer
"""
    #VIEW SET CUSTOM
class AvaliacaoViewSet( mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, 
                        mixins.UpdateModelMixin, 
                        mixins.DestroyModelMixin, 
                        viewsets.GenericViewSet):
    
    # /api/v2/avaliacoes -> metodo 'list' não vai ser permitido
    # /api/v2/avaliacoes/4 -> Metodo 'retreave' permitido

    # Basicamente definimos nos parámetros o que vai ser permitido ou n
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # quando entramos em http://127.0.0.1:8000/api/v2/avaliacoes/, que deveria mostrar a lista,
    # mostra um get not allowed 