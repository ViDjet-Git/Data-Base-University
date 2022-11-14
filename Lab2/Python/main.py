from view import View
from model import ModelBasic
from controller import Controller
import config
import psycopg2


def start(cfg):
    connect = psycopg2.connect(
                 host=cfg.host,
                 user=cfg.user,
                 password=cfg.password,
                 database=cfg.db_name
             )
    return connect

con = start(config)
c = Controller(ModelBasic(), View())

def menu():
    print("1. Add Element To Table")
    print("2. Update Element In Table")
    print("3. Delete Element From Table")
    print("4. Show Tables Names")
    print("5. Show Table")
    x = input("Enter number: ")
    if(x == '1'):
        c.add_to_table(con)
    elif(x == '2'):
        c.update_item(con)
    elif(x == '3'):
        c.delete_item_from_table(con)
    elif(x == '4'):
        c.show_tables_name()
    elif(x == '5'):
        c.show_table(con)
    else:
        print("Error... Enter correct number")
##############################################
#                      Menu
# while(True):
#     menu()


c.add_to_table_many_items(con,"Customer",10, 1000, 2)
# c.add_to_table_many_items(con,"Product",10, 1000)
# c.add_to_table_many_items(con,"Delivery Company", 5)
# print("\n///////////////// TABLES: ")
# c.show_tables_name()
# print("/////////////////")
# c.show_table(con)
# c.show_table(con)
# c.show_table(con)
# for x in range(6):
#      c.add_to_table(con)
# c.update_item(con)
# c.delete_item_from_table(con)
# print("TEST 100 ITEMS: ")
# c.add_to_table_many_items(con, "Delivery Company", 100000, 100, 10)
# c.show_table(con)
# c.search(con)
# for i in range(2):
#     c.delete_all_from_table(con)
