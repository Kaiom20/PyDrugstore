#================================#
#========== Interfaces ==========#
#================================#

#-----------------------------------Imports----------------------------------#
import os


#-----------------------------------Funções----------------------------------#


#====================================#
#========== Menu Principal ==========#
#====================================#


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
    #======|            4 - Módulo Relatórios            |======#  
    #======|            5 - Módulo Informações           |======#
    #======|            0 - Sair                         |======#
    #======|                                             |======#
    #===========================================================# 
    """)
    module = input("Escolha sua opção\n-> ")
    return module


#=================================#
#========== Informações ==========#
#=================================#


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
    #======|        Inspirações:                              |======#
    #======|          -> Projeto de Flavius Gorgônio          |======#
    #======|          -> Projeto de Diêgo Axel                |======#
    #================================================================#
    """)
    input("Pressione <ENTER> para continuar.")