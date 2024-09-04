'''
Implemente um sistema de simulação de transações Pix utilizando os conceitos de orientação
a objetos em Python. O sistema deve incluir classes para representar contas bancárias e
transações Pix. O objetivo é modelar diferentes tipos de contas (Conta Corrente e Conta
Poupança) e diferentes tipos de transações (Pix Simples e Pix Agendado). 
'''

# Requisitos:

# 1 Herança: Crie uma classe base Conta que possui atributos e métodos comuns a todas as contas. A partir dessa classe, derive duas classes: ContaCorrente e ContaPoupanca. 

# 2 polimorfismo:  Ambas as classes ContaCorrente e ContaPoupanca devem implementar um método realizar_pix(), mas com comportamentos diferentes dependendo do tipo de conta.

# 3 Override/Substituição: Implemente um método na classe ContaCorrente que sobrescreva o método da classe base Conta, para aplicar uma taxa adicional ao realizar o Pix.

# 4 Utilize a classe Enum do módulo enum para representar os diferentes tipos de conta (por exemplo, CONTA_CORRENTE e CONTA_POUPANCA), e associe essa enumeração ao comportamento das classes.

# 5 Abstração: Implemente uma classe Pix que possa ser instanciada tanto para uma transferência imediata quanto para uma transferência agendada. Utilize herança para criar as subclasses PixSimples e PixAgendado.

'''
Especificações Técnicas:
- A classe Conta deve ter os atributos titular, saldo, numero e tipo_conta.
- O método realizar_pix() deve ser implementado nas classes ContaCorrente e ContaPoupanca.
- Ao realizar o Pix, deve-se verificar se há saldo suficiente na conta. Caso contrário, exiba uma mensagem de erro.
- Para o método sobrecarregado realizar_pix() na classe ContaCorrente, implemente duas versões: uma que aceita apenas o valor do Pix e outra que aceita o valor e uma mensagem de confirmação. 
'''

from datetime import datetime
from enum import Enum
from typing import Optional

# Enum para definir o tipo de conta
class TipoConta(Enum):
    Poupanca = 1
    Corrente = 2

# Classe base para o sistema de conta
class Conta:
    def __init__(self, titular: str, saldo: float, numero: str, tipo_conta: TipoConta) -> None:
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
        self.tipo_conta = tipo_conta

    def realizar_pix(self, valor: float) -> None:
        """Método abstrato para realizar uma transferência PIX."""
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

# Subclasse ContaPoupanca
class ContaPoupanca(Conta):
    
    def __init__(self, titular: str, saldo: float, numero: str) -> None:
        super().__init__(titular, saldo, numero, TipoConta.Poupanca)  # Define o tipo como Poupança

    def realizar_pix(self, valor: float) -> None:
        """Realiza um PIX com restrições de limite diário."""
        limite_diario = 1000.0

        if valor > limite_diario:
            print(f'Pix não realizado. Limite diário de {limite_diario} excedido.')
        elif self.saldo < valor:
            print('Pix não realizado. Saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'Pix realizado. Seu saldo é {self.saldo}.')

# Subclasse ContaCorrente
class ContaCorrente(Conta):
    
    def __init__(self, titular: str, saldo: float, numero: str) -> None:
        super().__init__(titular, saldo, numero, TipoConta.Corrente)  # Define o tipo como Corrente

    def realizar_pix(self, valor: float, mensagem: Optional[str] = None) -> None:
        """Realiza um PIX com taxa de 5% para Conta Corrente."""
        taxa = 0.05  # 5% de taxa para transferências via PIX
        valor_com_taxa = valor * (1 + taxa)

        if self.saldo < valor_com_taxa:
            print('Pix não realizado. Saldo insuficiente após aplicar taxa.')
        else:
            self.saldo -= valor_com_taxa
            print(f'Pix realizado com taxa de {taxa * 100}%. Seu saldo é {self.saldo}.')
            
            if mensagem:
                print(f'Mensagem de confirmação: {mensagem}')

# Implementação da classe Pix
class Pix:
    def __init__(self, valor: float, conta_origem: Conta, conta_destino: Conta) -> None:
        self.valor = valor
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.data_transacao = None

    def executar(self) -> None:
        """Método abstrato para executar a transação PIX."""
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

# Subclasse PixSimples para transferências imediatas
class PixSimples(Pix):
    def __init__(self, valor: float, conta_origem: Conta, conta_destino: Conta) -> None:
        super().__init__(valor, conta_origem, conta_destino)
        self.data_transacao = datetime.now()

    def executar(self) -> None:
        """Executa uma transferência PIX imediata."""
        if self.conta_origem.saldo < self.valor:
            print('Pix não realizado. Saldo insuficiente.')
        else:
            self.conta_origem.realizar_pix(self.valor)
            self.conta_destino.saldo += self.valor
            print(f'Pix de {self.valor} realizado com sucesso.')
            print(f'Saldo atual da conta origem: {self.conta_origem.saldo}')
            print(f'Saldo atual da conta destino: {self.conta_destino.saldo}')

# Subclasse PixAgendado para transferências agendadas
class PixAgendado(Pix):
    def __init__(self, valor: float, conta_origem: Conta, conta_destino: Conta, data_agendamento: datetime) -> None:
        super().__init__(valor, conta_origem, conta_destino)
        self.data_agendamento = data_agendamento

    def executar(self) -> None:
        """Executa uma transferência PIX agendada."""
        if datetime.now() >= self.data_agendamento:
            if self.conta_origem.saldo < self.valor:
                print('Pix não realizado. Saldo insuficiente.')
            else:
                self.conta_origem.realizar_pix(self.valor)
                self.conta_destino.saldo += self.valor
                print(f'Pix de {self.valor} realizado com sucesso.')
                print(f'Saldo atual da conta origem: {self.conta_origem.saldo}')
                print(f'Saldo atual da conta destino: {self.conta_destino.saldo}')
        else:
            print(f'A transação está agendada para {self.data_agendamento}. Ainda não foi realizada.')

# Exemplos de uso:

# Criando contas
conta_origem = ContaCorrente("Alice", 5000.0, "12345")
conta_destino = ContaPoupanca("Bob", 1000.0, "67890")

# Transferência imediata
pix_simples = PixSimples(200.0, conta_origem, conta_destino)
pix_simples.executar()

# Transferência agendada
data_agendamento = datetime(2024, 9, 10, 14, 30)
pix_agendado = PixAgendado(300.0, conta_origem, conta_destino, data_agendamento)
pix_agendado.executar()

# Usando os diferentes métodos de realizar_pix em ContaCorrente
conta_origem.realizar_pix(100.0)
conta_origem.realizar_pix(50.0, "Pagamento de serviço")  # Com mensagem de confirmação
