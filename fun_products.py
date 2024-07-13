#=========================================#
#========== Funções de Produtos ==========#
#=========================================#

#-----------------------------------Imports----------------------------------#
import os

#----------------------------------Dicionário--------------------------------#

# código do produto = [nome, data de fabricação, data de validade, preço]
products = {
    '123' : ["Dipirona monoidratada 500mg", "13/07/2024", "13/07/2025", "10,00" ],
    '456' : ["Ácido tranexâmico 250mg", "20/05/2024", "20/05/2026", "15,50"],
    '789' : ["Cetoprofeno 150mg", "15/03/2023", "15/08/2025", "12,00"]
}

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
    code = str(input(" Código: "))
    print()
    product_name = str(input(" Nome: "))
    print()
    fabrication = str(input(" Data de Fabricação: "))
    print()
    validity = str(input(" Data de Validade: "))
    print()
    price = str(input(" Preço: "))
    print()
    products[code] = [product_name, fabrication, validity, price]
    print(products)
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
        product_name = input("Nome: ")
        print()
        fabrication = input("Data de Fabricação: ")
        print()
        validity = input("Data de Validade:")
        print()
        price = input("Preço: R$ ")
        print("--" * 20)
        products[code] = [product_name, fabrication, validity, price]
        print(products)
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