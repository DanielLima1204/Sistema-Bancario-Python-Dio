from deposito import deposito
from saque import saque


extrato = []

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
    saldo = deposito(saldo=saldo)
  
  elif(opcao == 2):
    saldo, saques_realizados = saque(saldo=saldo, saques_realizados=saques_realizados)  
  
  if(opcao == 4):
    print("Obrigado por usar nosso banco, volte sempre!")
    break
  print(saldo)   
  