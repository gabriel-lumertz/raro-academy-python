from contas.conta import Conta

class Pix:
    
    def __init__(self, valor: float, conta_origem: Conta, conta_destino: Conta) -> None:
        self.valor = valor
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.data_transacao = None

    """Método abstrato para executar a transação PIX."""
    
    def executar(self) -> None:
        
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")
