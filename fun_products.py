#=========================================#
#========== Funções de Produtos ==========#
#=========================================#

#-----------------------------------Imports----------------------------------#
import os
import validators
#----------------------------------Dicionário--------------------------------#

# código do produto = [nome, data de fabricação, data de validade, preço]
products = {}

#-----------------------------------Funções----------------------------------#


#==================================#
#========== Menu Produto ==========#
#==================================#

def products_menu():
    os.system('cls || clear')
    print("""
    #===========================================================#
    #===========|   Você está no Módulo Produtos   |============#               
    #===========================================================#
    #======|                                             |======#
    #======|        1 - Cadastrar Produto                |======#
    #======|        2 - Exibir Dados do Produto          |======#
    #======|        3 - Alterar Dados do Produto         |======#
    #======|        4 - Excluir Produto                  |======#
    #======|        0 - Retornar ao menu principal       |======#
    #======|                                             |======#
    #===========================================================#
    """)
    module2 = input("Escolha sua opção\n-> ")
    return module2


#=======================================#
#========== Cadastrar Produto ==========#
#=======================================#


def create_product():
    os.system('cls || clear')

    print("#=========================================#")
    print("#=========|  Cadastrar Produto  |=========#")
    print("#=========================================#")
    
    print("--" * 20)

#Código do produto
    code = str(input(" Código: "))
    code.strip().replace(' ', '')
    while not validators.validate_number(code) or code in products:
        print("Código Inválido ou já Existente!\n(Use Apenas Números)")
        print()
        code = str(input("->"))
        code.strip().replace(' ', '')
    print()
    
#Nome do produto
    product_name = str(input(" Nome: "))
    product_name = product_name.strip()
    print()
    
#Data de fabricação
    fabrication = str(input(" Data de Fabricação: "))
    while not validators.is_valid_date(fabrication):
        print("Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx)")
        print()
        fabrication = str(input("-> "))
        fabrication = fabrication.strip()
    print()

#Data de Validade
    validity = str(input(" Data de Validade: "))
    while not validators.is_valid_date(validity):
        print("Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx)")
        print()
        validity = str(input("-> "))
        validity = validity.strip()
    print()

#Preço do produto
    price = str(input(" Preço: "))
  
    print()
    products[code] = [product_name, fabrication, validity, price]
    print("--" * 20)
    print()
    print("Produto Cadastrado com Sucesso!")
    print()
    input("Pressione <ENTER> para continuar.")


#====================================#
#========== Exibir Produto ==========#
#====================================#


def read_product():
    os.system('cls || clear')

    print("#==========================================#")
    print("#===========|  Exibir Produto  |===========#")
    print("#==========================================#")
    print()
    code = input("Digite o Código do Produto: ")
    code.strip().replace(' ', '')
    print()
    if code in products:
        print("--" * 20)
        print("Nome: ", products[code][0])
        print()
        print("Data de Fabricação: ", products[code][1])
        print()
        print("Data de Validade: ", products[code][2])
        print()
        print("Preço: R$ ", products[code][3])
        print("--" * 20)
    else:
        print("Produto inexistente!")
                
    input("Pressione <ENTER> para continuar.")


#=====================================#
#========== Alterar Produto ==========#
#=====================================#


def update_product():
    os.system('cls || clear')

    print("#=========================================#")
    print("#==========|  Alterar Produto  |==========#")
    print("#=========================================#")

    code = input("Digite o Código do Produto: ")

    if code in products:
        print("--" * 20)
        print("Insira os novos dados:")
        print()
#Nome do produto
        product_name = str(input(" Nome: "))
        product_name = product_name.strip()
        print()
#Data de fabricação
        fabrication = input(" Data de Fabricação: ")
        while not validators.is_valid_date(fabrication):
            print("Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx)")
            print()
            fabrication = str(input("-> "))
            fabrication = fabrication.strip()
        print()
#Data de validade
        validity = input(" Data de Validade:")
        while not validators.is_valid_date(validity):
            print("Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx)")
            print()
            validity = str(input("-> "))
            validity = validity.strip()
        print()
#Preço do produto  
        price = input(" Preço: R$ ")
        
        print("--" * 20)
        products[code] = [product_name, fabrication, validity, price]
        print()
        print("Produto Alterado com Sucesso!")
        print()   
        input("Pressione <ENTER> para continuar.")
    else:
        print("Produto inexistente!")
        input("Pressione <ENTER> para continuar.")


#=====================================#
#========== Excluir Produto ==========#
#=====================================#


def delete_product():
    os.system('cls || clear')

    print("#=======================================#")
    print("#=========|  Excluir Produto  |=========#")
    print("#=======================================#")

    code = input("Digite o Código do Produto: ")
    code.strip().replace(' ', '')
    if code in products:
        print("--" * 20)
        print("Nome: ", products[code][0])
        print()
        print("Data de Fabricação: ", products[code][1])
        print()
        print("Data de Validade: ", products[code][2])
        print()
        print("Preço: R$ ", products[code][3])
        print("--" * 20)
        delete = str(input("Tem Certeza que Deseja Excluir esse Produto?[S/N]: "))
        if delete.upper() == "S":
            del products[code]
            print("Produto Excluído com Sucesso!")
            print()
            input("Pressione <ENTER> para continuar.")
        else:
            input("Pressione <ENTER> para continuar.")
    else:
        print("Produto inexistente!")
        input("Pressione <ENTER> para continuar.")