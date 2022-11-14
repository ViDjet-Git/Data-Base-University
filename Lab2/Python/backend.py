
def add_customer(connection, customerName, deliveryPlace):
    try:
        cursor = connection.cursor()
        sql_query = """INSERT INTO public.\"Customer\" (\"C_Name\", \"D_Place\") 
        VALUES (%s, %s)"""
        record_to_insert = (customerName, deliveryPlace)
        cursor.execute(sql_query, record_to_insert)
        connection.commit()
        cursor.close()
        print("[INFO] customer {} (City: {}) was added".format(customerName, deliveryPlace))
    except Exception as _ex:
        print("[INFO] Error while adding customer: ", _ex)


def update_customer(connection, _id, customerName, deliveryPlace):
    try:
        cursor = connection.cursor()
        sql_query = """UPDATE public.\"Customer\" SET  \"C_Name\"='{}', \"D_Place\"='{}' 
        where \"C_ID\"={}""".format(customerName, deliveryPlace, _id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] updated customer id={}".format(_id))
    except Exception as _ex:
        print("[INFO] Error while updating customer: ", _ex)


def delete_customer(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = """DELETE FROM public.\"Customer\" WHERE \"C_ID\"={}""".format(_id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] deleted customer id={}".format(_id))
    except Exception as _ex:
        print("[INFO] Error while deleting customer: ", _ex)


def add_product(connection, productName, productPrice):
    try:
        cursor = connection.cursor()
        sql_query = """INSERT INTO public.\"Product\" (\"P_Name\", \"P_Price\") 
        VALUES(%s, %s)"""
        record_to_insert = (productName, productPrice)
        cursor.execute(sql_query, record_to_insert)
        connection.commit()
        cursor.close()
        print("[INFO] product {} (Price: {}) was added".format(productName, productPrice))
    except Exception as _ex:
        print("[INFO] Error while adding product: ", _ex)


def update_product(connection, _id, productName, productPrice):
    try:
        cursor = connection.cursor()
        sql_query = """UPDATE public.\"Product\" SET  \"P_Name\"='{}', \"P_Price\"={} 
        where \"P_ID\"={}""".format(productName, productPrice, _id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] updated product id={}".format(_id))
    except Exception as _ex:
        print("[INFO] Error while updating product: ", _ex)


def delete_product(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = """DELETE FROM public.\"Product\" WHERE \"P_ID\"={}""".format(_id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] deleted product id={}".format(_id))
    except Exception as _ex:
        print("[INFO] Error while delating product: ", _ex)


def add_delivery_company(connection, companyName):
    try:
        cursor = connection.cursor()
        sql_query = """INSERT INTO public.\"Delivery Company\" (\"DC_Name\") 
        VALUES(%s)"""
        record_to_insert = companyName
        cursor.execute(sql_query, record_to_insert)
        connection.commit()
        cursor.close()
        print("[INFO] Delivery company {} was added".format(companyName))
    except Exception as _ex:
        print("[INFO] Error while adding delivery company: ", _ex)


def update_delivery_company(connection, _id, companyName):
    try:
        cursor = connection.cursor()
        sql_query = """UPDATE public.\"Delivery Company\" SET  \"DC_Name\"='{}'
        where \"DC_ID\"={}""".format(companyName, _id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] updated delivery company by id={}".format(_id))
    except Exception as _ex:
        print("[INFO] Error while updating delivery company: ", _ex)


def delete_delivery_company(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = """DELETE FROM public.\"Delivery Company\" WHERE \"DC_ID\"={}""".format(_id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] deleted delivery company by id={}".format(_id))
    except Exception as _ex:
        print("[INFO] Error while deleting delivery company: ", _ex)


def add_product_to_customer(connection, customerID, productID, count):
    try:
        cursor = connection.cursor()
        sql_query = """INSERT INTO public.\"Customers_Products\" (\"Product_id\", \"Customer_id\", \"Product_count\") 
        VALUES({}, {}, {})""".format(productID, customerID, count)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] product id={} (Count: {}) was added to customer id={} ".format(productID, count, customerID))
    except Exception as _ex:
        print("[INFO] Error while adding product to customer", _ex)


def delete_product_from_customer(connection, customer_id, product_id):
    try:
        cursor = connection.cursor()
        sql_query = """DELETE FROM public.\"Customers_Products\" 
        WHERE \"Customer_id\"={} AND \"Product_id\"={}""".format(customer_id, product_id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] product id={} was deleted from customer id={} ".format(product_id, customer_id))
    except Exception as _ex:
        print("[INFO] Error while deleting product from customer", _ex)


def add_delivery_company_to_customer(connection, customerID, companyID):
    try:
        cursor = connection.cursor()
        sql_query = """INSERT INTO public.\"Customers_DCompanies\" (\"Customer_ID\", \"DC_ID\") 
        VALUES({}, {})""".format(customerID, companyID)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] DC id={} was added to customer id={}".format(companyID, customerID))
    except Exception as _ex:
        print("[INFO] Error while adding company to customer: ", _ex)


def update_delivery_company_to_customer_by_customer_id(connection, customerID, companyID):
    try:
        cursor = connection.cursor()
        sql_query = """UPDATE public.\"Customers_DCompanies\" SET  \"DC_ID\"='{}'
        where \"Customer_ID\"={}""".format(companyID, customerID)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] updated Customers_DCompanies by customer id={}".format(customerID))
    except Exception as _ex:
        print("[INFO] Error while updating Customers_DCompanies: ", _ex)


