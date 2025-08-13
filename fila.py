# Filas

from dataclasses import dataclass
from datetime import datetime, timedelta


sair = 0
entrada = datetime.now()
agora = datetime.now()
doisSeg = timedelta(seconds=2)
dezSeg = timedelta(seconds=10)

clientes = [

]

while sair != 1:
    def entradaFila(clientes):
        if datetime.now() >= agora + doisSeg:
            fila_clientes = []
            for cliente in clientes:
                fila_clientes.append(cliente)
        return fila_clientes
            
    def atendimento(fila_clientes):
        if datetime.now() >= agora + dezSeg:
            clientes_atendimento = []
            for cliente in fila_clientes:
                clientes_atendimento.append(cliente)
            return clientes_atendimento
    
    def saidaAtendimento(clientes_atendimento):
        if datetime.now() >= agora + dezSeg:
            atendido = clientes_atendimento.pop(0)
            print('Cliente atendido: ', atendido)

entradaFila()
atendimento()
saidaAtendimento()
sair = 0
