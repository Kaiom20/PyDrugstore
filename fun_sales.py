#=======================================#
#========== Funções de Vendas ==========#
#=======================================#

#-----------------------------------Imports----------------------------------#
import os
import validators
#----------------------------------Dicionário--------------------------------#

# número da venda = [codigo do produto, quantidade, data da venda, cpf do comprador]
#sales = {}

#-----------------------------------Funções----------------------------------#


#================================#
#========== Menu Venda ==========#
#================================#


def sales_menu():
    os.system('cls || clear')
    print("""
    #==========================================================#
    #============|   Você está no Módulo Vendas   |============#              
    #==========================================================#
    #======|                                            |======#                                    
    #======|        1 - Cadastrar Venda                 |======#
    #======|        2 - Exibir Vendas                   |======#
    #======|        3 - Alterar Venda                   |======#
    #======|        4 - Excluir Venda                   |======#
    #======|        0 - Retornar ao menu principal      |======#
    #======|                                            |======#
    #==========================================================#
    """)
    module2 = input("Escolha sua opção\n-> ")
    return module2


#=====================================#
#========== Cadastrar Venda ==========#
#=====================================#


def create_sale(sales):
    os.system('cls || clear')

    print("#=========================================#")
    print("#==========|  Cadastrar Venda  |==========#")
    print("#=========================================#")
    print("--" * 20)
    
#Número da Venda // créditos: Fillipe Medeiros
    if not sales:
        sale_number = "1"
    else:
        sale_number = int(sorted(sales.keys())[-1]) + 1
        sale_number = str(sale_number)
    print()
    
#Codigo do produto 
    item = str(input(" Código do Produto: "))
    item = item.strip().replace(' ', '')
    while not validators.validate_number(item):
        print("Código de Produto Inválido! Tente Novamente.\n(Insira Apenas Números)")
        print()
        item = str(input("-> "))
        item = item.strip().replace(' ', '')
    print()


#Quantidade de produtos 
    quant = str(input(" Quantidade: "))
    quant = quant.strip().replace(' ', '')
    while not validators.validate_number(quant):
        print("Quantidade Inválida!, Tente Novamente\n(Insira Apenas Números)")
        print()
        quant = str(input("-> "))
        quant = quant.strip().replace(' ', '')
    print()
    
#Data da Venda 
    date = str(input(" Data da venda: ")) 
    while not validators.is_valid_date(date):
        print("Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx)")
        print()
        date = str(input("-> "))
        date = date.strip()
    print()

#Cpf do cliente 
    cpf = str(input(" Cpf do Cliente: "))
    cpf = cpf.strip()
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    while validators.validate_cpf(cpf) == False:
        print("Cpf Inválido, Tente Novamente.")
        print()
        cpf = str(input("-> "))
        cpf = cpf.strip()
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
        cpf = cpf.replace(' ', '')
    sales[sale_number] = [item, quant, date, cpf]
    print("--" * 20)
    print()
    print("Venda Cadastrada com Sucesso!")
    print()
    input("Pressione <ENTER> para continuar.")


#==================================#
#========== Exibir Venda ==========#
#==================================#


def read_sale(sales):
    os.system('cls || clear')

    print("#====================================#")
    print("#=========|  Exibir Venda  |=========#")
    print("#====================================#")
    print()
    sale_number = input("Insira o Número da Venda: ")
    sale_number = sale_number.strip().replace(' ', '')
    print()
    if sale_number in sales:
        print("--" * 20)
        print("Código do Produto: ", sales[sale_number][0])
        print()
        print("Quantidade: ", sales[sale_number][1])    
        print()
        print("Data da Venda: ", sales[sale_number][2])
        print()
        print("Cpf do Cliente: ", sales[sale_number][3])
        print("--" * 20)
    else:
        print("Venda Inexistente!")
    
    input("Pressione <ENTER> para prosseguir.")


#===================================#
#========== Alterar Venda ==========#
#===================================#


def update_sale(sales):
    os.system('cls || clear')

    print("#=====================================#")
    print("#=========|  Alterar Venda  |=========#")
    print("#=====================================#")

    sale_number = input("Insira o Número da Venda: ")
    sale_number = sale_number.strip().replace(' ', '')
    if sale_number in sales:
        print("--" * 20)
        
        print("Insira os Novos Dados:")
        print()
        item = str(input("Código do Produto: "))
        item = item.strip().replace(' ', '')
        while not validators.validate_number(item):
            print("Código de Produto Inválido! Tente Novamente.\n(Insira Apenas Números)")
            print()
            item = str(input("-> "))
            item = item.strip().replace(' ', '')
        
        print()
        
        quant = str(input("Quantidade: "))
        quant = quant.strip().replace(' ', '')
        while not validators.validate_number(quant):
            print("Quantidade Inválida!, Tente Novamente\n(Insira Apenas Números)")
            print()
            quant = str(input("-> "))
            quant = quant.strip().replace(' ', '')
        
        print()
        
        date = str(input("Data da Venda: "))
        while not validators.is_valid_date(date):
            print("Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx)")
            print()
            date = str(input("-> "))
            date = date.strip()
            
        print()
        
        cpf = str(input("Cpf do Cliente: "))
        cpf = cpf.strip()
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
        cpf = cpf.replace(' ', '')
        while validators.validate_cpf(cpf) == False:
            print("Cpf Inválido, Tente Novamente.")
            print()
            cpf = str(input("-> "))
            cpf = cpf.strip()
            cpf = cpf.replace('.', '')
            cpf = cpf.replace('-', '')
            cpf = cpf.replace(' ', '')
        
        print("--" * 20)
        sales[sale_number] = [item, quant, date, cpf]
        print()
        print("Venda Alterada com Sucesso!")
        print()
        input("Pressione <ENTER> para continuar.")
    else:
        print("Venda Inexistente!")
        input("Pressione <ENTER> para continuar.")


#===================================#
#========== Excluir Venda ==========#
#===================================#


def delete_sale(sales):
    os.system('cls || clear')

    print("#=====================================#")
    print("#=========|  Excluir Venda  |=========#")
    print("#=====================================#")

    sale_number = input("Insira o Número da Venda: ")
    sale_number = sale_number.strip().replace(' ', '')

    if sale_number in sales:
        print("--" * 20)
        print("Produto: ", sales[sale_number][0])
        print()
        print("Quantidade: ", sales[sale_number][1])
        print()
        print("Data da Venda: ", sales[sale_number][2])
        print("--" * 20)        
        delete = str(input("Tem Certeza que Deseja Excluir essa Venda?[S/N]: "))
        if delete.upper() == "S":
            del sales[sale_number]
            print("Venda Excluída com Sucesso!")
            print()
            input("Pressione <ENTER> para continuar.")
        else:
            input("Pressione <ENTER> para continuar.")
    else:
        print("Venda Inexistente!")
        input("Pressione <ENTER> para continuar.")