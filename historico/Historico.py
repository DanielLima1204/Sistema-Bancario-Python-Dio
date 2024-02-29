import datetime

class Historico():
  def __init__(self):
    self.transacoes_realizadas = []
    
  def adicionar_transacao(self, transacao):
    data_atual = datetime.datetime.now()
    
    data_da_transacao = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
    hora_da_transacao = f'{data_atual.hour}:{data_atual.minute}:{data_atual.second}'
    tipo_da_transacao = type(transacao)
    valor_da_transacao = transacao.valor
    
    transacao_realizada = dict()
    transacao_realizada['Transação'] = tipo_da_transacao.__name__
    transacao_realizada['Valor'] = f'{valor_da_transacao} R$'
    transacao_realizada['Data'] = data_da_transacao
    transacao_realizada['Hora'] = hora_da_transacao
    
    self.transacoes_realizadas.append(transacao_realizada)
    return  