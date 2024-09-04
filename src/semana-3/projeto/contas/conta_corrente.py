from typing import Optional
from contas.conta import Conta
from enums.tipo_conta import TipoConta

class ContaCorrente(Conta):
    
    def __init__(self, titular: str, saldo: float, numero: str) -> None:
        super().__init__(titular, saldo, numero, TipoConta.Corrente)  # Define o tipo da conta como Corrente.

    """Realiza um PIX com taxa de 5% para Conta Corrente."""
    
    def realizar_pix(self, valor: float, mensagem: Optional[str] = None) -> None:
        
        taxa = 0.05
        valor_com_taxa = valor * (1 + taxa)

        if self.saldo < valor_com_taxa:
            print('Pix não realizado. Saldo insuficiente após aplicar taxa.')
        else:
            self.saldo -= valor_com_taxa
            print(f'Pix realizado com taxa de {taxa * 100}%. Seu saldo é {self.saldo}.')
            
            if mensagem:
                print(f'Mensagem de confirmação: {mensagem}')
