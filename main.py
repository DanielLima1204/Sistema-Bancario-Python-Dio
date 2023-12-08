from deposito import deposito
from saque import saque
from extrato import extrato
from criar_usuario import criar_usuario

extrato_info_list = []

usuarios_list = []

saldo = 0

saques_realizados = 0

menu = f'''
###################################################################################################################################
                                       BEM - VINDO AO DANIELS BANK
###################################################################################################################################

Digite uma das opções desejada:
[ 1 ] = Déposito 
[ 2 ] = Saque
[ 3 ] = Extrato
[ 4 ] = Cadastrar Usuário
[ 5 ] = Sair                                       
'''

while True:
  print(menu)
  opcao = int(input('Digite a opção: '))
  
  if(opcao == 1):
    saldo, infor_para_extrato = deposito(saldo)
    extrato_info_list.append(infor_para_extrato)
  
  elif(opcao == 2):
    saldo, saques_realizados, infor_para_extrato = saque(saldo=saldo, saques_realizados=saques_realizados)
    extrato_info_list.append(infor_para_extrato)
  
  elif(opcao == 3):
    ## Como minha implementação está diferente da proposta, deixarei o unico argumento passado como keyword.
    extrato(dados=extrato_info_list)
  elif(opcao == 4):
    new_user = criar_usuario(usuarios_list)
    usuarios_list.append(new_user)
  elif(opcao == 5):
    print("Obrigado por usar nosso banco, volte sempre!")
    break
  else:
    print("Opção Inválida. Tente novamente!")
  
    
  