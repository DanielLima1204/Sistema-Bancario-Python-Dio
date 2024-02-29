from funcoes_uteis.buscando_conta import buscando_conta
from funcoes_uteis.buscando_usuario import buscando_usuario
from transacoes.transacao_saque import Saque


def saque(lista_usuarios):
  print(" ################## Voçe está na opção de saque. #####################")
  
  usuario_para_saque = buscando_usuario(lista_usuarios)
  if usuario_para_saque == None:
    print("Usuário não encontrado!")
    return False
  
  conta_para_saque = buscando_conta(usuario_para_saque)
  if conta_para_saque == None:
    print("Esta conta não existe!")
    return False
  
  valor_do_saque = float(input("Digite o valor para saque: "))
  saque = Saque(valor_do_saque)
  
  if usuario_para_saque.realizar_transacao(conta_para_saque, saque) == True:
    print(f"Saque Realizado com sucesso. Seu saldo é: {conta_para_saque.saldo:.2f} R$")
    conta_para_saque.historico.adicionar_transacao(saque)
    return True
  else:
    return False