from contas.conta import Conta
from enums.tipo_conta import TipoConta

class ContaPoupanca(Conta):
    
    def __init__(self, titular: str, saldo: float, numero: str) -> None:
        super().__init__(titular, saldo, numero, TipoConta.Poupanca)  # Define o tipo da conta como Poupança.

    """Realiza um PIX com restrições de limite diário."""
    
    def realizar_pix(self, valor: float) -> None:
        
        limite_diario = 1000.0

        if valor > limite_diario:
            print(f'Pix não realizado. Limite diário de {limite_diario} excedido.')
        elif self.saldo < valor:
            print('Pix não realizado. Saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'Pix realizado. Seu saldo é {self.saldo}.')
