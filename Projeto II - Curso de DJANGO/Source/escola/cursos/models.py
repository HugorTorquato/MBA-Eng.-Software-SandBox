# This imports Django's model module, which allows you to create database schemas by defining classes.
from django.db import models

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True) # This field will be added automatcly
    atualizacao = models.DateTimeField(auto_now=True) # This one will store the date when the record is updated
    ativo = models.BooleanField(default=True)

    class Meta:              # This inner class is used to provide metadata about the model
        abstract = True      # This makes the Base model abstract, meaning it won't be created as a database table. Instead, it's used as a base class for other models.

class Curso(Base):
    titulo = models.CharField(max_length=255)
    url=models.URLField(unique=True) # Each curso must have one URL and cannot repeate

    class Meta:
        verbose_name = 'Curso'          # Specifies the singular name for the model.
        verbose_name_plural = 'Cursos'  # Specifies the plural name for the model.
        ordering = ['id']               # Pelo que quermos ordenar? Ordenamento global e vale para todo projeto

    def __str__(self):       # This method returns the titulo of the Curso when its instance is converted to a string
        return self.titulo

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField() # We can validate the data with the programing itself... this field will only receive an email
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1) # Defines that it can have number and one decimal field

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Acaliações"
        unique_together = ['email', 'curso']
        ordering = ['-id']               # Pelo que quermos ordenar? Invertido

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'