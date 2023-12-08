from funcoes_uteis.menus import exibir_menu_de_confirmacao
from funcoes_uteis.coletando_dados import coletando_info_usuario
 
def criar_usuario(users_list):
  text = """
#############################################################################################################################################
                                      FICAREMOS FELIZES EM TER VOÇE CONOSCO
     MAS PARA ISSO PRECISAREMOS DE ALGUMAS INFORMAÇÕES, POR ISSO RESPONDA TODAS AS PERGUNTAS ADEQUADAMENTE ;) VAMOS LÁ?
#############################################################################################################################################                                           
"""
  print(text)
  while(True):
    informacoes_usuario = coletando_info_usuario(users_list)
    
    if 'Erro' in informacoes_usuario:
      print(informacoes_usuario['Erro'])
      continue
    else:
      opcao_selected = exibir_menu_de_confirmacao(informacoes_usuario)
      if opcao_selected['Resposta'] == 'Ok':
        return informacoes_usuario
      elif opcao_selected['Resposta'] == 'Corrigir':
        continue
      elif opcao_selected['Resposta'] == 'Retornar':
        break
    break  