from funcoes_uteis.buscando_usuario import buscando_usuario
from funcoes_uteis.buscando_conta import buscando_conta
from transacoes.transacao_deposito import Deposito
    
def deposito(lista_usuarios): 
  print(" ################## Voçe está na opção de déposito. #####################")
  
  # Encontrando user - Poderia ser feito na main
  usuario_para_deposito = buscando_usuario(lista_usuarios)
  if usuario_para_deposito == None:
    print("Usuário não encontrado!")
    return False 
  
  # Buscando a conta na instancia do User   
  conta_para_deposito = buscando_conta(usuario_para_deposito)
  if conta_para_deposito == None:
    print("Esta conta não existe!")
    return False
  
  valor_do_deposito = float(input("Digite o valor para déposito: "))
  deposito = Deposito(valor_do_deposito)
  
  if usuario_para_deposito.realizar_transacao(conta_para_deposito, deposito) == True:
    print(f"Déposito Realizado com sucesso. Seu saldo é: {conta_para_deposito.saldo:.2f} R$")
    conta_para_deposito.historico.adicionar_transacao(deposito)
    return True
  else:
    return False
 