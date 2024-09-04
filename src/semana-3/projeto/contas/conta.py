from enums.tipo_conta import TipoConta

class Conta:
    
    def __init__(self, titular: str, saldo: float, numero: str, tipo_conta: TipoConta) -> None:
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
        self.tipo_conta = tipo_conta

    """Método abstrato para realizar uma transferência PIX."""
    
    def realizar_pix(self, valor: float) -> None:
        
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")
