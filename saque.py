def saque(saldo, saques_realizados):
  QUANTIDADE_DE_SAQUES_DIARIOS = 3
  
  print(" ################## Voçe está na opção de saque. #####################")
  if(saques_realizados >= QUANTIDADE_DE_SAQUES_DIARIOS):
    print("Infelizmente vc execedeu o limite de saques diarios!")
    infor_para_extrato = {'Tipo de Operação:': 'Saque', 'Status': 'Execedeu o número de saques, operação cancelada.'}
    return saldo, saques_realizados, infor_para_extrato
  else:
    valor_do_saque = float(input("Digite o valor para saque: "))
    
  if(saldo >= valor_do_saque <= 500.00 and valor_do_saque > 0):
    saldo_anterior = saldo
    novo_saldo = saldo - valor_do_saque
    infor_para_extrato = {'Tipo de Operação:': 'Saque', 'Valor de saque: ': f'R${valor_do_saque:.2f}', 'Saldo Anterior': f'R${saldo_anterior:.2f}', 'Saldo Atual': f'R${novo_saldo:.2f}'}
    
    print(f"Saque Realizado com sucesso. Seu saldo é: {novo_saldo:.2f} R$")
    return novo_saldo, saques_realizados + 1, infor_para_extrato
  else:
    print("Valor Inválido, Tente novamente.")
    infor_para_extrato = {'Tipo de Operação:': 'Saque', 'Status': 'Valor inválido, operação cancelada.'}
    return saldo, saques_realizados, infor_para_extrato 
