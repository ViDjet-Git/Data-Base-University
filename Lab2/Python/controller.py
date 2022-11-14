def enter_table():
    name = input("Enter table name: ")
    return name


def check_table_name(name):
    if (name == 'Customer'):
        return True
    elif (name == 'Product'):
        return True
    elif (name == 'Delivery Company'):
        return True
    elif (name == 'Customers_Products'):
        return True
    elif (name == 'Delivery'):
        return True
    elif (name == 'Customers_DCompanies'):
        return True
    else:
        return False

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_tables_name(self):
        self.view.show_names()

    def add_to_table(self, connection):
        name = enter_table()
        i = 1
        if (name == 'Customer'):
            c_name = input("Enter Customer Name: ")
            d_place = input("Enter Delivery Place: ")
            self.model.add_new_customer(connection, c_name, d_place)
        elif (name == 'Product'):
            p_name = input("Enter Product Name: ")
            p_price = input("Enter Product Price: ")
            self.model.add_new_product(connection, p_name, p_price)
        elif (name == 'Delivery Company'):
            dc_name = input("Enter Delivery Company Name: ")
            self.model.add_new_delivery_company(connection, dc_name)
        elif (name == 'Customers_Products'):
            customer = input("Enter Customer ID: ")
            product = input("Enter Product ID: ")
            count = input("Enter Count of Product: ")
            if (self.model.select_customer_by_id(connection, customer) == [] or
            self.model.select_product_by_id(connection, product) == []):
                i = 0
            else:
                self.model.add_product_to_customer(connection, customer, product, count)
        elif (name == 'Delivery'):
            customer = input("Enter Customer ID: ")
            if (self.model.select_customer_by_id(connection, customer) == []):
                i = 0
            else:
                self.model.add_delivery(connection, customer)
        elif (name == 'Customers_DCompanies'):
            customer = input("Enter Customer ID: ")
            company = input("Enter Company ID: ")
            if (self.model.select_customer_by_id(connection, customer) == [] or
            self.model.select_delivery_company_by_id(connection, company) == []):
                i = 0
            else:
                self.model.add_delivery_company_to_customer(connection, customer, company)
        else:
            i = 0

        if(i == 1):
            _all = self.model.select_all(connection, name)
            for x in _all:
                item = x
            self.view.display_item_stored(item, name)
        elif(i == 0):
            self.view.display_input_error()

    def add_to_table_many_items(self, connection, name, count, max_val = 100, str_len = 5):
        if (name == 'Customer'):
            x = self.model.auto_gen_char(connection, str_len, count)
            y = self.model.auto_gen_char(connection, str_len, count)
            for i in range(count):
                c_name = x[i]
                d_place = y[i]
                self.model.add_new_customer(connection, c_name, d_place)

        elif (name == 'Product'):
            x = self.model.auto_gen_char(connection, str_len, count)
            y = self.model.auto_gen_int(connection, max_val, count)
            for i in range(count):
                p_name = x[i]
                p_price = y[i]
                self.model.add_new_product(connection, p_name, p_price)
        elif (name == 'Delivery Company'):
            x = self.model.auto_gen_char(connection, str_len, count)
            for i in range(count):
                dc_name = x[i]
                self.model.add_new_delivery_company(connection, dc_name)
        else:
            self.view.display_input_error()

        self.view.display_many_item_stored(count, name)

    def update_item(self, connection):
        name = enter_table()
        i = 1
        if (name == 'Customer'):
            c_id = input("Enter Customer ID: ")
            if(self.model.select_customer_by_id(connection, c_id) == []):
                i = 0
            else:
                c_name = input("Enter NEW Customer Name: ")
                d_place = input("Enter NEW Delivery Place: ")
                old = self.model.select_customer_by_id(connection, c_id)
                self.model.update_customer(connection, c_id, c_name, d_place)
                new = self.model.select_customer_by_id(connection, c_id)
        elif (name == 'Product'):
            p_id = input("Enter Product ID: ")
            if (self.model.select_product_by_id(connection, p_id) == []):
                i = 0
            else:
                p_name = input("Enter NEW Product Name: ")
                p_price = input("Enter NEW Product Price: ")
                old = self.model.select_product_by_id(connection, p_id)
                self.model.update_product(connection, p_id, p_name, p_price)
                new = self.model.select_product_by_id(connection, p_id)
        elif (name == 'Delivery Company'):
            dc_id = input("Enter Delivery Company ID: ")
            if (self.model.select_delivery_company_by_id(connection, dc_id) == []):
                i = 0
            else:
                dc_name = input("Enter NEW Delivery Company Name: ")
                old = self.model.select_delivery_company_by_id(connection, dc_id)
                self.model.update_delivery_company(connection, dc_id, dc_name)
                new = self.model.select_delivery_company_by_id(connection, dc_id)
        elif (name == 'Customers_DCompanies'):
            customer = input("Enter Customer ID: ")
            if (self.model.select_company_to_customer_by_customer_id(connection, customer) == []):
                i = 0
            else:
                company = input("Enter NEW Company ID: ")
                old = self.model.select_company_to_customer_by_customer_id(connection, customer)
                self.model.update_delivery_company_to_customer_by_customer_id(connection, customer, company)
                new = self.model.select_company_to_customer_by_customer_id(connection, customer)
        else:
            i = 0

        if(i == 1):
            self.view.display_update_item(old, new, name)
        elif(i == 0):
            self.view.display_input_error()

    def delete_all_from_table(self, connection):
        name = enter_table()
        self.model.delete_all_from_table(connection, name)
        self.view.display_all_deletion(name)

    def delete_item_from_table(self, connection):
        name = enter_table()
        i = 1
        if (name == 'Customer'):
            _id = input("Enter Customer ID: ")
            if(self.model.select_product_to_customer_by_customer_id(connection, _id) != [] or
            self.model.select_company_to_customer_by_customer_id(connection, _id) != [] or
            self.model.select_delivery_by_customer_id(connection, _id) != []):
                i = 0
            else:
                self.model.delete_customer(connection, _id)
        elif (name == 'Product'):
            _id = input("Enter Product ID: ")
            if (self.model.select_product_to_customer_by_product_id(connection, _id) != []):
                i = 0
            else:
                self.model.delete_product(connection, _id)
        elif (name == 'Delivery Company'):
            _id = input("Enter Delivery Company ID: ")
            if(self.model.select_company_to_customer_by_company_id(connection, _id) != []):
                i = 0
            else:
                self.model.delete_delivery_company(connection, _id)
        elif (name == 'Customers_Products'):
            customer = input("Enter Customer ID: ")
            product = input("Enter Product ID: ")
            self.model.delete_product_from_customer(connection, customer, product)
            _id = customer + " and " + product
        elif (name == 'Delivery'):
            _id = input("Enter Delivery ID: ")
            self.model.delete_delivery(connection, _id)
        elif (name == 'Customers_DCompanies'):
            _id = input("Enter Customer ID: ")
            self.model.delete_delivery_company_from_customer(connection, _id)
        else:
            i = 0

        if(i == 1):
            self.view.display_item_deletion(_id, name)
        elif(i == 0):
            self.view.display_input_error()

    def show_table(self, connection):
        name = enter_table()
        table = self.model.select_all(connection, name)
        if(table == []):
            print("Table don't have items")
        else:
            self.view.show_table(table)

    def auto_gen_int(self, connection, rows_number, max_val=100):
        return self.model.auto_gen_int(connection, max_val, rows_number)

    def auto_gen_char(self, connection, rows_number, str_len=5):
        return self.model.auto_gen_char(connection, str_len, rows_number)

    def search(self, connection):
        # first
        price = input("Enter min price: ")
        f_c_name = input("Enter First Letter of Customer Name: ")
        f_p_name = input("Enter First Letter of Product Name: ")
        self.model.search_1(connection, price, f_c_name, f_p_name)
        # second
        _id = input("Enter max DC_ID: ")
        l_c_name = input("Enter Last Letter of Customer Name: ")
        i_d_place = input("Enter Part of Product Name: ")
        self.model.search_2(connection, _id, l_c_name, i_d_place)
        # third
        min_id = input("Enter min D_ID: ")
        max_id = input("Enter max D_ID: ")
        l_c_name = input("Enter Last Letter of Customer Name: ")
        i_d_place = input("Enter Part of Product Name: ")
        self.model.search_3(connection, min_id, max_id, l_c_name, i_d_place)