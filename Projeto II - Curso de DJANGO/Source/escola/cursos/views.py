from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Nesse caso os dados bem do request com a propriedade data
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        #return Response({"msg":"Criado com sucesso"}) # A resposta tbm pode ser uma mensagem
        #return Response({"id":serializer.data['id']}) # A resposta tbm pode ser uma mensagem com dados

        



class AvaliacaoAPIView(APIView):

    def get(self, request):
        avaliacores = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacores, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Nesse caso os dados bem do request com a propriedade data
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



