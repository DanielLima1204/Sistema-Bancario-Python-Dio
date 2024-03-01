from Classes.Historico import Historico
        
class Conta():
  def __init__(self, saldo, numero, agencia, cliente):
    self._saldo = saldo
    self._numero = numero
    self._agencia = agencia
    self._cliente = cliente
    self.historico = Historico()
  
  @property
  def saldo(self):
    return self._saldo
  
  @property
  def numero(self):
    return self._numero  
  
  @classmethod
  def nova_conta(cls):
    pass
  
  def depositar(self, valor):
    pass
