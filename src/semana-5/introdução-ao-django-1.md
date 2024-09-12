Comece criando uma nova virtualenv

```cmd
python -m venv nome_venv
```

Ative a sua virtual env

```cmd
.\{nome_venv}\Scripts\activate OU {nome_venv}\Scripts\activate.bat se for no prompt

```

Após isso, faça a instalação do Django com o pip e com a virtualenv ativada

```cmd
pip install django
```

Verifique se foi instalado com sucesso

```cmd
django-admin --version
```

Agora para criar um novo projeto Django basta apenas digitar o comando no terminal

```cmd
django-admin startproject nome_do_projeto
```

Entre no Projeto e execute o comando para rodar o Django

```cmd
cd nome_projeto #para entrar na pasta
python manage.py runserver
```

Para criar uma nova view, dentro da pasta principal do projeto(é o nome do projeto que você criou), crie um arquivo views.py e crie uma função que será a sua view

```python
from django.http import HttpResponse


def teste(request):
    return HttpResponse("Teste teste")
```

e no urls.py crie uma nova URL, e irá ficar dessa forma:

```python
from django.contrib import admin
from django.urls import path
from .views import teste

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste)
]
```


Acesse a url http://localhost:8000/teste no seu navegador e verá seu projeto Django em execução com a view que você criou :)



<br />

# Template básico

crie uma nova pasta na raíz do seu projeto e crie um arquivo html dentro dessa pasta

```cmd
nome_projeto/
    templates/
        nome_template.html
```

no template coloque algo de sua preferência, mas que seja em HTML, exemplo:

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meu Projeto Django</title>
    </head>
    <body>
        <h1>Bem-vindo ao meu site Django</h1>
    </body>
</html>

```

no settings.py adiciona a seguinte lib no topo

```python
import os
```

adicione na variavel de template, no DIRS o seguinte:

```python
os.path.join(BASE_DIR, 'templates')
```

dessa forma a variavel irá ficar assim:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Na view que já está criada(ou você pode criar uma nova) faça a importação do pacote render e retorne na view o seu template, que irá ficar assim:

```python
from django.shortcuts import render

def teste(request):
    return render(request, 'teste.html')
```

Abra o seu navegador na url http://localhost:8000/teste e verá o seu template renderizado