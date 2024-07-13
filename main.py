#===========================================================#
#=================|  Projeto pyDrugstore  |=================#
#===========================================================#
#=======|     Sistema de Gestão de uma Farmácia     |=======#
#=======|      Sistemas de Informação / UFRN        |=======#
#=======|    Lógica e Algoritmos de Programação     |=======#
#=======|          Aluno: Kaio Márcio               |=======#
#===========================================================#


#-----------------------------------Imports----------------------------------#
import os
   
#---------------------------------Dicionários--------------------------------#
# código do produto = [nome, data de fabricação, data de validade, preço]
products = {
    '123' : ["Dipirona monoidratada 500mg", "13/07/2024", "13/07/2025", "10,00" ],
    '456' : ["Ácido tranexâmico 250mg", "20/05/2024", "20/05/2026", "15,50"],
    '789' : ["Cetoprofeno 150mg", "15/03/2023", "15/08/2025", "12,00"]
}

# número da venda = [codigo do produto, quantidade, data da venda, cpf do comprador]
sales = {
    '001' : ["123", "2", "15/08/2024", "11122233344"],
    '002' : ["456", "1", "23/05/2024", "22233344455"],
    '003' : ["789", "1", "20/04/2023", "33344455566"]
}

# cpf do cliente = [nome do cliente, telefone do cliente]
clients = {
    '11122233344' : ["Kaio Márcio", "(83) 98716-3046"],
    '22233344455' : ["Rhuan Vítor", "(83) 98181-2929"],
    '33344455566' : ["José Alves", "(84) 99988-7722"]
}

#-----------------------------------Funções----------------------------------#
def main_menu():
    os.system('cls || clear')

    print("""
    #===========================================================#
    #===========|   Projeto de Gestão de Farmácia   |===========#
    #===========================================================#
    #======|                                             |======#
    #======|            1 - Módulo Produtos              |======#
    #======|            2 - Módulo Vendas                |======#
    #======|            3 - Módulo Clientes              |======#
    #======|            4 - Módulo Informações           |======#  
    #======|            0 - Sair                         |======#
    #======|                                             |======#
    #===========================================================# 
    """)
    module = input("Escolha sua opção\n-> ")
    return module
#----------------------------------------------------------------------------#
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
#----------------------------------------------------------------------------#
def create_product():
    os.system('cls || clear')

    print("#=========================================#")
    print("#=========|  Cadastrar Produto  |=========#")
    print("#=========================================#")
    
    print("--" * 20)
    product_name = str(input(" Nome: "))
    print()
    code = str(input(" Código: "))
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
    
#----------------------------------------------------------------------------#
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
#----------------------------------------------------------------------------#
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
#----------------------------------------------------------------------------#
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
#----------------------------------------------------------------------------#
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
#----------------------------------------------------------------------------#
def create_sale():
    os.system('cls || clear')

    print("#=========================================#")
    print("#==========|  Cadastrar Venda  |==========#")
    print("#=========================================#")
    print("--" * 20)
    sale_number = str(input("Informe o Número da Venda: "))
    print()
    item = str(input("Código do Produto: "))
    print()
    quant = str(input("Quantidade: "))
    print()
    data = str(input("Data da venda: "))
    print()
    cpf = str(input("Cpf do Cliente: "))
    sales[sale_number] = [item, quant, data, cpf]
    print(sales)
    print("--" * 20)
    print()
    print("Venda Cadastrada com Sucesso!")
    print()
    input("Pressione <ENTER> para continuar.")

#----------------------------------------------------------------------------#
def read_sale():
    os.system('cls || clear')

    print("#====================================#")
    print("#=========|  Exibir Venda  |=========#")
    print("#====================================#")
    print()
    sale_number = input("Insira o Número da Venda: ")
    print()
    if sale_number in sales:
        print("--" * 20)
        print("Produto: ", sales[sale_number][0])
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
#----------------------------------------------------------------------------#
def update_sale():
    os.system('cls || clear')

    print("#=====================================#")
    print("#=========|  Alterar Venda  |=========#")
    print("#=====================================#")

    sale_number = input("Insira o Número da Venda: ")

    if sale_number in sales:
        print("--" * 20)
        print("Insira os Novos Dados:")
        print()
        item = str(input("Código do Produto: "))
        print()
        quant = str(input("Quantidade: "))
        print()
        data = str(input("Data da Venda: "))
        print()
        cpf = str(input("Cpf do Cliente: "))
        print("--" * 20)
        sales[sale_number] = [item, quant, data, cpf]
        print(sales)
        print()
        print("Venda Alterada com Sucesso!")
        print()
        input("Pressione <ENTER> para continuar.")
    else:
        print("Venda Inexistente!")
        input("Pressione <ENTER> para continuar.")
