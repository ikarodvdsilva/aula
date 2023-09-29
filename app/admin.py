from django.contrib import admin

from .models import Aluno, Aula, Disciplina, Turma, Professor

admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Aula)
admin.site.register(Aluno)
admin.site.register(Professor)
