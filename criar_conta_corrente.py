from funcoes_uteis.testes_cpf import testando_cpf_ja_existe
from abc import ABC, abstractmethod

class Historico:
  def adicionar_transacao(self, transacao):
    pass

class Transacao(ABC):
  @abstractmethod
  def deposito(self):
    pass
  @abstractmethod
  def saque(self):
    pass
  def registrar(self, conta):
    pass

class Conta:
  def __init__(self, saldo, numero, agencia, cliente):
    self._saldo = saldo
    self._numero = numero
    self._agencia = agencia
    self._cliente = cliente
    self._historico = Historico()
  
  @property
  def saldo(self):
    return self._saldo  
  
  def nova_conta(cls):
    pass

class ContaCorrente(Conta):
  def __init__(self, limite_saques=5, limite=15000.00, **kw):
    super().__init__(**kw)
    self._limite = limite
    self._limite_saques = limite_saques  

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
    cpf = str(input("Digite seu CPF(apenas números): "))
    cpf_ja_existe = testando_cpf_ja_existe(cpf, users_list)
    if cpf_ja_existe == False:
      print("Este CPF não existe em nosso Cadastro de Usuários, Realize seu cadastro!")
      return
    
    #Obtendo nome da lista de usuario
    nome = None
    for user in users_list:
      if user.cpf == cpf:
        print(user)
        nova_conta_corrente = ContaCorrente(
          saldo=0.0,
          numero=qtd_contas_correntes + 1,
          agencia="0001",
          cliente=user
        )
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
    