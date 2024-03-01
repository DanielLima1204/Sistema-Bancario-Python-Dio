class Cliente:
  def __init__(self, endereco):
    self._endereco = endereco
    self._contas = []
  
  @property
  def contas_do_user(self):
    return self._contas
  
  def realizar_transacao(self, conta, transacao):
    pass
      
  def adicionar_conta(self, conta):
    pass
