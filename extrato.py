text = '''
  #########################################################################################################################
                                    DEMONSTRATIVO DE TRANSAÇÕES
  #########################################################################################################################                  
  '''
def extrato(dados):
  print(text)
  for dado in dados:
    for key, value in dado.items():
      print(f"{key} ---- {value}")
    print("##########################")
  return  