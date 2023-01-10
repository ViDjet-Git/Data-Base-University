from sqlalchemy import create_engine
from sqlalchemy import update, delete
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy import Column, Integer, ForeignKey, Text, Numeric


engine = create_engine('postgresql://postgres:fyl12345@localhost:5432/lab1')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class delivery(Base):
    __tablename__ = 'Delivery'
    D_ID = Column('D_ID', Integer, primary_key=True)
    Customer_ID = Column('Customer_ID', Text, ForeignKey('Customer.C_ID'), primary_key=True)

    def __repr__(self):
        return "<Delivery(Customer_ID='{}')>" \
            .format(self.Customer_ID)


class product(Base):
    __tablename__ = 'Product'
    P_ID = Column('P_ID', Integer, primary_key=True)
    P_Name = Column('P_Name', Text)
    P_Price = Column('P_Price', Numeric)

    def __repr__(self):
        return "<Product(P_Name='{}', P_Price='{}')>" \
            .format(self.P_Name, self.P_Price)


class customer(Base):
    __tablename__ = 'Customer'
    C_ID = Column('C_ID', Integer, primary_key=True)
    C_Name = Column('C_Name', Text)
    D_Place = Column('D_Place', Text)

    def __repr__(self):
        return "<Customer(C_Name='{}', D_Place='{}')>" \
            .format(self.C_Name, self.D_Place)


class delivery_company(Base):
    __tablename__ = 'Delivery Company'
    DC_ID = Column('DC_ID', Integer, primary_key=True)
    DC_Name = Column('DC_Name', Text)

    def __repr__(self):
        return "<Delivery Company(DC_Name='{}')>" \
            .format(self.DC_Name)


class customers_products(Base):
    __tablename__ = 'Customers_Products'
    Product_id = Column('Product_id', Integer, ForeignKey('Product.P_ID'), primary_key=True)
    Customer_id = Column('Customer_id', Integer, ForeignKey('Customer.C_ID'), primary_key=True)
    Product_count = Column('Product_count', Integer)

    def __repr__(self):
        return "<Customers_Products(Product_id='{}', Customer_id='{}', Product_count='{}')>" \
            .format(self.Product_id, self.Customer_id, self.Product_count)

class customers_DCompanies(Base):
    __tablename__ = 'Customers_DCompanies'
    Customer_ID = Column('Customer_ID', Integer, ForeignKey('Customer.C_ID'), primary_key=True)
    DC_ID = Column('DC_ID', Integer, ForeignKey('Delivery Company.DC_ID'), primary_key=True)

    def __repr__(self):
        return "<Customers_DCompanies(Customer_ID='{}', DC_ID='{}')>" \
            .format(self.Customer_ID, self.DC_ID)



s = Session()

def add_row(table_name, files):
    try:
        if(table_name == 'Customer'):
            temp = customer(
                C_Name=list(files.values())[0],
                D_Place=list(files.values())[1]
            )
        elif(table_name == 'Product'):
            temp = product(
                P_Name=list(files.values())[0],
                P_Price=list(files.values())[1]
            )
        elif(table_name == 'Delivery Company'):
            temp = delivery_company(
                DC_Name=list(files.values())[0]
            )
        elif(table_name == 'Delivery'):
            temp = delivery(
                Customer_ID=list(files.values())[0]
            )
        elif(table_name == 'Customers_Products'):
            temp = customers_products(
                Product_id=list(files.values())[0],
                Customer_id=list(files.values())[1],
                Product_count=list(files.values())[2]
            )
        elif(table_name == 'Customers_DCompanies'):
            temp = customers_DCompanies(
                Customer_ID=list(files.values())[0],
                DC_ID=list(files.values())[1]
            )
        s.add(temp)
        s.commit()
    except Exception as error:
        print(error)
        s.rollback()
        return False


def del_row(table_name, key, value):
    try:
        if type(value) is str:
            filter_txt = '"{}" = \'{}\''.format(key, value)
        else:
            filter_txt = '"{}" = {}'.format(key, value)

        if (table_name == 'Customer'):
            s.query(customer).filter(text(filter_txt)).delete(synchronize_session=False)
        elif (table_name == 'Product'):
            s.query(product).filter(text(filter_txt)).delete(synchronize_session=False)
        elif (table_name == 'Delivery Company'):
            s.query(delivery_company).filter(text(filter_txt)).delete(synchronize_session=False)
        elif (table_name == 'Delivery'):
            s.query(delivery).filter(text(filter_txt)).delete(synchronize_session=False)
        elif (table_name == 'Customers_Products'):
            s.query(customers_products).filter(text(filter_txt)).delete(synchronize_session=False)
        elif (table_name == 'Customers_DCompanies'):
            s.query(customers_DCompanies).filter(text(filter_txt)).delete(synchronize_session=False)

        s.commit()
    except Exception as error:
        print(error)
        s.rollback()
        return False


def edit_value(table_name, key, key_change, new_val, key_val):
    try:
        if (table_name == 'Customer'):
            table_class = customer
        elif (table_name == 'Product'):
            table_class = product
        elif (table_name == 'Delivery Company'):
            table_class = delivery_company
        elif (table_name == 'Delivery'):
            table_class = delivery
        elif (table_name == 'Customers_Products'):
            table_class = customers_products
        elif (table_name == 'Customers_DCompanies'):
            table_class = customers_DCompanies

        if key_val is str:
            filter_txt = "\"{}\" = '{}'".format(key, key_val)
        else:
            filter_txt = "\"{}\" = {}".format(key, key_val)

        update_values = {key_change: new_val}
        s.query(table_class) \
            .filter(text(filter_txt)) \
            .update(update_values, synchronize_session=False)
        s.commit()
    except Exception as error:
        print(error)
        s.rollback()
        return False






# add_row("Delivery Company", {'DC_Name': 'Nova Poshta'})
# add_row("Customers_DCompanies", {'Customer_ID': 1, 'DC_ID': 1})
#
# del_row('Customers_DCompanies', 'DC_ID', '1')
#
# edit_value("Delivery Company", "DC_ID", "DC_Name", "UkrPoshta", 2)