def deposito(saldo): 
  print(" ################## Voçe está na opção de déposito. #####################")
  valor_do_deposito = float(input("Digite o valor para déposito: "))
  if(valor_do_deposito > 0):
    novo_saldo = saldo + valor_do_deposito
    print(f"Déposito Realizado com sucesso. Seu saldo é: {novo_saldo} R$")
    return novo_saldo
  else:
    print("Valor Inválido, Tente novamente.")
    novo_saldo = 0
    return novo_saldo