def delete_delivery_company_from_customer(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = """DELETE FROM public.\"Customers_DCompanies\" 
        WHERE \"Customer_ID\"={}""".format(_id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] deleted Customers_DCompanies by customer id={}".format(_id))
    except Exception as _ex:
        print("[INFO] Error while deleting Customers_DCompanies: ", _ex)


def add_delivery(connection, customerID):
    try:
        cursor = connection.cursor()
        sql_query = """INSERT INTO public.\"Delivery\" (\"Customer_ID\") 
        VALUES({})""".format(customerID)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] customer id={} ordered delivery".format(customerID))
    except Exception as _ex:
        print("[INFO] Error while adding delivery: ", _ex)


def delete_delivery(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = """DELETE FROM public.\"Delivery\" WHERE \"D_ID\"={}""".format(_id)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] delivery id={} was deleted".format(_id))
    except Exception as _ex:
        print("[INFO] Error while deleting delivery: ", _ex)


def select_all(connection, tableName):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"{}\"".format(tableName)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select all from {}".format(tableName))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting all from table", tableName,": ", _ex)


def select_customer_by_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Customer\" WHERE \"C_ID\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select customer by id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting customer by ID: ", _ex)


def select_product_by_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Product\" WHERE \"P_ID\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select product by id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting product by ID: ", _ex)


def select_delivery_company_by_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Delivery Company\" WHERE \"DC_ID\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select delivery company by id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting delivery company by ID: ", _ex)


def select_product_to_customer_by_customer_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Customers_Products\" WHERE \"Customer_id\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select customers_products by customer id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting customers_products by customer ID: ", _ex)


def select_product_to_customer_by_product_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Customers_Products\" WHERE \"Product_id\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select customers_products by product id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting customers_products by product ID: ", _ex)


def select_company_to_customer_by_customer_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Customers_DCompanies\" WHERE \"Customer_ID\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select customers_dcompanies by customer id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting customers_dcompanies by customer ID: ", _ex)


def select_company_to_customer_by_company_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Customers_DCompanies\" WHERE \"DC_ID\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select customers_dcompanies by company id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting customers_dcompanies by company ID: ", _ex)


def select_delivery_by_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Delivery\" WHERE \"D_ID\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select delivery by id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting delivery by ID: ", _ex)


