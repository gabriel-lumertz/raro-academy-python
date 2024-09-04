from contas.conta import Conta
from pix.pix import Pix
from datetime import datetime

class PixSimples(Pix):
    
    def __init__(self, valor: float, conta_origem: Conta, conta_destino: Conta) -> None:
        super().__init__(valor, conta_origem, conta_destino)
        self.data_transacao = datetime.now()

    """Executa uma transferência PIX Simples."""

    def executar(self) -> None:
        
        if self.conta_origem.saldo < self.valor:
            print('Pix não realizado. Saldo insuficiente.')
        else:
            self.conta_origem.realizar_pix(self.valor)
            self.conta_destino.saldo += self.valor
            print(f'Pix de {self.valor} realizado com sucesso.')
            print(f'Saldo atual da conta origem: {self.conta_origem.saldo}')
            print(f'Saldo atual da conta destino: {self.conta_destino.saldo}')
