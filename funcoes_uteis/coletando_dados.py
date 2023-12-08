from funcoes_uteis.testes_cpf import testando_cpf_ja_existe, verificando_formato_cpf
     
def coletando_info_usuario(user_list):
  user_name = str(input('Digite seu nome (apenas letras): '))
  user_date_of_birth = str(input('Data de Nascimento (ex: DD/MM/AA): '))
  user_cpf = str(input('CPF (Apenas números): '))
  if verificando_formato_cpf(cpf_digitado=user_cpf) == False:
    return {'Erro': 'CPF digitado com formato inválido, Tente com outro CPF.'}
  elif testando_cpf_ja_existe(cpf_digitado=user_cpf, users_list=user_list):
    return {'Erro': 'CPF digitado já existe, Tente com outro CPF.'}
  else:
    user_location = str(input('Rua/Avenida: '))
    user_number = str(input('Número: '))
    user_district = str(input('Bairro: '))
    user_city = str(input('Cidade: '))
    user_state = str(input('Estado (Sigla ex: SE, RJ): '))
    
    user_full_adress = f'{user_location}, {user_number} - {user_district} - {user_city}/{user_state}'
    return {'Nome': user_name, 'Data de Nascimento': user_date_of_birth, 'CPF': user_cpf, 'Endereço': user_full_adress}