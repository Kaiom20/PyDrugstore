#=================================#
#========== Validadores ==========#
#=================================#

#-----------------------------------Imports----------------------------------#


#-----------------------------------Funções----------------------------------#

#=================================#
#========== Validar Cpf ==========#  
#=================================#
#créditos: Flavius Gorgônio
def validate_cpf(cpf):
    
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0
    if tam != 11:
        return False
    for i in range(11):
        if (cpf[i]<'0')or(cpf[i]>'9'):
            return False
    for i in range(9):
        soma += (int(cpf[i])*(10 - i))
    d1 = 11 - (soma % 11)
    if (d1 == 10 or d1 == 11):
        d1 = 0
    if d1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += (int(cpf[i])*(11-i))
    d2 = 11 - (soma%11)
    if (d2 == 10 or d2 == 11):
        d2 = 0
    if d2 != int(cpf[10]):
        return False
    return True

#==================================#
#========== Validar Nome ==========#
#==================================#
#créditos: feito por mim 
def validate_name(client_name):
    client_name = client_name.replace(' ', '')
    if client_name.isalpha():
        return True
    else:
        return False
    
#======================================#
#========== Validar Telefone ==========#
#======================================#
#créditos: Flavius Gorgônio
def validate_phone(phone_number):
  phone_number = phone_number.replace(' ', '')
  phone_number = phone_number.replace('-', '')
  phone_number = phone_number.replace('(', '')
  phone_number = phone_number.replace(')', '')
  phone_number = phone_number.replace('+', '')
  tam = len(phone_number)
  if tam != 11:
    return False
  if not(phone_number.isdigit()):
    return False
  
  return True

