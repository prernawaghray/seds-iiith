import csv
import database as db

PW = "Manager#123" # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record" # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"
connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB 
db.create_switch_database(connection, DB, DB)


RELATIVE_CONFIG_PATH = '../config/'
USERS = 'users'
ITEM = 'items'
ORDER = 'orders'

# Creating users table
create_users_table = """
    CREATE TABLE users (
        user_id varchar(10) PRIMARY KEY,
        user_name varchar(45) NOT NULL,
        user_email varchar(45) NOT NULL,
        user_password varchar(45) NOT NULL,
        user_address varchar(45) NULL,
        is_vendor tinyint(1) DEFAULT 0
    )
    """

# create items table
create_items_table = """
    CREATE TABLE items (
      product_id varchar(45) NOT NULL PRIMARY KEY,
      product_name varchar(45) NOT NULL,
      product_description varchar(100) NOT NULL,
      product_price float(45) NOT NULL,
      emi_available varchar(10) NOT NULL,
      vendor_id varchar(10) NOT NULL,
      CONSTRAINT `fk_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `users` (`user_id`)
    )
    """
# create orders table
create_orders_table = """
    CREATE TABLE orders (
      order_id int NOT NULL PRIMARY KEY,
      total_value float(45) NOT NULL,
      order_quantity int NOT NULL,
      reward_point int NOT NULL,
      vendor_id varchar(10) NOT NULL,
      customer_id varchar(10) NOT NULL,
      CONSTRAINT `vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `users` (`user_id`),
      CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `users` (`user_id`)
    )
    """

# creating customer leaderboard table
create_customer_leaderboard = """
    CREATE TABLE customer_leaderboard (
      customer_id varchar(10) NOT NULL PRIMARY KEY,
      total_value float(45) NOT NULL,
      customer_name varchar(50) NOT NULL,
      customer_email varchar(50) NOT NULL,
      CONSTRAINT `fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `users` (`user_id`)
    )
    """

print("Initiating creation of users table: ")
db.create_insert_query(connection, create_users_table) # Execute our defined query
print("Users table created")

db.create_insert_query(connection, create_items_table) # Execute our defined query
print("Items table created")

db.create_insert_query(connection, create_orders_table) # Execute our defined query
print("Orders table created")

db.create_insert_query(connection, create_customer_leaderboard) # Execute our defined query
print("Customer leaderboard table created")

print("Data insertion in Users table is initiated: ")
with open(RELATIVE_CONFIG_PATH+USERS+'.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    sql = '''
    INSERT INTO users (user_id, user_name, user_email, user_password, user_address, is_vendor) 
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    val.pop(0)
    db.insert_many_data(connection, sql, val)
print("Data insetion in Users table is completed.")

print("Data insertion is Items table is initiated: ")
with open(RELATIVE_CONFIG_PATH+ITEM+'.csv', 'r') as f:
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
print("Data insetion in items table is completed.")

print("Data insertion is Orders table is initiated: ")
with open(RELATIVE_CONFIG_PATH+ORDER+'.csv', 'r') as f:
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

print("Data insetion in Order table is completed.")

