
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from django.contrib.auth import logout

from django.shortcuts import render, redirect, get_object_or_404
from .models import Socio
from .forms import SocioForm
from django.db.models import Q

from .models import Mensalidade, Pagamento
from .forms import MensalidadeForm, PagamentoForm
from django.shortcuts import render, redirect, get_object_or_404

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
def consulta_socio(request):
    return render(request, 'consulta_socio.html')


@login_required
def atualizacao_cadastral(request):
    return render(request, 'atualizacao_cadastral.html')





@login_required
def usuarios(request):
    return render(request, 'usuarios.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')




@login_required
def cadastro_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST, request.FILES)

        if form.is_valid():
            socio = form.save()

            username = socio.cpf
            senha_padrao = socio.cpf

            user, criado = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': socio.nome,
                    'email': socio.email,
                    'is_active': True
                }
            )

            if criado:
                user.set_password(senha_padrao)
                user.save()

            grupo_socio = Group.objects.get(name='Socio')
            user.groups.add(grupo_socio)

            return redirect('lista_socios')
    else:
        form = SocioForm()

    return render(request, 'cadastro_socio.html', {'form': form})


@login_required
def lista_socios(request):
    socios = Socio.objects.all().order_by('nome')

    return render(
        request,
        'lista_socios.html',
        {'socios': socios}
    )



@login_required
def editar_socio(request, id):

    socio = get_object_or_404(Socio, id=id)

    if request.method == 'POST':
        form = SocioForm(
            request.POST,
            request.FILES,
            instance=socio
        )

        if form.is_valid():
            form.save()
            return redirect('lista_socios')

    else:
        form = SocioForm(instance=socio)

    return render(
        request,
        'editar_socio.html',
        {
            'form': form,
            'socio': socio
        }
    )

@login_required
def consulta_socio(request):

    pesquisa = request.GET.get('q')

    socios = Socio.objects.all()

    if pesquisa:

        socios = socios.filter(
            Q(nome__icontains=pesquisa) |
            Q(cpf__icontains=pesquisa)
        )

    return render(
        request,
        'consulta_socio.html',
        {
            'socios': socios
        }
    )

@login_required
def excluir_socio(request, id):
    socio = get_object_or_404(Socio, id=id)

    if request.method == 'POST':
        socio.delete()
        return redirect('lista_socios')

    return render(request, 'excluir_socio.html', {'socio': socio})

@login_required
def lista_mensalidades(request):
    mensalidades = Mensalidade.objects.all().order_by('-id')

    return render(request, 'lista_mensalidades.html', {
        'mensalidades': mensalidades
    })


@login_required
def cadastro_mensalidade(request):
    if request.method == 'POST':
        form = MensalidadeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_mensalidades')
    else:
        form = MensalidadeForm()

    return render(request, 'cadastro_mensalidade.html', {
        'form': form
    })


@login_required
def editar_mensalidade(request, id):
    mensalidade = get_object_or_404(Mensalidade, id=id)

    if request.method == 'POST':
        form = MensalidadeForm(request.POST, instance=mensalidade)

        if form.is_valid():
            form.save()
            return redirect('lista_mensalidades')
    else:
        form = MensalidadeForm(instance=mensalidade)

    return render(request, 'editar_mensalidade.html', {
        'form': form,
        'mensalidade': mensalidade
    })


@login_required
def excluir_mensalidade(request, id):
    mensalidade = get_object_or_404(Mensalidade, id=id)

    if request.method == 'POST':
        mensalidade.delete()
        return redirect('lista_mensalidades')

    return render(request, 'excluir_mensalidade.html', {
        'mensalidade': mensalidade
    })

@login_required
def lista_pagamentos(request):
    pagamentos = Pagamento.objects.all().order_by('-id')

    return render(request, 'lista_pagamentos.html', {
        'pagamentos': pagamentos
    })


@login_required
def cadastro_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_pagamentos')
    else:
        form = PagamentoForm()

    return render(request, 'cadastro_pagamento.html', {
        'form': form
    })


@login_required
def editar_pagamento(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)

    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)

        if form.is_valid():
            form.save()
            return redirect('lista_pagamentos')
    else:
        form = PagamentoForm(instance=pagamento)

    return render(request, 'editar_pagamento.html', {
        'form': form,
        'pagamento': pagamento
    })


@login_required
def excluir_pagamento(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)

    if request.method == 'POST':
        pagamento.delete()
        return redirect('lista_pagamentos')

    return render(request, 'excluir_pagamento.html', {
        'pagamento': pagamento
    })