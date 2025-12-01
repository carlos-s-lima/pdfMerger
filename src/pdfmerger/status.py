from enum import Enum

class Status(Enum):
    AGUARDANDO = 'Aguardando'
    PROCESSANDO = 'Processando'
    SUCESSO = 'Sucesso'
    ERRO = 'Erro'
