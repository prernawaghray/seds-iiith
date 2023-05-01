import csv
import database as db

###### This file needs to be executed first
###### Then execute main.py

PW = "LearnSQL@123" # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record" # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"
connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB 
db.create_switch_database(connection, DB, DB)


RELATIVE_CONFIG_PATH = '../config/'

USER = 'users'
ITEM = 'items'
ORDER = 'orders'

# Create the tables through python code here
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation

# creating users table
create_users_table = """
    CREATE TABLE users (
        user_id varchar(10) PRIMARY KEY,
        user_email varchar(50) NOT NULL,
        user_name varchar(50) NOT NULL,
        user_password varchar(45) NOT NULL,
        user_address varchar(60) NULL,
        is_vendor tinyint(1) DEFAULT 0
        )
"""
print("Creating the Users Table: ")
db.create_insert_query(connection, create_users_table)
print("Users Table created.")

# creating orders table
create_orders_table = """
    CREATE TABLE orders (
        order_id int NOT NULL PRIMARY KEY,
        customer_id varchar(10) NOT NULL,
        vendor_id varchar(10) NOT NULL,
        total_value float(45) NOT NULL,
        order_quantity int NOT NULL,
        reward_point int NOT NULL,
        FOREIGN KEY (vendor_id) REFERENCES users(user_id),
        FOREIGN KEY (customer_id) REFERENCES users(user_id)
    )
"""
print("Creating the Orders Table: ")
db.create_insert_query(connection, create_orders_table)
print("Orders Table created.")

# creating items table
create_items_table = """
    CREATE TABLE items (
        product_id varchar(45) NOT NULL PRIMARY KEY,
        product_name varchar(45) NOT NULL,
        product_description varchar(100) NOT NULL,
        vendor_id varchar(10) NOT NULL,
        product_price float(45) NOT NULL,
        emi_available varchar(10) NOT NULL,
        FOREIGN KEY (vendor_id) REFERENCES users(user_id)
    )
"""
print("Creating the Items Table: ")
db.create_insert_query(connection, create_items_table)
print("Items Table created.")


print("Initialising the data insertion in the Users Table:")
with open(RELATIVE_CONFIG_PATH+USER+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
    sql = """
        INSERT INTO USERS (user_id, user_name, user_email, user_password, user_address, is_vendor)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    db.insert_many_data(connection, sql, val)
    print("Data insertion into the Users Table completed.")

print("Initialising the data insertion in the Items Table:")
with open(RELATIVE_CONFIG_PATH+ITEM+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
    sql = """
            INSERT INTO ITEMS (product_id, product_name, product_price, product_description, vendor_id, emi_available)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
    db.insert_many_data(connection, sql, val)
    print("Data insertion into the Items Table completed.")

print("Initialising the data insertion in the Orders Table:")
with open(RELATIVE_CONFIG_PATH+ORDER+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    val.pop(0)
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
    sql = """
            INSERT INTO ORDERS (order_id, customer_id, vendor_id, total_value, order_quantity, reward_point)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
    db.insert_many_data(connection, sql, val)
    print("Data insertion into the Orders Table completed.")
