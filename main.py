#===========================================================#
#=================|  Projeto pyDrugstore  |=================#
#===========================================================#
#=======|     Sistema de Gestão de uma Farmácia     |=======#
#=======|      Sistemas de Informação / UFRN        |=======#
#=======|    Lógica e Algoritmos de Programação     |=======#
#=======|          Aluno: Kaio Márcio               |=======#
#===========================================================#


import validators
#-----------------------------------Imports----------------------------------#
import os
import fun_products
import fun_sales
import fun_clients
import interfaces
#---------------------------------Dicionários--------------------------------#



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
            module2 = fun_products.products_menu()
            print()
            if module2 == "1":
                fun_products.create_product()
            elif module2 == "2":
                fun_products.read_product()
            elif module2 == "3":
                fun_products.update_product()
            elif module2 == "4":
                fun_products.delete_product()
                         
    elif module == "2":
        module2 = " "
        while module2 != "0":
            module2 = fun_sales.sales_menu()
            print()
            if module2 == "1":
                fun_sales.create_sale()
            elif module2 == "2":
                fun_sales.read_sale()
            elif module2 == "3":
                fun_sales.update_sale()
            elif module2 == "4":
                fun_sales.delete_sale()
    
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

print("Programa Encerrado!")
