## Avançando nos templates

Iremos ver algumas implementações que conseguimos fazer dentro do próprio template, condições, iterações, e apresentações de informação

Na view já criada, crie uma variavel com o nome de contexto, e passe ela para o template:

```python
from django.shortcuts import render

def teste(request):
    contexto = {
        'mensagem': 'Olá, bem-vindo ao meu site!',
        'usuario': 'Leonardo',
        'idade': 25,
        'usuarios': [
            {'nome': 'Leonardo', 'idade': 50},
            {'nome': 'Maria', 'idade': 30},
            {'nome': 'João', 'idade': 22},
        ]
    }
    return render(request, 'nome_do_template.html', contexto)
```

No template iremos conseguir apresentar as informações, usando o nome das variaveis passado no contexto:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Teste de Contexto</title>
    </head>
    <body>
        <h1>{{ mensagem }}</h1>
        <p>Usuário: {{ usuario }}</p>
        <p>Idade: {{ idade }}</p>
    </body>
</html>
```

Também iremos conseguir percorrer o array criado no contexto:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Teste de Contexto</title>
    </head>
    <body>
        {% for usuario in usuarios %}
	        <li>{{ usuario.nome }} - {{ usuario.idade }} anos</li>
        {% endfor %}
    </body>
</html>
```

Podemos também fazer condições para saber se a variável está preenchida, ou está setada como None:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Teste de Contexto</title>
    </head>
    <body>
        <p>
	    {% if usuario %}
	        Usuário: {{ usuario }}
	    {% else %}
	        Usuário não encontrado.
	    {% endif %}
        </p>
    </body>
</html>
```

<br />
<br />
<br />

## Criando um novo App do Django

Execute o comando no terminal

```cmd
python manage.py startapp nome_app
```

Dentro do settings.py procure a variável INSTALLED_APPS e adicione o app que você criou dentro do array

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nome_app',
]
```

Você verá uma pasta com o nome que você criou, porém já com os arquivos necessários para criar seu models, views e urls. :)


Um pouco de models

No app que você criou, provavelmente deve ter visto um arquivo chamado models.py, nele você irá criar o seu model para fazer alteração no seu banco de dados, irá ficar semelhante a isso:

```python
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    texto_exemplo = models.TextField(blank=True, null=True)

    def __str__(self):
        return  self.nome

```

Após fazer a criação do model, para realizar as alterações no banco de dados basta executar dois comandos:

```cmd
python manage.py makemigrations (que irá criar os arquivos de migração)

python manage.py migrate (que irá aplicar de fato as alterações no banco de dados)
```

Após isso, você consegue persistir os dados, manipular, etc, da forma que você quiser:

Criando:
```python
    aluno = Aluno(nome='leo', texto_exemplo='teste de texto')
    aluno.save()
```
Buscando:
```python
    aluno = Aluno.objects.get(nome='leo')
```

Alterando:
```python
    aluno = Aluno.objects.get(nome='leo')
    aluno.texto_exemplo = 'mudei'
    aluno.save()

```
Deletando:
```python
    aluno = Aluno.objects.get(nome='leo')
    aluno.delete()
```