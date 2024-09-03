# Aula: Recursão em Python

## Objetivo da Aula

Entender o conceito de recursão, como ela funciona em Python e quando utilizá-la para resolver problemas de forma elegante e eficiente.

---

## 1. O que é Recursão?

Recursão é uma técnica em programação onde uma função chama a si mesma. É usada para resolver problemas que podem ser divididos em subproblemas menores e similares ao problema original.

### Definição:

- **Caso Base:** O caso mais simples, onde a função retorna um valor sem chamar a si mesma. Evita que a recursão continue indefinidamente.
- **Caso Recursivo:** O caso em que a função chama a si mesma para resolver um subproblema.

### Exemplo Simples:

```python
def countdown(n):
    if n == 0:  # Caso Base
        print("Fogo!")
    else:  # Caso Recursivo
        print(n)
        countdown(n - 1)

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Fogo!
```

Aqui, a função `countdown()` chama a si mesma com `n-1` até que `n` seja igual a zero (o caso base), quando ela para de chamar a si mesma.

---

## 2. Como a Recursão Funciona?

A recursão resolve problemas dividindo-os em partes menores, e cada parte é tratada separadamente. O Python usa uma estrutura de pilha (stack) para gerenciar as chamadas recursivas.

Cada vez que uma função recursiva é chamada, uma nova instância dessa função é colocada na pilha até que o caso base seja atingido. Quando o caso base é alcançado, o Python começa a desempilhar as chamadas e a resolver os subproblemas.

---

## 3. Exemplo Clássico: Fatorial

O fatorial de um número é o produto de todos os inteiros positivos até aquele número. Ele pode ser calculado recursivamente.

### Fórmula Matemática:
```
n! = n * (n - 1) * (n - 2) * ... * 1
```

### Implementação Recursiva:

```python
def factorial(n):
    if n == 0 or n == 1:  # Caso Base
        return 1
    else:  # Caso Recursivo
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Análise:

1. O caso base é quando `n` é 0 ou 1, onde o fatorial é 1.
2. Para `n > 1`, a função chama a si mesma com `n-1` até atingir o caso base.

### Visualizando as Chamadas Recursivas:

Para `factorial(5)`:
- `factorial(5) = 5 * factorial(4)`
- `factorial(4) = 4 * factorial(3)`
- `factorial(3) = 3 * factorial(2)`
- `factorial(2) = 2 * factorial(1)`
- `factorial(1) = 1`

O cálculo então se resolve de volta para cima, multiplicando todos os valores.

---

## 4. Exemplo Clássico: Sequência de Fibonacci

A sequência de Fibonacci é outra aplicação clássica de recursão. Cada número da sequência é a soma dos dois números anteriores.

### Fórmula Matemática:
```
F(n) = F(n-1) + F(n-2)
F(0) = 0, F(1) = 1
```

### Implementação Recursiva:

```python
def fibonacci(n):
    if n == 0:  # Caso Base 1
        return 0
    elif n == 1:  # Caso Base 2
        return 1
    else:  # Caso Recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
```

### Análise:

- Caso base: `fibonacci(0)` retorna 0, e `fibonacci(1)` retorna 1.
- Para `n > 1`, a função chama a si mesma com `n-1` e `n-2`.

### Problema de Performance:

Embora a recursão seja uma solução simples para Fibonacci, ela é ineficiente para números grandes devido à repetição de cálculos. Para resolver esse problema, técnicas como **memoização** podem ser aplicadas (discutido abaixo).

---

## 5. Vantagens e Desvantagens da Recursão

### Vantagens:

- **Elegância e Clareza:** Recursão pode tornar o código mais intuitivo, especialmente ao lidar com problemas que têm uma estrutura recursiva natural, como árvores e grafos.
- **Simplicidade:** Algumas soluções são mais fáceis de implementar recursivamente, especialmente para algoritmos que envolvem divisão e conquista.

### Desvantagens:

- **Limite de Recursão:** Python tem um limite de profundidade de recursão padrão (geralmente 1000). Se sua função recursiva ultrapassar esse limite, você encontrará um erro de `RecursionError`.
- **Performance:** Recursão geralmente usa mais memória, já que cada chamada é armazenada na pilha de execução. Isso pode levar a problemas de desempenho para problemas de grandes dimensões.
  
---

## 6. Técnicas para Melhorar a Recursão

### 6.1. Memoização (Caching)

Memoização é uma técnica para otimizar recursão armazenando os resultados de chamadas anteriores. Isso evita que a função recursiva faça o mesmo cálculo repetidamente.

#### Exemplo Usando `functools.lru_cache`:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # Muito mais rápido que sem cache
```

### 6.2. Recursão de Cauda

Recursão de cauda é um caso especial de recursão onde a chamada recursiva é a última operação que a função executa. Alguns compiladores podem otimizar esse tipo de recursão, mas o Python não faz essa otimização de forma nativa.

#### Exemplo de Recursão de Cauda:

```python
def tail_recursive_factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_recursive_factorial(n - 1, n * acc)

print(tail_recursive_factorial(5))  # Output: 120
```

Nesse caso, o cálculo intermediário é passado como argumento (acc), evitando a necessidade de acumular chamadas recursivas na pilha.

---

## 7. Recursão em Estruturas de Dados

### 7.1. Exemplo com Árvores

Recursão é extremamente útil ao lidar com estruturas de dados como árvores. Um exemplo clássico é percorrer uma árvore binária.

#### Exemplo:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)

# Criando uma árvore binária
root = Node(10)
root.left = Node(5)
root.right = Node(15)

in_order_traversal(root)
# Output:
# 5
# 10
# 15
```

Aqui, a função `in_order_traversal()` é recursiva e visita os nós da árvore binária em ordem.

---

## 8. Quando Usar Recursão?

- **Divisão e Conquista:** Algoritmos como Merge Sort e Quick Sort utilizam recursão para dividir o problema em partes menores.
- **Estruturas Recursivas:** Como árvores, grafos e problemas baseados em backtracking (ex: labirintos, Sudoku).
- **Problemas Naturais para Recursão:** Fatorial, Fibonacci, permutações, e combinações.

---

## 9. Exercícios Práticos

### Exercício 1: Fatorial Recursivo

Implemente uma função recursiva que calcule o fatorial de um número `n`.

### Exercício 2: Fibonacci Recursivo

Implemente uma função recursiva que calcule o n-ésimo número da sequência de Fibonacci.

### Exercício 3: Soma de Lista Recursiva

Escreva uma função recursiva que some todos os números em uma lista.

---

## 10. Conclusão

Recursão é uma poderosa ferramenta em Python, mas precisa ser usada com cautela. Ela é ideal para resolver problemas que podem ser divididos em subproblemas menores. No entanto, é importante entender as limitações, como o limite de recursão e o consumo de memória, e saber quando optar por soluções iterativas mais eficientes.
