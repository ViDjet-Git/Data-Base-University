import backend as b
import time


class ModelBasic(object):

    #додавання покупця
    def add_new_customer(self, connection, customerName, deliveryPlace):
        b.add_customer(connection, customerName, deliveryPlace)

    #редагування покупця
    def update_customer(self, connection, _id, customerName, deliveryPlace):
        b.update_customer(connection, _id, customerName, deliveryPlace)

    #видалення покупця
    def delete_customer(self, connection, _id):
        b.delete_customer(connection, _id)

    #додання продукту
    def add_new_product(self, connection, productName, productPrice):
        b.add_product(connection, productName, productPrice)

    #редагування продукту
    def update_product(self, connection, _id, productName, productPrice):
        b.update_product(connection, _id, productName, productPrice)

    #видалення продукту
    def delete_product(self, connection, _id):
        b.delete_product(connection, _id)

    #додавання компанії
    def add_new_delivery_company(self, connection, companyName):
        b.add_delivery_company(connection, companyName)

    #редагування компанії
    def update_delivery_company(self, connection, _id, companyName):
        b.update_delivery_company(connection, _id, companyName)

    #видалення компанії
    def delete_delivery_company(self, connection, _id):
        b.delete_delivery_company(connection, _id)

    #доданя елементу в таблицю Покупець/Продукти
    def add_product_to_customer(self, connection, customerID, productID, count):
        b.add_product_to_customer(connection, customerID, productID, count)

    #видалення елементу з таблиці Покупець/Продукти
    def delete_product_from_customer(self, connection, customer_id, product_id):
        b.delete_product_from_customer(connection, customer_id, product_id)

    #доданя елементу в таблицю Покупець/Компанія доставки
    def add_delivery_company_to_customer(self, connection, customerID, companyID):
        b.add_delivery_company_to_customer(connection, customerID, companyID)

    #редагування елементу в таблиці Покупець/Компанія доставки
    def update_delivery_company_to_customer_by_customer_id(self, connection, customerID, companyID):
        b.update_delivery_company_to_customer_by_customer_id(connection, customerID, companyID)

    #видалення елементу з таблиці Покупець/Компанія доставки
    def delete_delivery_company_from_customer(self, connection, _id):
        b.delete_delivery_company_from_customer(connection, _id)

    #доданя елементу в таблицю Доставка
    def add_delivery(self, connection, customerID):
        b.add_delivery(connection, customerID)

    #видалення елементу з таблиці Доставка
    def delete_delivery(self, connection, _id):
        b.delete_delivery(connection, _id)

    #вибірка всіх елементів таблиці
    def select_all(self, connection, tableName):
        return b.select_all(connection, tableName)

    #вибірка елемента покупця за його id
    def select_customer_by_id(self, connection, _id):
        return b.select_customer_by_id(connection, _id)

    # вибірка елемента продукту за його id
    def select_product_by_id(self, connection, _id):
        return b.select_product_by_id(connection, _id)

    # вибірка елемента компанії доставки за його id
    def select_delivery_company_by_id(self, connection, _id):
        return b.select_delivery_company_by_id(connection, _id)

    # вибірка елемента Покупець/Продукт за id покупця
    def select_product_to_customer_by_customer_id(self, connection, _id):
        return b.select_product_to_customer_by_customer_id(connection, _id)

    # вибірка елемента Покупець/Продукт за id продукту
    def select_product_to_customer_by_product_id(self, connection, _id):
        return b.select_product_to_customer_by_product_id(connection, _id)

    # вибірка елемента Покупець/Компанія Доставки за id покупця
    def select_company_to_customer_by_customer_id(self, connection, _id):
        return b.select_company_to_customer_by_customer_id(connection, _id)

    # вибірка елементів Покупець/Компанія Доставки за id компанії доставки
    def select_company_to_customer_by_company_id(self, connection, _id):
        return b.select_company_to_customer_by_company_id(connection, _id)

    # вибірка елемента Доставки за id
    def select_delivery_by_id(self, connection, _id):
        return b.select_delivery_by_id(connection, _id)

    # вибірка елемента Доставки за id покупця
    def select_delivery_by_customer_id(self, connection, _id):
        return b.select_delivery_by_customer_id(connection, _id)

    # видалення всієї таблиці
    def delete_all_from_table(self, connection, tableName):
        b.delete_all_from_table(connection, tableName)

    # генерування чисел
    def auto_gen_int(self, connection, max_val, rows_number):
        return b.auto_gen_int(connection, max_val, rows_number)

    # генерування рядків
    def auto_gen_char(self, connection, str_len, rows_number):
        return b.auto_gen_char(connection, str_len, rows_number)

    # пошук 1 і замір часу
    def search_1(self, connection, min_price, f_c_name, f_p_name):
        start_time = time.perf_counter()
        b.search1(connection, min_price, f_c_name, f_p_name)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000
        print(f"Search 1 Finished in {run_time:.4f} milliseconds")

    # пошук 2 і замір часу
    def search_2(self, connection, max_id, l_c_name, i_d_place):
        start_time = time.perf_counter()
        b.search2(connection, max_id, l_c_name, i_d_place)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000
        print(f"Search 1 Finished in {run_time:.4f} milliseconds")

    # пошук 3 і замір часу
    def search_3(self, connection, min_id, max_id, l_c_name, i_d_place):
        start_time = time.perf_counter()
        b.search3(connection, min_id, max_id, l_c_name, i_d_place)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000
        print(f"Search 3 Finished in {run_time:.4f} milliseconds")