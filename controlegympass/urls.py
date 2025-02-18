"""
URL configuration for controlegympass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from turmas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("alunos/", views.lista_alunos, name="lista_alunos"),
    path("perfil/<int:aluno_id>/", views.perfil_aluno, name="perfil_aluno"),
    path("horarios/", views.horarios, name="horarios"),
    path("turmas/", views.lista_turmas, name="lista_turmas"),
    path("turmas/adicionar/", views.adicionar_turma, name="adicionar_turma"),
    path("turmas/remover/<int:turma_id>/", views.remover_turma, name="remover_turma"),
    path("presencas/", views.registrar_presenca, name="registrar_presenca"),
    path("calendario/", views.calendario_presencas, name="calendario_presencas"),
    path('listar-presencas/', views.listar_presencas, name='listar_presencas'), 
    # path("pagamentos/", views.listar_pagamentos, name="listar_pagamentos"),
    # path("pagamentos/registrar/", views.registrar_pagamento, name="registrar_pagamento"),
    path("calendario/<int:ano>/<int:mes>/", views.calendario_geral, name="calendario_geral"),
    path("calendario/<int:ano>/<int:mes>/aluno/<int:aluno_id>/", views.calendario_aluno, name="calendario_aluno"),
]



