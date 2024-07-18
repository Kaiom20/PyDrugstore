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
import pickle

# Recuperando dados do arquivo #

products = {}
try:
    arq_products = open("products.dat", "rb")
    products = pickle.load(arq_products)
except:
    arq_products = open("products.dat", "wb")
arq_products.close()


sales = {}
try:
    arq_sales = open("sales.dat", "rb")
    sales = pickle.load(arq_sales)
except:
    arq_sales = open("sales.dat", "wb")
arq_sales.close()


clients = {}
try:
    arq_clients = open("clients.dat", "rb")
    clients = pickle.load(arq_clients)
except:
    arq_clients = open("clients.dat", "wb")
arq_clients.close()

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
print("Até Logo!")

# Gravando dados em arquivo #

arq_products = open("products.dat", "wb")
pickle.dump(products, arq_products)
arq_products.close()

arq_sales = open("sales.dat", "wb")
pickle.dump(sales, arq_sales)
arq_sales.close()

arq_clients = open("clients.dat", "wb")
pickle.dump(clients, arq_clients)
arq_clients.close()