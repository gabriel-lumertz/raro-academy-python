# Python Advanced Tricks

## Objetivo da Aula

Apresentar técnicas avançadas de Python que ajudam desenvolvedores a escrever código mais limpo, eficiente e Pythonico.

---

## 1. Introdução

**Por que aprender truques avançados de Python?**

- **Produtividade**: Técnicas avançadas permitem que você escreva menos código para alcançar os mesmos resultados.
- **Legibilidade**: Código mais legível é mais fácil de manter e entender.
- **Performance**: Algumas técnicas podem otimizar o tempo de execução do código.

---

## 2. Compreensões (List, Set, Dict)

### O que são?

Compreensões são uma maneira concisa e poderosa de criar listas, conjuntos e dicionários em Python, evitando a necessidade de loops explícitos. Elas permitem que você aplique expressões a uma sequência ou iterável, transformando-a em um novo objeto em uma única linha.

### Exemplos

#### List Comprehension

Cria uma lista aplicando uma expressão a cada item de uma sequência.

```python
numbers = [x**2 for x in range(10)]
print(numbers)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### Set Comprehension

Cria um conjunto (set) com base em uma expressão aplicada a cada item de uma sequência, garantindo que os elementos sejam únicos.

```python
unique_squares = {x**2 for x in range(10)}
print(unique_squares)  # {0, 1, 64, 36, 4, 9, 16, 81, 49, 25}
```

#### Dict Comprehension

Cria um dicionário aplicando uma expressão que gera pares de chave-valor a partir de uma sequência.

```python
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### Quando usar?

- Quando você precisa gerar listas, sets ou dicionários de forma mais compacta e expressiva.
- Para manipulações simples e transformações de dados.

---

## 3. Funções Anônimas (Lambdas)

### O que são?

Lambdas são funções anônimas, ou seja, funções que não precisam ser nomeadas. Elas são usadas quando uma função simples e rápida é necessária, especialmente em operações que envolvem métodos como `map()`, `filter()` e `sorted()`.

### Exemplos

#### Função lambda básica

Lambdas são definidas com a palavra-chave `lambda` seguida por seus parâmetros e a expressão que será executada.

```python
multiply = lambda x, y: x * y
result = multiply(2, 3)
print(result)  # 6
```
### Quando usar?

- Quando você precisa de uma função simples e rápida sem a necessidade de defini-la explicitamente.
- Útil com funções como `map()`, `filter()`, `sorted()`, entre outras.

---

## 4. Funções Decoradoras

### O que são?

Decorators são uma forma de adicionar funcionalidades extras a funções existentes de forma concisa e elegante. Eles permitem que você "envolva" uma função com outra função, alterando ou estendendo seu comportamento.

### Exemplo Simples

```python
def decorator(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@decorator
def say_hello():
    print("Olá!")

say_hello()
# Output:
# Antes da função
# Olá!
# Depois da função
```

Nesse exemplo, o decorator `decorator` envolve a função `say_hello()`, adicionando uma mensagem antes e depois da execução da função original.

### Quando usar?

- Adicionar lógica de pré e pós-execução em funções sem alterar seu código original.
- Utilizado em logging, validações e modificações no comportamento da função.

---

## 5. Combos Importantes

#### Usando `map()` com lambda

### O que é `map()`?

`map()` é uma função que aplica uma função a todos os itens de um iterável (como uma lista) e retorna um map object (que pode ser convertido em uma lista, set, etc.). 

#### Exemplo:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

Aqui, `map()` aplica a função lambda (`lambda x: x**2`) a cada elemento da lista `numbers`, resultando em uma nova lista de quadrados.

#### Usando `filter()` com lambda

### O que é `filter()`?

`filter()` é uma função que filtra os itens de um iterável com base em uma função que retorna True ou False para cada item. Somente os itens que fazem a função retornar True são mantidos.

#### Exemplo:

```python
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
```

