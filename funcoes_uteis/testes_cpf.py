def testando_cpf_ja_existe(cpf_digitado, users_list):
  for user in users_list:
    if user['CPF'] == cpf_digitado:
      return True
    break

def verificando_formato_cpf(cpf_digitado=''): # Função de validação do CPF
    cpf_digitado = cpf_digitado.replace('.', '')
    cpf_digitado = cpf_digitado.replace('-', '')
    if len(cpf_digitado) > 11 or len(cpf_digitado) < 11 or cpf_digitado == '':
        return False
    else:
        cpfDig = []
        cpfTest = []
        try:
            for a in cpf_digitado:
                a = int(a)
                cpfDig.append(a)
                cpfTest.append(a)
        except:
            return False
        # Calculando 1º Digito
        acumulador = 0
        dv1 = 0
        for cpf_digitado, i in enumerate(cpfTest):
            m = (cpf_digitado + 1) * i
            acumulador += m
            if cpf_digitado == 8:
                break
        dv1 = acumulador % 11
        if dv1 == 10:
            dv1 = 0
        cpfTest.pop(9)
        cpfTest.insert(9, dv1)
        # Caluculando 2º Digito
        acumulador2 = 0
        dv2 = 0
        for cpf_digitado, i in enumerate(cpfTest):
            m = cpf_digitado * i
            acumulador2 += m
            if cpf_digitado == 9:
                break
        dv2 = acumulador2 % 11
        if dv2 == 10:
            dv2 = 0
        cpfTest.pop(10)
        cpfTest.insert(10, dv2)
        if cpfTest == cpfDig:
            return True
        else:
            return False  