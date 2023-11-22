text = '''
  #########################################################################################################################
                                    DEMONSTRATIVO DE TRANSAÇÕES
  #########################################################################################################################                  
  '''
def extrato(dados):
  if(len(dados) == 0):
    print(text)
    print("--------------------   NENHUMA MOVIMENTAÇÃO REALIZADA ------------------------")
  else: 
    print(text)
    for dado in dados:
      for key, value in dado.items():
        print(f"{key} ---- {value}")
      print("##########################")
  return  