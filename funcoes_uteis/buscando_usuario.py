def buscando_usuario(lista_usuarios):
  cpf_do_titular = input("Digite o cpf do titular da conta: ")
  user_para_deposito = None
  for user in lista_usuarios:
    if user.cpf == cpf_do_titular:
      user_para_deposito = user
  return user_para_deposito
      