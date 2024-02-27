def buscando_conta(cliente):
  numero_da_conta = int(input("Digite o número da conta: "))
  contas_do_cliente = cliente.contas_do_user
  conta_para_deposito = None
  for conta in contas_do_cliente:
    if conta.numero == numero_da_conta:
      conta_para_deposito = conta
  return conta_para_deposito
        
  