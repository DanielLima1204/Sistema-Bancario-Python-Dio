QUANTIDADE_DE_SAQUES_DIARIOS = 3

extrato = {}

saldo = 1500


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
  if(opcao == 4):
    print("Obrigado por usar nosso banco, volte sempre!")
    break   
  