Nesse caso, `filter()` aplica a função lambda (`lambda x: x % 2 == 0`) a cada elemento da lista `numbers`, retornando apenas os números que são divisíveis por 2 (ou seja, os números pares).

#### Usando `sorted()` com lambda

### O que é `sorted()`?

`sorted()` é uma função que ordena os itens de um iterável (lista, tupla, etc.) e retorna uma nova lista com os itens ordenados. A função permite o uso de um parâmetro `key` onde você pode especificar uma função para determinar a ordem de classificação.

#### Exemplo:

```python
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

sorted_students = sorted(students, key=lambda student: student['grade'], reverse=True)
print(sorted_students)
# Output:
# [{'name': 'Bob', 'grade': 92}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 78}]
```

Aqui, `sorted()` usa uma função lambda para ordenar a lista de dicionários `students` pela chave `grade` em ordem decrescente.

### `enumerate()`

### O que é?

`enumerate()` é uma função que adiciona um contador (índice) a um iterável e o retorna na forma de um objeto enumerado, que pode ser convertido em uma lista de tuplas.

#### Exemplo:

```python
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
# Output:
# 0 a
# 1 b
# 2 c
```

Aqui, `enumerate()` permite que você itere simultaneamente sobre os índices e os valores de uma lista.

### Quando usar?

- Quando você precisa tanto do índice quanto do valor dos itens em um iterável durante a iteração.

### `zip()`

### O que é?

`zip()` é uma função que combina duas ou mais sequências (listas, tuplas, etc.) em pares de tuplas, onde cada tupla contém elementos correspondentes das sequências fornecidas.

#### Exemplo:

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
# Output:
# Alice scored 85
# Bob scored 92
# Charlie scored 78
```

Aqui, `zip()` combina as listas `names` e `scores`, criando pares de nome e pontuação para cada aluno.

### Quando usar?

- Quando você precisa iterar sobre várias sequências ao mesmo tempo e deseja agrupar seus elementos correspondentes.

### Unpacking (Descompactação)

### O que é?

Unpacking, ou descompactação, é uma técnica que permite que você extraia os valores de listas ou tuplas em variáveis separadas de uma só vez.

#### Exemplo:

```python
a, b = 1, 2
print(a, b)  # 1 2
```

#### Unpacking em Loops:

```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

for number, letter in pairs:
    print(f"Number: {number}, Letter: {letter}")
# Output:
# Number: 1, Letter: a
# Number: 2, Letter: b
# Number: 3, Letter: c
```

### Quando usar?

- Quando você deseja atribuir múltiplos valores de uma vez de maneira limpa e legível.

---

## 6. Boas Práticas

- **PEP 8**: Seguir as convenções de estilo de código Python para manter o código legível.
- **Evitar Complexidade**: Lambdas e compreensões complexas podem prejudicar a leg

ibilidade. Use-os com moderação.
- **Documentação**: Sempre comente seu código, especialmente ao usar técnicas avançadas que podem não ser imediatamente óbvias.

---

## 7. Exercícios Práticos

### Exercício 1: List Comprehension

Crie uma lista de números ao quadrado para todos os números ímpares entre 1 e 20.

### Exercício 2: Funções Anônimas

Use `filter()` e uma função lambda para obter apenas os números pares de uma lista.

### Exercício 3: Funções Decoradoras

Crie um decorator que calcule o tempo de execução de uma função.

---

### Por que aprender truques avançados de Python?(Mais uma vez)

#### **Produtividade**

Técnicas avançadas em Python permitem que você escreva menos código para realizar tarefas complexas. Isso resulta em um aumento significativo na produtividade, especialmente em projetos maiores. Ao invés de escrever múltiplas linhas de código para tarefas que podem ser simplificadas, você pode usar métodos embutidos, como compreensões, funções anônimas (lambdas) e decoradores, para resolver problemas com menos esforço e maior eficiência.

**Exemplo:**
Usar uma list comprehension ao invés de um loop `for` reduz a quantidade de código e torna-o mais legível:
```python
# Sem list comprehension
squares = []
for x in range(10):
    squares.append(x**2)

