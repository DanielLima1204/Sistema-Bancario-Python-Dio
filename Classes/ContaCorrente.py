from Classes.Conta import Conta

class ContaCorrente(Conta):
  def __init__(self, limite_saques, saques_realizados, limite_de_saldo, **kw):
    super().__init__(**kw)
    self._limite = limite_de_saldo
    self.saques_realizados = saques_realizados
    self.limite_saques = limite_saques
  
  @classmethod
  def nova_conta(cls, limite_saques=5, saques_realizados=0, limite_de_saldo=15000.00, **kw):
    return cls(limite_saques, saques_realizados, limite_de_saldo, **kw)
  
  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      return True
    else:
      return False
    
  def sacar(self, valor):
    if valor > 0:
      self._saldo -= valor
      self.saques_realizados += 1
      return True
    else:
      return False
