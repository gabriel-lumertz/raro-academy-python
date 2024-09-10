# Teste: Implementação de Proxy para uma API Pública

## Descrição

Você receberá uma aplicação Flask com as rotas CRUD já definidas, mas sem nenhuma implementação. Seu objetivo é implementar um proxy que consuma dados de uma API pública e os exponha através das rotas definidas.

### Objetivo

- Implementar um proxy que faça chamadas a uma API pública, processe as respostas e as retorne para as rotas da aplicação Flask.
- Garantir que a implementação passe nos testes unitários fornecidos.

## Instruções

1. **Implementação do Proxy**:
   - Utilize a API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/).
   - Faça chamadas HTTP a essa API dentro das rotas definidas no Flask.
   - Retorne as respostas da API pública para as rotas correspondentes (GET, POST, PUT, DELETE).

2. **Testes Unitários**:
   - Os testes unitários estão definidos usando `pytest`. Eles verificam se as rotas estão funcionando corretamente.
   - Garanta que os testes passem ao implementar o proxy.
   - Utilize o comando `pytest` dentro do diretorio para rodar os testes.

3. **Estrutura do projeto**:
   - O projeto deve seguir a seguinte estrrutura:
    ```bash
    meu_projeto/
    ├── main.py
    ├── test_api.py
    ├── venv/  # Se você estiver usando um ambiente virtual / esse diretório não deve estar no seu repo
    ├── .gitignore
    └── requirements.txt
    ```
   - Caso seja utilizada alguma lib externa, colocar no arquivo `requirements.txt`.

---

## API Pública Sugerida

Para facilitar, você pode usar a API [JSONPlaceholder](https://jsonplaceholder.typicode.com/), que fornece endpoints para simular dados de posts, usuários, comentários, etc.

### Endpoints Úteis

- **GET** `/posts`: Retorna todos os posts.
- **GET** `/posts/{id}`: Retorna um post por ID.
- **POST** `/posts`: Cria um novo post.
- **PUT** `/posts/{id}`: Atualiza um post por ID.
- **DELETE** `/posts/{id}`: Deleta um post por ID.

---

## Dicas

1. Use a biblioteca `requests` para fazer chamadas HTTP para a API pública.
2. Teste cada rota manualmente antes de rodar os testes automatizados para garantir que o fluxo básico está funcionando.
3. Verifique a documentação da API pública escolhida para garantir que você está enviando e recebendo os dados no formato correto (JSON, headers, etc.).

---

## Critérios de Avaliação

- Implementação correta das chamadas HTTP ao proxy.
- Sucesso nos testes unitários fornecidos.
- Clareza e organização do código.

Boa sorte!