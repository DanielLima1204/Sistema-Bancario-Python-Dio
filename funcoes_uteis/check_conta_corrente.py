def usuario_tem_conta_corrente(usuario):
  contas = usuario.contas_do_user
  for conta in contas:
    if type(conta).__name__ == 'ContaCorrente':
      return True
  return  