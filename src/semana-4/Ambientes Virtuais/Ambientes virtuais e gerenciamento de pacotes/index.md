# Aula: Organização de Projetos Python e Ambientes Virtuais

## Organização de um Projeto Python

## O que é o pip?

`pip` é o gerenciador de pacotes oficial do Python. Ele permite instalar, atualizar, e remover pacotes de bibliotecas Python, que podem ser usadas em seus projetos. O `pip` simplifica o processo de gestão de dependências, permitindo que você use pacotes de terceiros facilmente.

- **pip** significa "Pip Installs Packages".
- Ele instala pacotes da [Python Package Index (PyPI)](https://pypi.org/).

## Instalação do pip

A maioria das distribuições modernas do Python já vem com o `pip` pré-instalado. Para verificar se o `pip` está instalado na sua máquina, execute o seguinte comando:

```bash
pip --version
```

Se não estiver instalado, você pode instalá-lo usando o script oficial do Python:

```bash
python -m ensurepip --upgrade
```

## Principais Comandos do pip

### Instalar um Pacote

Para instalar um pacote com o `pip`, use o comando `install` seguido do nome do pacote:

```bash
pip install nome-do-pacote
```

Exemplo:

```bash
pip install requests
```

Isso instalará a biblioteca `requests`, que facilita fazer chamadas HTTP em Python.

### Listar Pacotes Instalados

Para ver todos os pacotes instalados no seu ambiente, use:

```bash
pip list
```

Isso mostrará uma lista de todas as bibliotecas instaladas e suas versões.

### Atualizar um Pacote

Para atualizar um pacote específico para a versão mais recente, use o comando `install --upgrade`:

```bash
pip install --upgrade nome-do-pacote
```

Exemplo:

```bash
pip install --upgrade requests
```

### Desinstalar um Pacote

Para remover um pacote, use o comando `uninstall`:

```bash
pip uninstall nome-do-pacote
```

Exemplo:

```bash
pip uninstall requests
```

### Instalar Pacotes Usando `requirements.txt`

O `requirements.txt` é um arquivo de texto que lista todos os pacotes que seu projeto precisa, incluindo as versões específicas. Para instalar todos os pacotes de um arquivo `requirements.txt`, use o comando:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` pode ter o seguinte formato:

```
requests==2.26.0
Flask==2.0.1
```

Cada linha define o nome do pacote e sua versão. Esse arquivo facilita a instalação das dependências do projeto em diferentes máquinas ou ambientes.

### Congelar Dependências com `freeze`

Se você quiser gerar automaticamente um arquivo `requirements.txt` com todas as bibliotecas e versões instaladas no seu ambiente, use o comando `freeze`:

```bash
pip freeze > requirements.txt
```

Isso captura o estado atual do ambiente, tornando fácil compartilhar as dependências com outros desenvolvedores.

### Instalar Pacotes de Fontes Alternativas

Além do PyPI, você também pode instalar pacotes diretamente de outras fontes, como repositórios Git, URLs, ou arquivos locais.

Exemplo de instalação a partir de um repositório Git:

```bash
pip install git+https://github.com/psf/requests.git
```

---

## Ambientes Virtuais

### Por que Usar Ambientes Virtuais?

Ambientes virtuais isolam dependências, evitando conflitos entre pacotes de diferentes projetos. Cada projeto pode ter suas próprias versões de bibliotecas, sem afetar outros projetos ou o Python global do sistema.

### Criando Ambientes Virtuais com `venv`

## O que é `venv`?

`venv` é um módulo embutido no Python (a partir da versão 3.3) que permite a criação de **ambientes virtuais**. Um ambiente virtual é uma estrutura de diretórios isolada, onde você pode instalar pacotes específicos do seu projeto sem afetar os pacotes instalados globalmente no sistema. 

Isso é útil para evitar conflitos entre diferentes projetos que podem precisar de diferentes versões das mesmas bibliotecas.

### Por que usar `venv`?

1. **Isolamento de Dependências**: Cada projeto pode ter suas próprias bibliotecas e versões sem interferir em outros projetos ou no sistema global.
2. **Reprodutibilidade**: Facilita a criação de ambientes replicáveis para outros desenvolvedores ou para quando o projeto precisa ser executado em diferentes máquinas.
3. **Facilidade de Gerenciamento**: Ajuda a organizar as dependências e facilita a remoção e atualização de pacotes sem afetar o ambiente global do Python.

---

#### Em Windows

1. Crie o ambiente virtual:
   ```bash
   python -m venv nome_do_ambiente
   ```

2. Ative o ambiente virtual:
   ```bash
   nome_do_ambiente\Scripts\activate
   ```

3. Desative o ambiente:
   ```bash
   deactivate
   ```

#### Em macOS/Linux

1. Crie o ambiente virtual:
   ```bash
   python3 -m venv nome_do_ambiente
   ```

2. Ative o ambiente virtual:
   ```bash
   source nome_do_ambiente/bin/activate
   ```

3. Desative o ambiente:
   ```bash
   deactivate
   ```

---