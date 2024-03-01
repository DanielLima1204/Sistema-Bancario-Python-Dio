from funcoes_uteis.buscando_usuario import buscando_usuario
from funcoes_uteis.check_conta_corrente import usuario_tem_conta_corrente
from Classes.ContaCorrente import ContaCorrente

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
    