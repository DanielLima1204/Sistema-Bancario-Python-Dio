from funcoes_uteis.buscando_usuario import buscando_usuario
from funcoes_uteis.check_conta_corrente import usuario_tem_conta_corrente
from funcoes_uteis.testes_cpf import testando_cpf_ja_existe
from historico.Historico import Historico
        
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

def criar_conta_corrente(users_list, qtd_contas_correntes):
  text = """
    ########################################################################################################################################
                                                  BEM - VINDO AO NOSSO BANCO
    ########################################################################################################################################
    SE VOÇE JÁ ESTA CADASTRADO COMO USUARIO EM NOSSO BANCO, VOÇE PODE PROSSEGUIR COM A CRIAÇÃO DA CONTA CORRENTE, CASO CONTRÁRIO CADASTRE-SE PRIMEIRO!
    [ 1 ] = Para PROSSEGUIR.
    [ 2 ] = Para SAIR.
  """
  def coletando_dados():
    usuario_conta_corrente = buscando_usuario(users_list)
    if usuario_conta_corrente == None:
      print("Este CPF não existe em nosso Cadastro de Usuários, Realize seu cadastro!")
      return
    #Testando se o usuario já tem uma conta corrente
    if usuario_tem_conta_corrente(usuario_conta_corrente):
      print("Já existe uma conta corrente vínculada a este CPF!")
      return

    nova_conta_corrente = ContaCorrente.nova_conta(
      saldo=0.0,
      numero=qtd_contas_correntes + 1,
      agencia="0001",
      cliente=usuario_conta_corrente
    )
    usuario_conta_corrente.adicionar_conta(nova_conta_corrente)
    print(usuario_conta_corrente)
    return nova_conta_corrente
  
  while(True):
    print(text)
    opcao = str(input('Digite uma das opções: '))
    if opcao == '1':
      infor_nova_conta = coletando_dados()
      return infor_nova_conta
    elif opcao == '2':
      break
    else: 
      print("Opção Inválida, Tente novamente")
    