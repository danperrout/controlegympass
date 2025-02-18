from django.contrib import admin
from .models import Turma, Aluno, Horario, Presenca

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome_emojis', 'quantidade_alunos')
    search_fields = ('nome',)

    def nome_emojis(self, obj):
        return f"🏫 {obj.nome}"
    nome_emojis.short_description = "Turma"

    def quantidade_alunos(self, obj):
        return f"👥 {obj.aluno_set.count()} alunos"
    quantidade_alunos.short_description = "Quantidade de Alunos"

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_emojis', 'turma_emojis', 'email', 'forma_pagamento_emojis')
    list_filter = ('turma', 'forma_pagamento')
    search_fields = ('nome', 'email')

    def nome_emojis(self, obj):
        return f"👤 {obj.nome}"
    nome_emojis.short_description = "Aluno"

    def turma_emojis(self, obj):
        return f"🏫 {obj.turma.nome}" if obj.turma else "🚫 Sem Turma"
    turma_emojis.short_description = "Turma"

    def forma_pagamento_emojis(self, obj):
        if obj.forma_pagamento == 'mensal':
            return "💳 Mensal"
        elif obj.forma_pagamento == 'por_aula':
            return "💵 Por Aula"
        return "🚫 Desconhecido"
    forma_pagamento_emojis.short_description = "Forma de Pagamento"

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('dia_emojis', 'horario_formatado', 'turma_emojis')
    list_filter = ('dia', 'turma')
    search_fields = ('turma__nome',)

    def dia_emojis(self, obj):
        dias_emojis = {
            'Segunda': '📅 Segunda-feira',
            'Terça': '📅 Terça-feira',
            'Quarta': '📅 Quarta-feira',
            'Quinta': '📅 Quinta-feira',
            'Sexta': '📅 Sexta-feira',
            'Sábado': '📅 Sábado',
        }
        return dias_emojis.get(obj.dia, obj.dia)
    dia_emojis.short_description = "Dia da Semana"

    def horario_formatado(self, obj):
        return f"⏰ {obj.horario.strftime('%H:%M')}"
    horario_formatado.short_description = "Horário"

    def turma_emojis(self, obj):
        return f"🏫 {obj.turma.nome}"
    turma_emojis.short_description = "Turma"

@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
    list_display = ('aluno_emojis', 'horario_emojis', 'data_formatada', 'status_presenca', 'status_pagamento')
    list_filter = ('data', 'horario__turma', 'pago', 'presente')
    search_fields = ('aluno__nome', 'horario__turma__nome')

    def aluno_emojis(self, obj):
        return f"👤 {obj.aluno.nome}"
    aluno_emojis.short_description = "Aluno"

    def horario_emojis(self, obj):
        return f"⏰ {obj.horario.dia} - {obj.horario.horario.strftime('%H:%M')}"
    horario_emojis.short_description = "Horário"

    def data_formatada(self, obj):
        return f"📅 {obj.data.strftime('%d/%m/%Y')}"
    data_formatada.short_description = "Data"

    def status_presenca(self, obj):
        return "✅ Presente" if obj.presente else "❌ Ausente"
    status_presenca.short_description = "Status de Presença"

    def status_pagamento(self, obj):
        return "💰 Pago" if obj.pago else "💸 Não Pago"
    status_pagamento.short_description = "Status de Pagamento"

    # Adicionando estilos CSS para melhorar a aparência
    class Media:
        css = {
            'all': ('css/admin_presenca.css',)  # Arquivo CSS personalizado
        }