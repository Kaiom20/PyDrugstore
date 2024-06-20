# ========== Projeto pyDrugstore ========== #
import os

#-----------------------Dicionários--------------------------#
products = {}


sales = {}


clients = {}

#------------------------------------------------------------

module = " "

while module != "0":
    os.system('cls || clear')

    print("""
    _________________________________________________________
    |=-=-=-=-=-=> Projeto de Gestão de Farmácia <=-=-=-=-=-=|
    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|         
    |=-=-=-=-=-=->    1 - Módulo Produtos      <-=-=-=-=-=-=|
    |=-=-=-=-=-=->    2 - Módulo Vendas        <-=-=-=-=-=-=|
    |=-=-=-=-=-=->    3 - Módulo Clientes      <-=-=-=-=-=-=|
    |=-=-=-=-=-=->    4 - Módulo Informações   <-=-=-=-=-=-=|  
    |=-=-=-=-=-=->    0 - Sair                 <-=-=-=-=-=-=|
    |                                                       |
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
    """)
    module = input("Escolha sua opção\n->")

   
    if module == "1":
        
        module2 = " "
        
        while module2 != "0":
            os.system('cls || clear')
            print("""
    __________________________________________________________
    |=-=-=-=-=-=-> Você está no Módulo Produtos <-=-=-=-=-=-=|              
    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
    |=-=-=-=-=->    1 - Cadastrar Produto          <-=-=-=-=-|
    |=-=-=-=-=->    2 - Exibir Dados do Produto    <-=-=-=-=-|
    |=-=-=-=-=->    3 - Alterar Dados do Produto   <-=-=-=-=-|
    |=-=-=-=-=->    4 - Excluir Produto            <-=-=-=-=-|
    |=-=-=-=-=->    0 - Retornar ao menu principal <-=-=-=-=-|
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)
            module2 = input("Escolha sua opção\n->")
        
           
            if module2 == "1":
                os.system('cls || clear')

                print("___________________________________________")
                print("|=-=-=-=-=-> Cadastrar Produto <-=-=-=-=-=|")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                
                print("--" * 10)
                name = str(input(" Nome: "))
                print()
                code = str(input(" Código: "))
                print()
                fabrication = str(input(" Data de Fabricação: "))
                print()
                validity = str(input(" Data de Validade: "))
                print()
                price = float(input(" Preço: "))
                print()
                products[code] = [name, fabrication, validity, price]
                print(products)
                print("--" * 10)
                print()
                print("Produto Cadastrado com Sucesso!")
                print()
                input("Pressione <ENTER> para continuar.")              

           
            elif module2 == "2":
                os.system('cls || clear')

                print("____________________________________________")
                print("|=-=-=-=-=-=->  Exibir Dados  <-=-=-=-=-=-=|")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

                code = input("Digite o Código do Produto: ")

                if code in products:
                    print("--" * 10)
                    print("Nome: ", products[code][0])
                    print("Data de Fabricação: ", products[code][1])
                    print("Data de Validade: ", products[code][2])
                    print("Preço: R$ ", products[code][3])
                    print("--" * 10)
                else:
                    print("Produto inexistente!")
                
                input("Pressione <ENTER> para continuar.")

            
            elif module2 == "3":
                os.system('cls || clear')

                print("___________________________________________")
                print("|=-=-=-=-=-=-> Alterar Dados <-=-=-=-=-=-=|")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

                code = input("Digite o Código do Produto: ")

                if code in products:
                    print("--" * 10)
                    print("Insira os novos dados:")
                    print()
                    name = input("Nome: ")
                    fabrication = input("Data de Fabricação: ")
                    validity = input("Data de Validade:")
                    price = input("Preço: R$ ")
                    print("--" * 10)
                    products[code] = [name, fabrication, validity, price]
                    print(products)
                    print()
                else:
                    print("Produto inexistente!")

                print("Produto Alterado com Sucesso!")
                print()   
                input("Pressione <ENTER> para continuar.")


            elif module2 == "4":
                os.system('cls || clear')

                print("___________________________________________")
                print("|=-=-=-=-=-> Excluir Produto <-=-=-=-=-=|")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

                code = input("Digite o Código do Produto: ")

                if code in products:
                    del products[code]

                else:
                    print("Produto inexistente!")
                
                print("Produto Excluído com Sucesso!")
                print()
                input("Pressione <ENTER> para continuar")





 #-----------------------------------------------------------------------#   
   
    elif module == "2":
        
        module2 = " "
        
        while module2 != "0":
            os.system('cls || clear')
            print("""
    ____________________________________________________________
    |=-=-=-=-=-=-=-> Você está no Módulo Vendas <-=-=-=-=-=-=-=|              
    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
    |=-=-=-=-=->    1 - Cadastrar Venda              <-=-=-=-=-|
    |=-=-=-=-=->    2 - Exibir Vendas                <-=-=-=-=-|
    |=-=-=-=-=->    3 - Alterar Venda                <-=-=-=-=-|
    |=-=-=-=-=->    4 - Excluir Venda                <-=-=-=-=-|
    |=-=-=-=-=->    0 - Retornar ao menu principal   <-=-=-=-=-|
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)
            module2 = input("Escolha sua opção\n->")

            if module2 == "1":
                os.system('cls || clear')

                print("___________________________________________")
                print("|-=-=-=-=-=-> Cadastrar Venda <-=-=-=-=-=-|")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

                

                

            elif module2 == "2":
                os.system('cls || clear')

                print("______________________________________")
                print("|=-=-=-=-=-> Exibir Venda <-=-=-=-=-=|")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

                

            elif module2 == "3":
                os.system('cls || clear')

                print("_______________________________________")
                print("|=-=-=-=-=-> Alterar Venda <-=-=-=-=-=|")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

                
            
            elif module2 == "4":
                os.system('cls || clear')

                print("_______________________________________")
                print("|=-=-=-=-=-> Excluir Venda <-=-=-=-=-=|")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")






        
        
        
        input("Pressione <ENTER> para continuar.")
