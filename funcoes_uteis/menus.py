def exibir_menu_de_confirmacao(informacoes_usuario):
  info_confirm_text = """
  '###################### CONFIRME SUAS INFORMAÇÕES ######################'
    
    Nome: {}
    Data de Nascimento: {}
    CPF: {}
    Endereço: {}
    
    ######################################################################
    [ 1 ] = Confirmo as informações.
    [ 2 ] = Corrigir informações.
    [ 3 ] = Cancelar Cadastro e retornar ao Menu Principal.
  """.format(informacoes_usuario['Nome'], informacoes_usuario['Data de Nascimento'], informacoes_usuario['CPF'], informacoes_usuario['Endereço']) 
  
  while(True):  
    print(info_confirm_text)
    opcao = int(input('Digite uma das opções: '))
    if(opcao == 1):
      return {'Resposta': 'Ok'}  
    elif(opcao == 2):
      return {'Resposta': 'Corrigir'}
    elif(opcao == 3):
      return {'Resposta': 'Retornar'}
    else:
      print('Opção Inválida!')