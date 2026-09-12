from django import forms
from .models import Paciente, Medico, Exame, Medicao, TemplateLaudo 


class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['paciente_id', 'medico_id', 'data_exame', 'observacoes']


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'idade', 'sexo', 'cpf'] 