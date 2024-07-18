#==========================================#
#========== Funções de Relatório ==========#
#==========================================#

#-----------------------------------Imports----------------------------------#
import os
import fun_products as fp
import fun_sales as fs
import fun_clients as fc
#-----------------------------------Funções----------------------------------#

#====================================#
#========== Menu Relatório ==========#
#====================================#

def reports_menu():
    os.system('cls || clear')
    print("""
    #===========================================================#
    #==========|   Você está no Módulo Relatórios   |===========#               
    #===========================================================#
    #======|                                             |======#
    #======|        1 - Relatório Produtos               |======#
    #======|        2 - Relatório Vendas                 |======#
    #======|        3 - Relatório Clientes               |======#
    #======|        0 - Retornar ao menu principal       |======#
    #======|                                             |======#
    #===========================================================#
    """)
    module2 = input("Escolha sua opção\n-> ")
    return module2
    
#========================================#
#========== Relatório Produtos ==========#
#========================================#

def reports_products(products):
    os.system('cls || clear')
    print("#========================================#")
    print("#========== Relatório Produtos ==========#")
    print("#========================================#")
    print()
    print()
    print("--" * 25)
    print("||" * 25)
    print("--" * 25)
    for fp.code in products:
        print("Código do Produto: ",fp.code)
        print()
        print("Nome do Produto: ",products[fp.code][0])
        print()
        print("Data de Fabricação: ",products[fp.code][1])
        print()
        print("Data de Validade: ",products[fp.code][2])
        print()
        print("Preço do Produto: ", products[fp.code][3])
        print("--" * 25)
        print("||" * 25)
        print("--" * 25)
    
    print()
    input("Pressione <ENTER> para continuar.")
#======================================#
#========== Relatório Vendas ==========#
#======================================#

def reports_sales(sales):
    os.system('cls || clear')
    print("#========================================#")
    print("#=========== Relatório Vendas ===========#")
    print("#========================================#")
    print()
    print()
    print("--" * 25)
    print("||" * 25)
    print("--" * 25)
    for fs.sale_number in sales:
        print("Número da Venda: ",fs.sale_number)
        print()
        print("Código do Produto: ",sales[fs.sale_number][0])
        print()
        print("Quantidade de Itens: ",sales[fs.sale_number][1])
        print()
        print("Data da Venda: ",sales[fs.sale_number][2])
        print()
        print("Cpf do Cliente: ",sales[fs.sale_number][3])
        print("--" * 25)
        print("||" * 25)
        print("--" * 25)
    print()
    input("Pressione <ENTER> para continuar.")
#========================================#
#========== Relatório Clientes ==========#
#========================================#

def reports_clients(clients):
    os.system('cls || clear')
    print("#========================================#")
    print("#========== Relatório Clientes ==========#")
    print("#========================================#")
    print()
    print()
    print("--" * 25)
    print("||" * 25)
    print("--" * 25)
    for fc.cpf in clients:
        print("Cpf do Cliente: ",fc.cpf)
        print()
        print("Nome do Cliente: ",clients[fc.cpf][0])
        print()
        print("Telefone do Cliente: ",clients[fc.cpf][1])
        print("--" * 25)
        print("||" * 25)
        print("--" * 25)
    print()
    input("Pressione <ENTER> para continuar.")