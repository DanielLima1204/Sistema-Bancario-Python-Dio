from transacoes.Transacao import Transacao

class Saque(Transacao):
  def __init__(self, valor):
    self.valor = valor 
  def registrar(self, conta):
    if self.valor > conta.saldo:
      print("Valor para saque maior que o saldo em conta, Operação não realizada.")
      return False
    elif conta.saques_realizados >= conta.limite_saques:
      print("Limite diário de saques ultrapassado, Operação não realizada.")
      return False
    else:
      return conta.sacar(self.valor)
    #TODO Checar o saldo da conta e realizar a operação e retornar um true no caso de sucesso