#----------------------------------------------------------------------------#
def delete_sale():
    os.system('cls || clear')

    print("#=====================================#")
    print("#=========|  Excluir Venda  |=========#")
    print("#=====================================#")

    sale_number = input("Insira o Número da Venda: ")

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
#----------------------------------------------------------------------------#
def clients_menu():
    os.system('cls || clear')
    print("""
    #============================================================#
    #============|   Você está no Módulo Clientes   |============#
    #============================================================#
    #======|                                              |======#
    #======|        1 - Cadastrar Cliente                 |======#
    #======|        2 - Exibir Cliente                    |======#
    #======|        3 - Alterar Cliente                   |======#
    #======|        4 - Excluir Cliente                   |======#
    #======|        0 - Retornar ao Menu Principal        |======#
    #======|                                              |======#
    #============================================================#
    """)
    module2 = input("Escolha sua opção\n-> ")
    return module2
#----------------------------------------------------------------------------#
def create_client():
    os.system('cls || clear')

    print("#=========================================#")
    print("#=========|  Cadastrar Cliente  |=========#")
    print("#=========================================#")
    print("--" * 20)
    client_name = str(input("Nome: "))
    print()
    cpf = str(input("Cpf: "))
    print()
    phone_number = str(input("Telefone: "))
    print()
    clients[cpf] = [client_name, phone_number]
    print(clients)
    print("--" * 20)
    print()
    print("Cliente Cadastrado com Sucesso!")
    print()
    input("Pressione <ENTER> para continuar.")
#----------------------------------------------------------------------------#
def read_client():
    os.system('cls || clear')

    print("#======================================#")
    print("#=========|  Exibir Cliente  |=========#")
    print("#======================================#")

    cpf = str(input("Insira o Cpf do Cliente: "))

    if cpf in clients:
        print("--" * 20)
        print("Nome: ", clients[cpf][0])
        print()
        print("Telefone: ", clients[cpf][1])
        print("--" * 20)
    
    else:
        print("Cliente Inexistente!")
    
    input("Pressione <ENTER> para continuar.")
#----------------------------------------------------------------------------#
def update_client():
    os.system('cls || clear')

    print("#=======================================#")
    print("#=========|  Alterar Cliente  |=========#")
    print("#=======================================#")

    cpf = str(input("Insira o Cpf do Cliente: "))

    if cpf in clients:
        print("--" * 20)
        print("Insira os novos dados:")
        print()
        client_name = str(input("Nome: "))
        print()
        phone_number = str(input("Telefone: "))
        print("--" * 20)
        clients[cpf] = [client_name, phone_number]
        print(clients)
        print()
        print("Cliente Alterado com Sucesso!")
        print()
        input("Pressione <ENTER> para continuar.")    
    else:
        print("Cliente Inexistente")
        input("Pressione <ENTER> para continuar.")

    
#----------------------------------------------------------------------------#
def delete_client():
    os.system('cls || clear')

    print("#=======================================#")
    print("#=========|  Excluir Cliente  |=========#")
    print("#=======================================#")

    cpf = input("Insira o Cpf do Cliente: ")

    if cpf in clients:
        print("--" * 20)
        print("Nome: ", clients[cpf][0])
        print()
        print("Telefone: ", clients[cpf][1])
        print("--" * 20)
        delete = str(input("Tem Certeza que Deseja Excluir esse Cliente?[S/N]: "))
        if delete.upper() == "S":
            del clients[cpf]
            print("Cliente Excluído com Sucesso!")
            print()
            input("Pressione <ENTER> para continuar.")
        else:
            input("Pressione <ENTER> para continuar.")     
    else:
        print("Cliente Inexistente!")
        input("Pressione <ENTER> para continuar.")  
#----------------------------------------------------------------------------#
def info():
    os.system('cls || clear')
        
    print("""
    #================================================================#
    #============|   Você está no Módulo Informações   |=============#              
    #================================================================#
    #======|                                                  |======#
    #======|        Projeto de Gestão de uma Farmácia         |======#
    #======|        Desenvolvedor: Kaio Márcio                |======#
    #======|        Email: kaio.lira.080@ufrn.edu.br          |======#
    #======|        Whatsapp: (83) 9 8716-3046                |======#
    #======|                                                  |======#
    #================================================================#
    """)
    input("Pressione <ENTER> para continuar.")   
#=============================Programa Principal=============================#
module = " "
while module != "0":
    module = main_menu()

    if module == "1":
        module2 = " "
        while module2 != "0":
            module2 = products_menu()
            print()
            if module2 == "1":
                create_product()
            elif module2 == "2":
                read_product()
            elif module2 == "3":
                update_product()
            elif module2 == "4":
                delete_product()
                         
    elif module == "2":
        module2 = " "
        while module2 != "0":
            module2 = sales_menu()
            print()
            if module2 == "1":
                create_sale()
            elif module2 == "2":
                read_sale()
            elif module2 == "3":
                update_sale()
            elif module2 == "4":
                delete_sale()
    
    elif module == "3":
        module2 = " "
        while module2 != "0":
            module2 = clients_menu()
            print()
            if module2 == "1":
                create_client()
            elif module2 == "2":
                read_client()
            elif module2 == "3":
                update_client()
            elif module2 == "4":
                delete_client()
    
    elif module == "4":
        info()
#----------------------------------------------------------------------------#  
   
                
#----------------------------------------------------------------------------#    
   
    
#----------------------------------------------------------------------------#   
                 
#----------------------------------------------------------------------------#

print("Programa Encerrado!")
