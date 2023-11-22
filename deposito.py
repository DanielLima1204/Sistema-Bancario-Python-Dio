def deposito(saldo): 
  print(" ################## Voçe está na opção de déposito. #####################")
  valor_do_deposito = float(input("Digite o valor para déposito: "))
  if(valor_do_deposito > 0):
    saldo_anterior = saldo
    novo_saldo = saldo + valor_do_deposito
    infor_para_extrato = {'Tipo de Operação': 'Deposito', 'Valor do deposito: ': f'R${valor_do_deposito:.2f}', 'Saldo Anterior': f'R${saldo_anterior:.2f}', 'Saldo Atual': f'R${novo_saldo:.2f}'}
    print(f"Déposito Realizado com sucesso. Seu saldo é: {novo_saldo:.2f} R$")
    return novo_saldo, infor_para_extrato
  else:
    print("Valor Inválido, Tente novamente.")
    infor_para_extrato = {'Tipo de Operação': 'Deposito', 'Erro': 'Valor Inválido, Operação cancelada'} 
    return saldo, infor_para_extrato 