# Com list comprehension
squares = [x**2 for x in range(10)]
```
A segunda versão é mais curta e clara, levando a menos erros e tempo reduzido de desenvolvimento.

#### **Legibilidade**

Um código mais legível facilita a manutenção, colaboração em equipe e expansão do projeto ao longo do tempo. Em Python, a legibilidade é uma prioridade. Truques avançados permitem que você escreva código expressivo, que comunica de forma mais clara o que está sendo feito. Isso é importante para equipes de desenvolvimento, onde o código será lido e modificado por outras pessoas no futuro.

**Exemplo:**
O uso de decorators torna mais evidente o comportamento adicional de uma função, em vez de tentar incorporar essa lógica dentro do corpo da função.

```python
@time_decorator
def minha_funcao():
    pass
```

Ao invés de misturar a lógica de cronometragem dentro da função, o decorador deixa claro o que está sendo adicionado à função original, melhorando a legibilidade e modularidade.

#### **Performance**

Aqui é onde técnicas avançadas podem brilhar em termos de otimização. Python não é a linguagem mais rápida comparada a linguagens compiladas como C ou C++, mas com o uso correto de técnicas avançadas, você pode reduzir o tempo de execução e o consumo de recursos.

1. **Compreensões:** Elas geralmente são mais rápidas que loops `for` tradicionais, pois são otimizadas internamente pela linguagem. Quando se lida com grandes volumes de dados, essa otimização pode fazer uma diferença significativa.

   **Exemplo de Comparação:**
   ```python
   # Usando um loop for
   result = []
   for x in range(1000000):
       result.append(x * 2)

   # Usando list comprehension
   result = [x * 2 for x in range(1000000)]
   ```
   O segundo exemplo, com list comprehension, é mais eficiente porque evita as chamadas de método `append()` repetitivas.

2. **Funções Embutidas:** Métodos como `map()`, `filter()`, e `sorted()` são implementados em C dentro do interpretador Python, tornando-os mais rápidos do que loops tradicionais.

   **Exemplo:**
   ```python
   # Usando map (mais eficiente)
   result = map(lambda x: x * 2, range(1000000))

   # Usando um loop for
   result = []
   for x in range(1000000):
       result.append(x * 2)
   ```
   `map()` é mais eficiente do que o loop tradicional por causa da implementação interna otimizada.

3. **Funções Decoradoras:** Ao usar decoradores para adicionar funcionalidades como cache (usando `functools.lru_cache`), você pode reduzir significativamente o tempo de execução de funções que são chamadas repetidamente com os mesmos argumentos. Isso é especialmente útil em aplicações que fazem cálculos pesados ou acessam repetidamente dados da mesma origem.

   **Exemplo com Cache:**
   ```python
   from functools import lru_cache

   @lru_cache(maxsize=100)
   def fib(n):
       if n < 2:
           return n
       return fib(n-1) + fib(n-2)

   # A segunda chamada será muito mais rápida porque o resultado será armazenado em cache
   print(fib(50))
   ```

### Resumo

- **Produtividade:** Escrever menos código para fazer mais.
- **Legibilidade:** Códigos mais claros e fáceis de manter.
- **Performance:** Otimizações que economizam tempo e recursos computacionais, especialmente ao utilizar compreensões, funções embutidas e técnicas como caching e paralelismo.

Esses truques avançados tornam o código Python mais eficiente, ajudando você a escrever programas que rodam mais rápido e são mais fáceis de manter.

## Conclusão

As técnicas abordadas ajudam a otimizar e limpar o código. Praticar essas abordagens avançadas permitirá que os desenvolvedores escrevam código mais eficiente e profissional. A prática constante é a chave para dominar esses truques e utilizá-los da maneira certa no dia a dia.
