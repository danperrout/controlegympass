from django import forms
from .models import Turma
from .models import Presenca
from django import forms
from django import forms
from .models import Presenca

class RegistrarPresencaForm(forms.ModelForm):
    class Meta:
        model = Presenca
        fields = ['aluno', 'horario', 'data', 'presente', 'pago']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Define o tipo do campo como 'date'
        }
        
class PresencaForm(forms.ModelForm):
    class Meta:
        model = Presenca
        fields = ["aluno", "horario", "data"]

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ["nome"]

    
