import mysql.connector
import random
import time
import datetime

# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
	# Implement the logic to create the server connection
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL server connection established successfully.")
    except mysql.connector.Error as err:
        print(f"Error: '{err}' ")

    return connection

# This method will create the database
def create_switch_database(connection, db_name, switch_db):
    # For database creatio nuse this method
    # If you have created your databse using UI, no need to implement anything
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {switch_db}")
        print(f"Successfully connected to the Database {switch_db}.")
    except mysql.connector.Error as err:
        print(f"Database {db_name} does not exist.")
        if err:
            cursor.execute(f"CREATE SCHEMA {db_name}")
            print(f"Database {db_name} created successfully.")
            connection.database = db_name
        else:
            print(err)


# This method will establish the connection with the newly created DB 
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print(f"Database {db_name} connection successfully established.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return connection

# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, query):
# This method will perform creation of the table
# this can also be used to perform single data point insertion in the desired table
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    
# retrieving the data from the table based on the given query
def select_query(connection, query):
    # fetching the data points from the table
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# performing the execute many query over the table, 
# this method will help us to inert multiple records using a single instance
def insert_many_data(connection, sql, val):
    # to perform multiple insert operation in teh database
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query Successful.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

