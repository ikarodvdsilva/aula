from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Aula, AvaliacaoAula
from .forms import VotacaoAulaForm
from datetime import datetime
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import login


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response(status=status.HTTP_200_OK)


@login_required(login_url="login")
def dashboard(request):
    return render(request, "aluno/dashboard.html")


@login_required(login_url="login")
def votar_na_aula(request, aula_id):
    aula = Aula.objects.get(pk=aula_id)
    aluno = request.user.aluno
    print(request.user.username)
    if AvaliacaoAula.objects.filter(aula=aula, aluno=aluno).exists():
        messages.warning(request, "Você já votou nesta aula.")
        return redirect("dashboard")

    if request.method == "POST":
        form = VotacaoAulaForm(request.POST)
        if form.is_valid():
            nota = form.cleaned_data["nota"]
            dat_atual = datetime.now()
            AvaliacaoAula.objects.create(
                aula=aula, aluno=aluno, nota=nota, data=dat_atual
            )

            messages.success(request, "Avaliação realizada com sucesso.")
            return redirect("dashboard")
    else:
        form = VotacaoAulaForm()

    return render(request, "aluno/votar_na_aula.html", {"form": form, "aula": aula})


@login_required(login_url="login")
def historico_aulas(request):
    aluno = request.user.aluno
    historico = Aula.objects.filter(turma__alunos=aluno)
    return render(request, "aluno/historico_aulas.html", {"historico": historico})


@login_required(login_url="login")
def historico_avaliacoes(request):
    aluno = request.user.aluno
    historico = AvaliacaoAula.objects.filter(aluno=aluno)
    return render(request, "aluno/historico_avaliacoes.html", {"historico": historico})
