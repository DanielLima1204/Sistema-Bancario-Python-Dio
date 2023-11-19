from deposito import deposito


QUANTIDADE_DE_SAQUES_DIARIOS = 3

extrato = []

saldo = 0

menu = '''
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
     
  if(opcao == 4):
    print("Obrigado por usar nosso banco, volte sempre!")
    break
  print(saldo)   
  