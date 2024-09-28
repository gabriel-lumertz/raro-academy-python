"""
URL configuration for curso_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from curso.views import (
    # criar_turma,
    criar_turma_formulario,
    listar_turma,
    criar_professor,
    criar_professor_formulario,
    CriarTurmaView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    # path(
    #     'criar-turma/',
    #     criar_turma,
    #     name='criar_turma'
    # ),
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    path(
        'criar-turma/',
        CriarTurmaView.as_view(),
        name='criar_turma'
    ),
    path(
        'criar-turma-formulario/',
        criar_turma_formulario,
        name='criar_turma_formulario'
    ),
    path(
        'listar-turma/',
        listar_turma,
        name='listar_turma'
    ),
    path(
        'criar-professor-formulario/',
        criar_professor_formulario,
        name='criar_professor_formulario'),
    path(
        'criar-professor/',
        criar_professor,
        name='criar_professor'
    )
]