#-------------------------------------------------------------------------#    
   
    elif module == "3":
        os.system('cls || clear')
        print("""
    ______________________________________________________________
    |=-=-=-=-=-=-=-> Você está no Módulo Clientes <-=-=-=-=-=-=-=|
    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
    |=-=-=-=-=->    1 - Cadastrar Cliente             <-=-=-=-=-=|
    |=-=-=-=-=->    2 - Consultar Cliente             <-=-=-=-=-=|
    |=-=-=-=-=->    3 - Alterar Cliente               <-=-=-=-=-=|
    |=-=-=-=-=->    4 - Excluir Cliente               <-=-=-=-=-=|
    |=-=-=-=-=->    0 - Retornar ao Menu Principal    <-=-=-=-=-=|
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)
        module2 = input("Escolha sua opção\n->")

        if module2 == "1":
            os.system('cls || clear')

            print("___________________________________________")
            print("|=-=-=-=-=-> Cadastrar Cliente <-=-=-=-=-=|")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

        

        elif module2 == "2":
            os.system('cls || clear')

            print("___________________________________________")
            print("|=-=-=-=-=-> Consultar Cliente <-=-=-=-=-=|")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")



        elif module2 == "3":
            os.system('cls || clear')

            print("_________________________________________")
            print("|=-=-=-=-=-> Alterar Cliente <-=-=-=-=-=|")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")



        elif module2 == "4":
            os.system('cls || clear')

            print("___________________________________________")
            print("|=-=-=-=-=-> Excluir Cliente <-=-=-=-=-=|")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        
        
        
        
        
        
        
        
        input("Pressione <ENTER> para continuar.")
#-------------------------------------------------------------------------#    
    elif module == "4":
        os.system('cls || clear')
        
        print("""
    ______________________________________________________________
    |-=-=-=-=-=-=> Você está no Módulo Informações <=-=-=-=-=-=-=|              
    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
    |=-=-=-=-=>    Projeto de Gestão de uma Farmácia   <=-=-=-=-=|
    |=-=-=-=-=>    Desenvolvedor: Kaio Márcio          <=-=-=-=-=|
    |=-=-=-=-=>    Email: kaio.lira.080@ufrn.edu.br    <=-=-=-=-=|
    |=-=-=-=-=>    Whatsapp: (83) 9 8716-3046          <=-=-=-=-=|
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    """)
        input("Pressione <ENTER> para continuar.")            
#-------------------------------------------------------------------------#

print("Programa Encerrado!")
