from funcoes_uteis.menus import exibir_menu_de_confirmacao
from funcoes_uteis.coletando_dados import coletando_info_usuario      

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
  
def criar_usuario(users_list):
  text = """
#############################################################################################################################################
                                      FICAREMOS FELIZES EM TER VOÇE CONOSCO
     MAS PARA ISSO PRECISAREMOS DE ALGUMAS INFORMAÇÕES, POR ISSO RESPONDA TODAS AS PERGUNTAS ADEQUADAMENTE ;) VAMOS LÁ?
#############################################################################################################################################                                           
"""
  print(text)
  while(True):
    informacoes_usuario = coletando_info_usuario(users_list)
    
    if 'Erro' in informacoes_usuario:
      print(informacoes_usuario['Erro'])
      continue
    else:
      opcao_selected = exibir_menu_de_confirmacao(informacoes_usuario)
      if opcao_selected['Resposta'] == 'Ok':
        novo_usuario = PessoaFisica(nome=informacoes_usuario['Nome'], cpf=informacoes_usuario['CPF'], data_de_nascimento=informacoes_usuario['Data de Nascimento'], endereco=informacoes_usuario['Endereco'])
        return novo_usuario
      elif opcao_selected['Resposta'] == 'Corrigir':
        continue
      elif opcao_selected['Resposta'] == 'Retornar':
        break
    break  