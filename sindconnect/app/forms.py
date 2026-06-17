from django import forms
from .models import Socio
from .models import Mensalidade, Pagamento

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = [
            'nome',
            'cpf',
            'rg',
            'data_nascimento',
            'sexo',
            'endereco',
            'telefone',
            'email',
            'cargo_funcao',
            'data_filiacao',
            'documentos',
        ]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cargo_funcao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_filiacao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'documentos': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
class MensalidadeForm(forms.ModelForm):

    class Meta:
        model = Mensalidade
        fields = [
            'categoria',
            'competencia',
            'valor'
        ]

        widgets = {
            'categoria': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'competencia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '06/2026'
                }
            ),

            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),
        }
class PagamentoForm(forms.ModelForm):

    class Meta:
        model = Pagamento
        fields = [
            'socio',
            'mensalidade',
            'competencia_paga',
            'valor_pago',
            'data_pagamento'
        ]

        widgets = {

            'socio': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'mensalidade': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'competencia_paga': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '06/2026'
                }
            ),

            'valor_pago': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'data_pagamento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }