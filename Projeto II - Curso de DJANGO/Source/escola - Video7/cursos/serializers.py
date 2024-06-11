from rest_framework import serializers
from .models import Curso, Avaliacao

# Defines how th object converts from class to JSON, and the other way arround

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
        

class CursoSerializer(serializers.ModelSerializer):

    #Types of Relationship
    # 1. Nested Relationship
    # Pode somente ler e muitos elementos
    ## avaliacoes = AvaliacaoSerializer(many=True, read_only=True) 

    # 2. Hyperlinked Related Field
    # Não gera todos os dados, e é uma forma mais performatica por gerar links ao inves dos dados
    # As informações são acessadas pelos links
    # Nome da rota 'avaliacao' e o 'detail' é a função de ver dados especificos que o link vai gerar
    # Menos dados são levados na resposta JSON, mas fornece o endpoint para acessar os dados
    ## avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # 3. Primary Key Related Field
    # Não gera o campo com o hyperlink, mas gera o campo com a chave primária ( id ) da avaliação
    # Forma mais performatica por trazer somente 1 dado pequeno, id do registro.
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes' # Listas das nossas avaliações
        )