def select_delivery_by_customer_id(connection, _id):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM \"Delivery\" WHERE \"Customer_ID\"={}".format(_id)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("[INFO] Select delivery by customer id={}".format(_id))
        return records
    except Exception as _ex:
        print("[INFO] Error while selecting delivery by customer ID: ", _ex)


def delete_all_from_table(connection, tableName):
    try:
        cursor = connection.cursor()
        sql_query = """DELETE FROM public.\"{}\"""".format(tableName)
        cursor.execute(sql_query)
        connection.commit()
        cursor.close()
        print("[INFO] All was deleted from table {}".format(tableName))
    except Exception as _ex:
        print("[INFO] Error while deleting data: ", _ex)


def auto_gen_int(connection, max_val, rows_number):
    try:
        query = 'SELECT trunc(random()*{}+1)::int from generate_series(1,{})'.format(max_val, rows_number)
        #print(query)
        cur = connection.cursor()
        cur.execute(query)
        return cur.fetchall()
    except Exception as _ex:
        print("[INFO] Error while generating data: ", _ex)


def auto_gen_char(connection, str_len, rows_number):
    try:
        part = 'chr(trunc(65 + random()*25)::int)'
        if str_len > 0:
            param = part + (' || ' + part) * (str_len - 1)

        query = 'SELECT {} from generate_series(1,{})'.format(param, rows_number)
        print(query)
        cur = connection.cursor()
        cur.execute(query)
        return cur.fetchall()
    except Exception as _ex:
        print("[INFO] Error while generating data: ", _ex)

def search1(connection, min_price, first_letter_c_name, first_letter_p_name):
    cursor = connection.cursor()
    sql = 'SELECT "C_Name", "P_Name", "P_Price", "Product_count"' \
            'FROM "Customers_Products" ' \
            'JOIN "Customer" ' \
            'ON "Customer"."C_ID" = "Customers_Products"."Customer_id" ' \
            'JOIN "Product" ' \
            'ON "Product"."P_ID" = "Customers_Products"."Product_id" ' \
            'WHERE "P_Price" > {} ' \
            'AND "C_Name" LIKE \'{}%\' ' \
            'AND "P_Name" LIKE \'{}%\' '.format(min_price, first_letter_c_name, first_letter_p_name)
    cursor.execute(sql)
    res = cursor.fetchall()
    print("\nSEARCH_1:\nC_Name, P_Name, P_Price, Product_count:")
    print(res)

def search2(connection, max_d_id, last_c_name, inside_d_place):
    cursor = connection.cursor()
    sql = 'SELECT "C_Name", "D_Place", "DC_Name" ' \
            'FROM "Customers_DCompanies" ' \
            'JOIN "Customer" ' \
            'ON "Customer"."C_ID" = "Customers_DCompanies"."Customer_ID" ' \
            'JOIN "Delivery Company" ' \
            'ON "Delivery Company"."DC_ID" = "Customers_DCompanies"."DC_ID" ' \
            'WHERE "Customers_DCompanies"."DC_ID" < {} ' \
            'AND "C_Name" LIKE \'%{}\' ' \
            'AND "D_Place" LIKE \'%{}%\''.format(max_d_id, last_c_name, inside_d_place)
    cursor.execute(sql)
    res = cursor.fetchall()
    print("\nSEARCH_2:\nC_Name, D_Place DC_Name:")
    print(res)

def search3(connection, min_id, max_id, l_c_name, i_d_place):
    cursor = connection.cursor()
    sql = 'SELECT "C_Name", "D_ID", "D_Place" ' \
            'FROM "Delivery" ' \
            'JOIN "Customer" ' \
            'ON "Customer"."C_ID" = "Delivery"."Customer_ID" ' \
            'WHERE "D_ID" >= {} AND "D_ID" <= {} ' \
            'AND "C_Name" LIKE \'%{}\' ' \
            'AND "D_Place" LIKE \'%{}%\''.format(min_id, max_id, l_c_name, i_d_place)
    cursor.execute(sql)
    res = cursor.fetchall()
    print("\nSEARCH_3:\nC_Name, D_ID, D_Place")
    print(res)