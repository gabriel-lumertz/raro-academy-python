## Versionamento de Python com Pyenv

### O que é o Pyenv?

O `pyenv` permite que você gerencie várias versões do Python em um único sistema, alternando facilmente entre elas. Isso é útil para testar código em diferentes versões ou lidar com projetos legados.

### Instalando o Pyenv

#### Em macOS/Linux

1. Instale o `pyenv` via `curl`:
   ```bash
   curl https://pyenv.run | bash
   ```

2. Adicione o seguinte ao arquivo de configuração do shell (`~/.bashrc`, `~/.zshrc` etc.):
   ```bash
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   ```

3. Recarregue o shell:
   ```bash
   exec "$SHELL"
   ```

#### Em Windows

No Windows, você pode usar o `pyenv-win`, que é uma versão adaptada do `pyenv`.

1. Instale o `pyenv-win` seguindo as instruções do repositório oficial: [pyenv-win](https://github.com/pyenv-win/pyenv-win).

### Usando o Pyenv

#### Instalando uma Versão do Python

Você pode instalar uma versão específica do Python com o comando:

```bash
pyenv install 3.10.4
```

#### Definindo a Versão Global

```bash
pyenv global 3.10.4
```

Essa versão será utilizada em todos os diretórios.

#### Definindo a Versão Local (Projeto)

```bash
pyenv local 3.9.7
```

Isso cria um arquivo `.python-version` no diretório atual.

#### Listando Versões Instaladas

```bash
pyenv versions
```

#### Removendo uma Versão

```bash
pyenv uninstall 3.x.x
```