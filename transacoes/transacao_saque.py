from transacoes.Transacao import Transacao

class Saque(Transacao):
  def __init__(self, valor):
    self.valor = valor 
  def registrar(self, conta):
    return conta.sacar(self.valor)
    #TODO Checar o saldo da conta e realizar a operação e retornar um true no caso de sucesso