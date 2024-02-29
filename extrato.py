from funcoes_uteis.buscando_conta import buscando_conta
from funcoes_uteis.buscando_usuario import buscando_usuario


text = '''
  #########################################################################################################################
                                    DEMONSTRATIVO DE TRANSAÇÕES
  #########################################################################################################################                  
  '''
def extrato(lista_usuarios):
  print(" ################## Voçe está na opção de Extrato. #####################")
  
  usuario_para_extrato = buscando_usuario(lista_usuarios)
  if usuario_para_extrato == None:
    print("Usuário não encontrado!")
    return False
  
  conta_para_extrato = buscando_conta(usuario_para_extrato)
  if conta_para_extrato == None:
    print("Esta conta não existe!")
    return False
  
  todas_transacoes = conta_para_extrato.historico.transacoes_realizadas
  
  if(len(todas_transacoes) == 0):
    print(text)
    print("--------------------   NENHUMA MOVIMENTAÇÃO REALIZADA ------------------------")
  else: 
    print(text)
    for transacao in todas_transacoes:
      for key, value in transacao.items():
        print(f"{key} ---- {value}")
      print("##########################")
  return  