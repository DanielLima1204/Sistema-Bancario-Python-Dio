from transacoes.Transacao import Transacao

class Deposito(Transacao):
  def __init__(self, valor):
    self.valor = valor
  def registrar(self, conta):
    return conta.depositar(self.valor)
    