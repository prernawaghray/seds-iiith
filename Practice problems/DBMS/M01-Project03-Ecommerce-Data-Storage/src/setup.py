import csv
import database as db
from logging_function import writeLog

PW = "LearnSQL123" # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record" # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"
connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB 
db.create_switch_database(connection, DB)

RELATIVE_CONFIG_PATH = '../config/'

USER = 'users'
ITEM = 'items'
ORDER = 'orders'

# Create the tables through python code here
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation

# query definitions
create_users_table = '''
CREATE TABLE users (
    user_id VARCHAR(10) PRIMARY KEY,
    user_name VARCHAR(45) NOT NULL,
    user_email VARCHAR(45) NOT NULL,
    user_password VARCHAR(45) NOT NULL,
    user_address VARCHAR(45),
    is_vendor TINYINT(1) DEFAULT 0
)
'''

create_items_table = '''
CREATE TABLE items (
    product_id VARCHAR(45) PRIMARY KEY,
    product_name VARCHAR(45) NOT NULL,
    product_description VARCHAR(100) NOT NULL,
    product_price DOUBLE NOT NULL,
    emi_available VARCHAR(10) NOT NULL,
    vendor_id VARCHAR(10) FOREIGN KEY REFERENCES users(user_id)
)
'''

create_orders_table = '''
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    total_value DOUBLE NOT NULL,
    order_quantity INT NOT NULL,
    reward_point INT NOT NULL,
    vendor_id VARCHAR(10) FOREIGN KEY REFERENCES users(user_id),
    customer_id VARCHAR(10) FOREIGN KEY REFERENCES users(user_id)
)
'''

create_customer_leaderboard_table = '''
CREATE TABLE customer_leaderboard (
    customer_id VARCHAR(10) PRIMARY KEY,
    total_value DOUBLE NOT NULL,
    customer_name VARCHAR(50) NOT NULL,
    customer_email VARCHAR(50) NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES users(user_id)
)
'''

# creating tables using the above queries and functions defined in database.py file
print("Creating Users table")
writeLog("Creating Users table", "INFO")
db.create_insert_query(connection, create_users_table) 
print("Users table created")
writeLog("Users table created", "INFO")

print("Creating Items table")
writeLog("Creating Items table", "INFO")
db.create_insert_query(connection, create_items_table) 
print("Items table created")
writeLog("Items table created", "INFO")

print("Creating Orders table")
writeLog("Creating Orders table", "INFO")
db.create_insert_query(connection, create_orders_table)
print("Orders table created")
writeLog("Orders table created", "INFO")

print("Creating Customer leaderboard table")
writeLog("Creating Customer leaderboard table", "INFO")
db.create_insert_query(connection, create_customer_leaderboard_table) 
print("Customer leaderboard table created")
writeLog("Customer leaderboard table created", "INFO")

# inserting data into the tables

print("Inserting data into Users table")
writeLog("Inserting data into Users table", "INFO")
with open(RELATIVE_CONFIG_PATH+USER+'.csv', 'r') as f:
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    sql = '''
    INSERT INTO users (user_id, user_name, user_email, user_password, user_address, is_vendor) 
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    val.pop(0) # removing the header row from the .csv file which contains the column names
    db.insert_many_data(connection, sql, val)
print("Users table updated")
writeLog("Users table updated", "INFO")
   

print("Inserting data into Items table")
writeLog("Inserting data into Items table", "INFO")
with open(RELATIVE_CONFIG_PATH+ITEM+'.csv', 'r') as f:
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    sql = '''
    INSERT INTO items (product_id, product_name, product_price, product_description, vendor_id, emi_available) 
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    val.pop(0)
    db.insert_many_data(connection, sql, val)
print("Items table updated")
writeLog("Items table updated", "INFO")   


print("Inserting data into Orders table")
writeLog("Inserting data into Orders table", "INFO")
with open(RELATIVE_CONFIG_PATH+ORDER+'.csv', 'r') as f:
    """
    Here we have accessed the file data and saved into the val data struture, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    sql = '''
    INSERT INTO orders (order_id, customer_id, vendor_id, total_value, order_quantity, reward_point) 
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    val.pop(0)
    db.insert_many_data(connection, sql, val)
print("Orders table updated")
writeLog("Orders table updated", "INFO")
