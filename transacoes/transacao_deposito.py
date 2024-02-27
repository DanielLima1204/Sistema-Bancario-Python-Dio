from transacoes.Transacao import Transacao

class Deposito(Transacao):
  def __init__(self, valor):
    self.valor = valor
  def registrar(self, conta):
    return conta.depositar(self.valor)
    #TODO Checar o valor do deposito e realizar a operação e retornar um true no caso de sucesso