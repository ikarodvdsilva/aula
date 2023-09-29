from django.db import models
from django.contrib.auth.models import User


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField(unique=True)
    senha = models.CharField(max_length=255)


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField(unique=True)
    senha = models.CharField(max_length=255)


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)


class Aula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)


class AvaliacaoAula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    data = models.DateField()
    nota = models.PositiveIntegerField(choices=zip(range(11), range(11)))  # De 0 a 10
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)


class Coordenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    senha_padrao = models.CharField(max_length=255)
