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

class AvaliacaoAPIView(APIView):

    def get(self, request):
        avaliacores = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacores, many=True)
        return Response(serializer.data)