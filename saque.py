def saque(saldo, saques_realizados):
  QUANTIDADE_DE_SAQUES_DIARIOS = 3
  
  print(" ################## Voçe está na opção de saque. #####################")
  if(saques_realizados >= QUANTIDADE_DE_SAQUES_DIARIOS):
    print("Infelizmente vc execedeu o limite de saques diarios!")
    return saldo, saques_realizados
  else:
    valor_do_saque = float(input("Digite o valor para saque: "))
    
  if(saldo >= valor_do_saque >= 500.00 and valor_do_saque > 0):
    novo_saldo = saldo - valor_do_saque
    print(f"Saque Realizado com sucesso. Seu saldo é: {novo_saldo} R$")
    return novo_saldo, saques_realizados + 1
  else:
    print("Valor Inválido, Tente novamente.")
    return saldo, saques_realizados 
