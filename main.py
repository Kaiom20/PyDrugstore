#===========================================================#
#=================|  Projeto pyDrugstore  |=================#
#===========================================================#
#=======|     Sistema de Gestão de uma Farmácia     |=======#
#=======|      Sistemas de Informação / UFRN        |=======#
#=======|    Lógica e Algoritmos de Programação     |=======#
#=======|          Aluno: Kaio Márcio               |=======#
#===========================================================#


#-----------------------------------Imports----------------------------------#
import fun_products
import fun_sales
import fun_clients
import interfaces
import fun_reports
#============================ Programa Principal ============================#
module = " "
while module != "0":
    module = interfaces.main_menu()

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
            module2 = fun_clients.clients_menu()
            print()
            if module2 == "1":
                fun_clients.create_client()
            elif module2 == "2":
                fun_clients.read_client()
            elif module2 == "3":
                fun_clients.update_client()
            elif module2 == "4":
                fun_clients.delete_client()
    
    elif module == "4":
        module2 = ""
        while module2 != "0":
            module2 = fun_reports.reports_menu()
            print()
            if module2 == "1":
                fun_reports.reports_products()
            elif module2 == "2":
                fun_reports.reports_sales()
            elif module2 == "3":
                fun_reports.reports_clients()
    
    elif module == "5":
        interfaces.info()
               
#----------------------------------------------------------------------------#
print()
print("Programa Encerrado!")