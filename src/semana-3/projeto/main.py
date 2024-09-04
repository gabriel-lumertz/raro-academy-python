from datetime import datetime
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from pix.pix_simples import PixSimples
from pix.pix_agendado import PixAgendado

# Criando contas
conta_origem = ContaCorrente("João", 5000.0, "12345")
conta_destino = ContaPoupanca("Maria", 1000.0, "67890")

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
