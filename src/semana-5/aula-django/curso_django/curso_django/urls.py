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
from curso.views import acesso_curso, acesso_curso_template, acesso_curso_template_contexto, criar_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acesso/', acesso_curso),
    path('acesso-template/', acesso_curso_template),
    path('acesso-template-contexto/', acesso_curso_template_contexto, name='listagem_alunos'),
    path('criar-aluno/', criar_aluno, name='criar_aluno')
]
