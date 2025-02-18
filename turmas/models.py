from django.db import models
from django.utils.timezone import now
from django.core.mail import send_mail

class Turma(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    PAGAMENTO_CHOICES = [
        ('mensal', 'Mensal'),
        ('por_aula', 'Por Aula')
    ]

    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    forma_pagamento = models.CharField(max_length=10, choices=PAGAMENTO_CHOICES, default='mensal')

    def __str__(self):
        return f"{self.nome} ({self.turma})"

class Horario(models.Model):
    DIA_SEMANA_CHOICES = [
        ('Segunda', 'Segunda-feira'),
        ('Terça', 'Terça-feira'),
        ('Quarta', 'Quarta-feira'),
        ('Quinta', 'Quinta-feira'),
        ('Sexta', 'Sexta-feira'),
        ('Sábado', 'Sábado'),
    ]
    
    dia = models.CharField(max_length=10, choices=DIA_SEMANA_CHOICES)
    horario = models.TimeField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dia} - {self.horario} → {self.turma}"

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=False)  # Novo campo para marcar presença
    pago = models.BooleanField(default=False)     # Novo campo para marcar pagamento
    
    @property
    def mes_group(self):
        return self.data.strftime('%Y-%m')
    
    def __str__(self):
        return f"{self.aluno} - {self.data} - {self.horario} (Presente: {self.presente}, Pago: {self.pago})"

# Removemos o modelo Pagamento

# Função para enviar lembretes de pagamento
def enviar_lembretes():
    """ Envia lembretes para alunos que ainda não pagaram as 9 aulas obrigatórias. """
    from datetime import date
    hoje = date.today()
    mes_atual = hoje.month
    ano_atual = hoje.year

    alunos = Aluno.objects.all()
    for aluno in alunos:
        # Agora verificamos as presenças pagas no mês
        presencas_pagas = Presenca.objects.filter(aluno=aluno, data__month=mes_atual, data__year=ano_atual, pago=True).count()
        if presencas_pagas < 9:
            faltam_pagar = 9 - presencas_pagas
            send_mail(
                subject="Lembrete de Pagamento de Aulas",
                message=f"Olá {aluno.nome}, você ainda precisa pagar {faltam_pagar} aulas este mês.",
                from_email="admin@escola.com",
                recipient_list=[aluno.email],
                fail_silently=False
            )