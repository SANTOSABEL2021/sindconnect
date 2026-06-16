from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.shortcuts import redirect


from .forms import SocioForm


def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')
def login_usuario(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user)

            if user.groups.filter(name="Socio").exists():
                return redirect("home_socio")

            elif user.groups.filter(name="Atendente").exists():
                return redirect("home_atendente")

            else:
                messages.error(request, "Usuário sem grupo definido.")
                return redirect("login")

        else:
            messages.error(request, "CPF/E-mail ou senha inválidos.")

    return render(request, "login.html")



def home_atendente(request):
    return render(request, "home_atendente.html")


@login_required
def home_socio(request):
    return render(request, 'home_socio.html')


@login_required
def socio_dados(request):
    return render(request, 'socio_dados.html')


@login_required
def socio_documentos(request):
    return render(request, 'socio_documentos.html')


@login_required
def socio_mensalidades(request):
    return render(request, 'socio_mensalidades.html')


@login_required
def socio_pagamentos(request):
    return render(request, 'socio_pagamentos.html')

@login_required
def home_atendente(request):
    return render(request, 'home_atendente.html')


@login_required
def cadastro_socio(request):
    return render(request, 'cadastro_socio.html')


@login_required
def consulta_socio(request):
    return render(request, 'consulta_socio.html')


@login_required
def atualizacao_cadastral(request):
    return render(request, 'atualizacao_cadastral.html')


@login_required
def mensalidades(request):
    return render(request, 'mensalidades.html')


@login_required
def pagamentos(request):
    return render(request, 'pagamentos.html')


@login_required
def usuarios(request):
    return render(request, 'usuarios.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def cadastrar_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_socios')
    else:
        form = SocioForm()

    return render(request, 'cadastrar_socio.html', {'form': form})

def listar_socios(request):
    socios = Socio.objects.all()
    return render(request, 'listar_socios.html', {'socios': socios})
