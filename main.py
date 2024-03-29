from deposito import deposito
from saque import saque
from extrato import extrato
from criar_usuario import criar_usuario
from criar_conta_corrente import criar_conta_corrente

usuarios_list = []

contas_correntes = [] 

menu = f'''
###################################################################################################################################
                                       BEM - VINDO AO DANIELS BANK
###################################################################################################################################

Digite uma das opções desejada:
[ 1 ] = Déposito 
[ 2 ] = Saque
[ 3 ] = Extrato
[ 4 ] = Cadastrar Usuário
[ 5 ] = Criar Conta Corrente
[ 6 ] = Sair                                       
'''

while True:
  print(menu)
  opcao = int(input('Digite a opção: '))
  
  if(opcao == 1):
    resultado = deposito(usuarios_list)
    if resultado == True:
      print("Deposito Realizado com Sucesso.")
    else:
      print("Algo deu errado, Deposito não realizado.")  
  
  elif(opcao == 2):
    resultado = saque(usuarios_list)
    if resultado == True:
      print("Saque Realizado com sucesso!")
    else:
      print("Algo deu errado, Saque não realizado.")  
  
  elif(opcao == 3):
    extrato(lista_usuarios=usuarios_list)
  elif(opcao == 4):
    new_user = criar_usuario(usuarios_list)
    usuarios_list.append(new_user)
    print(usuarios_list)
  elif(opcao == 5):
    nova_conta_corrente = criar_conta_corrente(usuarios_list, len(contas_correntes))
    contas_correntes.append(nova_conta_corrente)
    print(len(contas_correntes)) 
  elif(opcao == 6):
    print("Obrigado por usar nosso banco, volte sempre!")
    break
  else:
    print("Opção Inválida. Tente novamente!")
  
    
  