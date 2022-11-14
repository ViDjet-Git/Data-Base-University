class View(object):

    @staticmethod
    def show_names():
        print("Customer")
        print("Product")
        print("Delivery Company")
        print("Customers_Products")
        print("Delivery")
        print("Customers_DCompanies")

    @staticmethod
    def show_table(table):
        for x in table:
            print(x)

    @staticmethod
    def display_input_error():
        print('**************************************************************')
        print('[ERROR] Input incorrect')
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item, table_name):
        print('**************************************************************')
        print('We already have {} in our {} table!'
              .format(item, table_name))
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, table_name):
        print('**************************************************************')
        print('We don\'t have any {} in our {} table. Please insert it first!'
              .format(item, table_name))
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item, table_name):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('We have just added {} to our {} table!'
              .format(item,table_name))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_update_item(older, newer, table):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change item from "{}" to "{}" in table {}'.format(older, newer, table))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(item, table):
        print('--------------------------------------------------------------')
        print('We have just removed id={} from our {} table'.format(item, table))
        print('--------------------------------------------------------------')

    @staticmethod
    def display_all_deletion(table):
        print('--------------------------------------------------------------')
        print('We have just removed ALL from our {} table'.format(table))
        print('--------------------------------------------------------------')

    @staticmethod
    def display_many_item_stored(count, table_name):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('We have just added {} random items to our {} table!'
              .format(count, table_name))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
