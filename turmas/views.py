
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Turma, Aluno, Horario, Presenca
from .forms import TurmaForm, PresencaForm
from datetime import date
import calendar
from collections import defaultdict
from django.urls import reverse

from django.shortcuts import render, get_object_or_404
from .models import Aluno, Presenca

def perfil_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    presencas = Presenca.objects.filter(aluno=aluno)
    
    context = {
        'aluno': aluno,
        'presencas': presencas,
    }
    return render(request, 'perfil_aluno.html', context)

@login_required
def x_perfil_aluno(request, aluno_id):
    """ Exibe o perfil do aluno e lista todos os meses em que ele teve aula, incluindo a quantidade de presenças. """
    aluno = get_object_or_404(Aluno, id=aluno_id)

    # Criar defaultdict(dict) para armazenar os anos, meses e quantidade de presenças
    presencas_por_mes = defaultdict(lambda: defaultdict(int))

    # Buscar todas as presenças do aluno
    presencas = Presenca.objects.filter(aluno=aluno).order_by("data")

    # Popular o defaultdict com os anos, meses e contagem de presenças
    for presenca in presencas:
        presencas_por_mes[presenca.data.year][presenca.data.month] += 1

    # ✅ Converter defaultdict para um dicionário normal para ser usado no template
    presencas_por_mes = {ano: dict(meses) for ano, meses in presencas_por_mes.items()}

    return render(request, "perfil_aluno.html", {
        "aluno": aluno,
        "presencas_por_mes": presencas_por_mes,
    })


def listar_presencas(request):
    # Ordena as presenças por aluno e por data
    presencas = Presenca.objects.all().order_by('aluno__nome', 'data')
    context = {
        'presencas': presencas,
    }
    return render(request, 'listar_presencas.html', context)

def registrar_pagamento(request):
    if request.method == "POST":
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "💰 Pagamento registrado com sucesso!")
            return redirect("listar_pagamentos")
        else:
            messages.error(request, "❌ Erro ao registrar pagamento. Verifique os dados.")
    
    form = PagamentoForm()
    return render(request, "registrar_pagamento.html", {"form": form})


def home(request):
    turmas = Turma.objects.all()
    alunos = Aluno.objects.all()
    
    context = {
        'turmas': turmas,
        'alunos': alunos,
    }
    return render(request, 'home.html', context)

def calendario_geral(request, ano, mes):
    """ Exibe o calendário de presença de todos os alunos em um determinado mês. """
    _, num_dias = calendar.monthrange(ano, mes)
    dias = range(1, num_dias + 1)
    print(f"Ano: {ano}, Mês: {mes}")
    
    presencas = Presenca.objects.filter(data__year=ano, data__month=mes)
    print(presencas)
    alunos = Aluno.objects.all()
    print(alunos)
    presencas_por_dia = {dia: [] for dia in dias}
    for presenca in presencas:
        presencas_por_dia[presenca.data.day].append(presenca.aluno)
    print(presencas_por_dia)
    return render(request, "calendario.html", {
        "ano": ano, "mes": mes, "dias": dias, "presencas_por_dia": presencas_por_dia, "alunos": alunos
    })

def calendario_aluno(request, ano, mes, aluno_id):
    """ Exibe o calendário de presença de um aluno específico. """
    aluno = get_object_or_404(Aluno, id=aluno_id)
    _, num_dias = calendar.monthrange(ano, mes)
    dias = range(1, num_dias + 1)
    
    presencas = Presenca.objects.filter(aluno=aluno, data__year=ano, data__month=mes)
    presencas_por_dia = {dia: False for dia in dias}
    print(presencas)
    for presenca in presencas:
        presencas_por_dia[presenca.data.day] = True
    print(type(presencas_por_dia))
    return render(request, "calendario_aluno.html", {
        "ano": ano, "mes": mes, "dias": dias, "presencas_por_dia": presencas_por_dia, "aluno": aluno
    })


def listar_pagamentos(request):
    hoje = date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year

    alunos = Aluno.objects.all()
    pagamentos = []
    for aluno in alunos:
        aulas_pagas = Pagamento.aulas_pagas_no_mes(aluno, mes_atual, ano_atual)
        pagamentos.append({
            'aluno': aluno,
            'aulas_pagas': aulas_pagas,
            'faltando': max(0, 9 - aulas_pagas)
        })

    return render(request, "pagamentos.html", {"pagamentos": pagamentos})

from django.shortcuts import render, redirect
from .models import Aluno, Horario, Presenca
from .forms import RegistrarPresencaForm

def registrar_presenca(request):
    if request.method == 'POST':
        form = RegistrarPresencaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrarPresencaForm()
    
    context = {
        'form': form,
    }
    return render(request, 'registrar_presenca.html', context)


def calendario_presencas(request):
    hoje = date.today()
    presencas = Presenca.objects.all().order_by("data")
    return render(request, "calendario.html", {"presencas": presencas, "hoje": hoje})

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, "alunos.html", {"alunos": alunos})

def horarios(request):
    horarios = Horario.objects.all().order_by("dia", "horario")
    return render(request, "horarios.html", {"horarios": horarios})


def lista_turmas(request):
    turmas = Turma.objects.all()
    return render(request, "turmas.html", {"turmas": turmas})

def adicionar_turma(request):
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_turmas")
    else:
        form = TurmaForm()
    return render(request, "adicionar_turma.html", {"form": form})



def remover_turma(request, turma_id):
    turma = Turma.objects.get(id=turma_id)
    turma.delete()
    messages.warning(request, f"⚠️ A turma {turma.nome} foi removida!")
    return redirect("lista_turmas")

