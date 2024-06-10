from django.contrib import admin

# Import the mdoels to be defined here

from .models import Curso, Avaliacao

# Register your models here.

    # Cadastramento de uma model no painel admin

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')

@admin.register(Avaliacao)
class CursoAvaliacao(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo')