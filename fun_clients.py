#=========================================#
#========== Funções de Clientes ==========#
#=========================================#

#-----------------------------------Imports----------------------------------#
import os
import validators
#----------------------------------Dicionário--------------------------------#

# cpf do cliente = [nome do cliente, telefone do cliente]
#clients = {}

#-----------------------------------Funções----------------------------------#


#==================================#
#========== Menu Cliente ==========#
#==================================#


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


#=======================================#
#========== Cadastrar Cliente ==========#
#=======================================#


def create_client(clients):
    os.system('cls || clear')

    print("#=========================================#")
    print("#=========|  Cadastrar Cliente  |=========#")
    print("#=========================================#")
    print("--" * 20)

#nome do cliente [OK]
    client_name = str(input(" Nome: "))
    client_name = client_name.strip()
    while validators.validate_name(client_name) == False:
        print("Nome Inválido! Tente Novamente\n(Insira Apenas Letras e Espaços)")    
        print()
        client_name = str(input("-> "))
        client_name = client_name.strip()
    print()
   
#cpf do cliente[OK]
    cpf = str(input(" Cpf: "))
    cpf = cpf.strip()
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    while validators.validate_cpf(cpf) == False or cpf in clients:
        print("Cpf Inválido ou já Existente, Tente Novamente.")
        print()
        cpf = str(input("-> "))
        cpf = cpf.strip()
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
        cpf = cpf.replace(' ', '')
    print()
   
#telefone do cliente [OK]
    phone_number = str(input(" Telefone: "))
    while validators.validate_phone(phone_number) == False:
        print("Número de Telefone Inválido! Tente Novamente\n(Utilize como referência o modelo: (xx) xxxxx-xxxx)")
        print()
        phone_number = str(input("-> "))
   
    print()
   
    clients[cpf] = [client_name, phone_number]
    print("--" * 20)
    print()
    print("Cliente Cadastrado com Sucesso!")
    print()
    input("Pressione <ENTER> para continuar.")


#====================================#
#========== Exibir Cliente ==========#
#====================================#


def read_client(clients):
    os.system('cls || clear')

    print("#======================================#")
    print("#=========|  Exibir Cliente  |=========#")
    print("#======================================#")

    cpf = str(input("Insira o Cpf do Cliente: "))
    cpf = cpf.strip()
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    if cpf in clients:
        print("--" * 20)
        print("Nome: ", clients[cpf][0])
        print()
        print("Telefone: ", clients[cpf][1])
        print("--" * 20)
    
    else:
        print("Cliente Inexistente!")
    
    input("Pressione <ENTER> para continuar.")


#=====================================#
#========== Alterar Cliente ==========#
#=====================================#


def update_client(clients):
    os.system('cls || clear')

    print("#=======================================#")
    print("#=========|  Alterar Cliente  |=========#")
    print("#=======================================#")

    cpf = str(input("Insira o Cpf do Cliente: "))
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    if cpf in clients:
        print("--" * 20)
        print("Insira os novos dados:")
        print()
        client_name = str(input("Nome: "))
        client_name = client_name.strip()
        while validators.validate_name(client_name) == False:
            print("Nome Inválido! Tente Novamente\n(Insira Apenas Letras e Espaços)")    
            print()
            client_name = str(input("-> "))
        
        print()
        
        phone_number = str(input("Telefone: "))
        while validators.validate_phone(phone_number) == False:
            print("Número de Telefone Inválido! Tente Novamente\n(Utilize como referência o modelo: (xx) xxxxx-xxxx)")
            print()
            phone_number = str(input("-> "))
        
        print("--" * 20)
        clients[cpf] = [client_name, phone_number]
        print()
        print("Cliente Alterado com Sucesso!")
        print()
        input("Pressione <ENTER> para continuar.")    
    else:
        print("Cliente Inexistente")
        input("Pressione <ENTER> para continuar.")


#=====================================#
#========== Excluir Cliente ==========#
#=====================================#


def delete_client(clients):
    os.system('cls || clear')

    print("#=======================================#")
    print("#=========|  Excluir Cliente  |=========#")
    print("#=======================================#")

    cpf = input("Insira o Cpf do Cliente: ")
    cpf = cpf.strip()
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
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