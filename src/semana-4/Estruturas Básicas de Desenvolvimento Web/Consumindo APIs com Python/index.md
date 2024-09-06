# Aula: Consumindo APIs REST em Python

## Objetivo
Nesta aula, vamos aprender como consumir APIs REST utilizando a biblioteca `requests` do Python. Vamos abordar desde o básico, como fazer requisições simples, até o uso de autenticação e manipulação de dados retornados no formato JSON.

---

## 1. Introdução ao `requests`

A biblioteca `requests` é uma das mais populares em Python para fazer requisições HTTP de maneira simples e eficiente.

### Instalando o requests

Para instalar o `requests`, execute o seguinte comando:
```bash
pip install requests
```

### Fazendo uma requisição GET simples

Aqui está um exemplo de como fazer uma requisição GET a uma API pública que retorna uma piada aleatória:

```python
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()

print(data["value"])
```

### Explicação:
- `requests.get()`: Envia uma requisição GET à URL especificada.
- `response.json()`: Converte a resposta em um objeto Python (dicionário) ao interpretar o JSON.

---

## 2. Requisições POST

Requisições `POST` são usadas para enviar dados para o servidor. Vamos enviar dados em formato JSON para uma API de teste.

### Exemplo de uma requisição POST

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.json())
```

### Explicação:
- `requests.post()`: Envia uma requisição POST para a URL especificada.
- O parâmetro `json=data` envia os dados no formato JSON.

---

## 3. Autenticação e Headers

Algumas APIs exigem autenticação para serem acessadas. Normalmente, isso é feito com tokens de API.

### Exemplo de requisição GET com token de autenticação

```python
import requests

url = "https://api.github.com/user"
token = "seu_token_aqui"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)
print(response.json())
```

### Explicação:
- `headers`: Contém a chave de autenticação passada no formato `Bearer`.
- Requisições autenticadas permitem acesso a dados privados de APIs, como no exemplo do GitHub.

---

## 4. Manipulação de Dados Retornados

Normalmente, os dados retornados por APIs REST são no formato JSON. O método `response.json()` converte a resposta para um dicionário Python.

### Exemplo de manipulação de dados

```python
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()

# Acessando a piada
print(f"Piada: {data['value']}")

# Acessando a URL da imagem do ícone
print(f"Ícone: {data['icon_url']}")
```

---

## 5. Tratamento de Erros

Durante as requisições, é importante tratar erros adequadamente, como o código de status HTTP.

### Exemplo de tratamento de erros

```python
import requests

url = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(url)
    response.raise_for_status()  # Levanta exceção para códigos de erro
    data = response.json()
    print(data["value"])
except requests.exceptions.HTTPError as err:
    print(f"Erro HTTP: {err}")
except Exception as err:
    print(f"Erro: {err}")
```

### Explicação:
- `response.raise_for_status()`: Levanta uma exceção para códigos de status HTTP indicando erro (ex.: 404, 500).
- Tratamento genérico para exceções inesperadas.

---

### 6. Passando Parâmetros na URL

Algumas APIs permitem que você passe parâmetros como query strings. O `requests` facilita o envio desses parâmetros.

### Exemplo de envio de parâmetros

Vamos utilizar a **Bored API**, que oferece atividades aleatórias com a opção de especificar o tipo de atividade que você deseja.

```python
import requests

url = "https://www.boredapi.com/api/activity"
params = {
    "type": "recreational"  # Podemos filtrar pelo tipo de atividade
}

response = requests.get(url, params=params)
data = response.json()

print(f"Atividade sugerida: {data['activity']}")
```

### Explicação:

- O parâmetro `params` permite enviar dados na URL como query strings (ex.: `?type=recreational`).
- A resposta é um JSON com uma sugestão de atividade que corresponde ao tipo solicitado.

---

## 7. Conclusão e Boas Práticas

### Boas Práticas ao consumir APIs:
1. **Tratar exceções**: Sempre trate possíveis erros de rede ou de requisição.
2. **Respeitar limites de requisições**: Muitas APIs impõem limites de requisições por minuto/hora.
3. **Leitura da documentação**: Entender as funcionalidades e limites da API usada.

---