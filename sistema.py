from deposito import deposito
from saque import saque
from extrato import extrato

extrato_info_list = []

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
[ 4 ] = Sair                                       
'''

while True:
  print(menu)
  opcao = int(input('Digite a opção: '))
  
  if(opcao == 1):
    saldo, infor_para_extrato = deposito(saldo=saldo)
    extrato_info_list.append(infor_para_extrato)
  
  elif(opcao == 2):
    saldo, saques_realizados, infor_para_extrato = saque(saldo=saldo, saques_realizados=saques_realizados)
    extrato_info_list.append(infor_para_extrato)
  
  elif(opcao == 3):
    extrato(dados=extrato_info_list)
  
  elif(opcao == 4):
    print("Obrigado por usar nosso banco, volte sempre!")
    break
  else:
    print("Opção Inválida. Tente novamente!")
  
    
  