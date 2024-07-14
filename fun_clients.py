#=========================================#
#========== Funções de Clientes ==========#
#=========================================#

#-----------------------------------Imports----------------------------------#
import os

#----------------------------------Dicionário--------------------------------#

# cpf do cliente = [nome do cliente, telefone do cliente]
clients = {
    '11122233344' : ["Kaio Márcio", "(83) 98716-3046"],
    '22233344455' : ["Rhuan Vítor", "(83) 98181-2929"],
    '33344455566' : ["José Alves", "(84) 99988-7722"]
}

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


#====================================#
#========== Exibir Cliente ==========#
#====================================#


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


#=====================================#
#========== Alterar Cliente ==========#
#=====================================#


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


#=====================================#
#========== Excluir Cliente ==========#
#=====================================#


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