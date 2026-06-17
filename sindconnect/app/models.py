from django.db import models


class Socio(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    cargo_funcao = models.CharField(max_length=100)
    data_filiacao = models.DateField()
    documentos = models.TextField(blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
class Mensalidade(models.Model):
    categoria = models.CharField(max_length=100)
    competencia = models.CharField(max_length=7)  # Exemplo: 06/2026
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.categoria} - {self.competencia}'


class Pagamento(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    mensalidade = models.ForeignKey(Mensalidade, on_delete=models.CASCADE)
    competencia_paga = models.CharField(max_length=7)  # Exemplo: 06/2026
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()

    def __str__(self):
        return f'{self.socio.nome} - {self.competencia_paga}'