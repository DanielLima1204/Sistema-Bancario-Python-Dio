from Classes.Cliente import Cliente

class PessoaFisica(Cliente):
  def __init__(self,  cpf, nome, data_de_nascimento, **kw):
    super().__init__(**kw)
    self._cpf = cpf
    self._nome = nome
    self._data_de_nascimento = data_de_nascimento
  
  @property
  def cpf(self):
    return self._cpf
  
  def realizar_transacao(self, conta, transacao):
    return transacao.registrar(conta)
  
  def adicionar_conta(self, conta):
  #TODO checar se já existe uma conta corrente com este cpf
    self._contas.append(conta)
     
  def __str__(self):
    return f"Nome: {self._nome}\tCPF: {self._cpf}\tData de Nascimento: {self._data_de_nascimento}\tContas: {self._contas}"
  