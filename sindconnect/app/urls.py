from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_usuario, name='login_usuario'),

    # PAGINAS PRINCIPAIS
    path('home-socio/', views.home_socio, name='home_socio'),
    path('home-atendente/', views.home_atendente, name='home_atendente'),

    path('socio/home/', views.home_socio, name='home_socio'),
    path('socio/dados/', views.socio_dados, name='socio_dados'),
    path('socio/documentos/', views.socio_documentos, name='socio_documentos'),
    path('socio/mensalidades/', views.socio_mensalidades, name='socio_mensalidades'),
    path('socio/pagamentos/', views.socio_pagamentos, name='socio_pagamentos'),
    path('socios/', views.lista_socios, name='lista_socios'),
    path('socios/editar/<int:id>/', views.editar_socio,name='editar_socio'),
    path('socios/excluir/<int:id>/', views.excluir_socio, name='excluir_socio'),

    path('atendente/home/',views.home_atendente,name='home_atendente' ),
    path('atendente/cadastro-socio/',views.cadastro_socio, name='cadastro_socio'),
    path('atendente/consulta-socio/',views.consulta_socio,name='consulta_socio'),
    path('atendente/usuarios/',views.usuarios, name='usuarios'),
    path('atendente/dashboard/', views.dashboard, name='dashboard' ),

    # MENSALIDADES
    path('mensalidades/', views.lista_mensalidades, name='lista_mensalidades' ),
    path('mensalidades/cadastrar/', views.cadastro_mensalidade, name='cadastro_mensalidade'  ),
    path('mensalidades/editar/<int:id>/', views.editar_mensalidade, name='editar_mensalidade' ),
    path('mensalidades/excluir/<int:id>/',views.excluir_mensalidade, name='excluir_mensalidade' ),

    # PAGAMENTOS
    path('pagamentos/',views.lista_pagamentos, name='lista_pagamentos' ),
    path('pagamentos/cadastrar/', views.cadastro_pagamento,name='cadastro_pagamento'),
    path('pagamentos/editar/<int:id>/',views.editar_pagamento, name='editar_pagamento' ),
    path('pagamentos/excluir/<int:id>/', views.excluir_pagamento, name='excluir_pagamento'),

    # LOGOUT
    path('logout/', views.logout_usuario, name='logout'),

]