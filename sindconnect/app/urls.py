from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_usuario, name='login_usuario'),


    path('home-socio/', views.home_socio, name='home_socio'),
    path('home-atendente/', views.home_atendente, name='home_atendente'),

    path('socio/home/', views.home_socio, name='home_socio'),
    path('socio/dados/', views.socio_dados, name='socio_dados'),
    path('socio/documentos/', views.socio_documentos, name='socio_documentos'),
    path('socio/mensalidades/', views.socio_mensalidades, name='socio_mensalidades'),
    path('socio/pagamentos/', views.socio_pagamentos, name='socio_pagamentos'),

    path('atendente/home/',views.home_atendente,name='home_atendente' ),

    path('atendente/cadastro-socio/',views.cadastro_socio, name='cadastro_socio'),

    path('atendente/consulta-socio/',views.consulta_socio,name='consulta_socio'),

    path('atendente/atualizacao-cadastral/',views.atualizacao_cadastral,name='atualizacao_cadastral'),

    path('atendente/mensalidades/',views.mensalidades,name='mensalidades'),

    path('atendente/pagamentos/',views.pagamentos,name='pagamentos'),

    path('atendente/usuarios/',views.usuarios, name='usuarios'),

    path('atendente/dashboard/', views.dashboard, name='dashboard' ),

    path('logout/',views.logout_usuario, name='logout'),
    path('socios/cadastrar/', views.cadastrar_socio, name='cadastrar_socio'),

]