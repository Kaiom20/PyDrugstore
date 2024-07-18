#=================================#
#========== Validadores ==========#
#=================================#

#-----------------------------------Imports----------------------------------#
import re

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
def validate_name(x):
    x = x.replace(' ', '')
    if x.isalpha():
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

#==================================#
#======== Validar Número ==========#
#==================================#
def validate_number(x):
    if x.isdigit():
        return True
    else:
        return False
    
#==================================#
#========== Validar Data ==========#
#==================================#
#créditos: feito por Google Gemini

def is_valid_date(date_str):
    try:
        day, month, year = date_str.split("/")  # Split by '/' separator
        day, month, year = int(day), int(month), int(year)  # Convert to integers

        # Check for valid day values
        if not 1 <= day <= 31:
            return False

        # Check for valid month values and adjust day range accordingly
        if not 1 <= month <= 12:
            return False
        elif month == 2 and not is_leap_year(year):  # Handle February for non-leap years
            if day > 28:
                return False
        elif month in [4, 6, 9, 11] and day > 30:
            return False

        # Check for valid year values
        if year < 1:
            return False

        return True  # All checks passed, date is valid

    except ValueError:  # Handle invalid input format
        return False

    except Exception as e:  # Handle unexpected errors
        print(f"Error during date validation: {e}")
        return False

def is_leap_year(year):

    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    return True


