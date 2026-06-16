from django.db import models


class Socio(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


