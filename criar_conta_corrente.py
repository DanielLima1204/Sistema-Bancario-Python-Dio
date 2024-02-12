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
  def __init__(self, limite, limite_saques, **kw):
    super().__init__(**kw)
    self._limite = limite
    self._limite_saques = limite_saques  

def criar_conta_corrente(user_list, contas_correntes):
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
    cpf_ja_existe = testando_cpf_ja_existe(cpf, user_list)
    if cpf_ja_existe == False:
      print("Este CPF não existe em nosso Cadastro de Usuários, Realize seu cadastro!")
      return
    
    #Obtendo nome da lista de usuario
    nome = None
    for user in user_list:
      if user['CPF'] == cpf:
        nome = user['Nome']
  
    infor_nova_conta = {
      'Agencia': '0001',
      'Número': '{}'.format(len(contas_correntes) + 1),
      'Nome': f'{nome}'
    }
    
    return infor_nova_conta
  
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
    