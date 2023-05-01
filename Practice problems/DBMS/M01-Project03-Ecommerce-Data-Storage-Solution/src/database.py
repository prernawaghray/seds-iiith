import mysql.connector
import random
import time
import datetime

# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("MySQL Database connection successful")
    except Exception as err:
        print(f"Error: '{err}'")

    return connection

# This method will create the database
def create_switch_database(connection, db_name, switch_db):
    cursor = connection.cursor()
    try:
        drop_query = "DROP DATABASE IF EXISTS " + db_name
        db_query = "CREATE DATABASE " + db_name
        switch_query = "USE " + switch_db
        cursor.execute(drop_query)
        cursor.execute(db_query)
        cursor.execute(switch_query)
        print("Database created successfully")
    except Exception as err:
        print(f"Error in creating database: '{err}'")

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
        print("MySQL Database connection successful")
    except Exception as err:
        print(f"Error in creating connection with database: '{err}'")

    return connection

# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Exception as err:
        print(f"Error in insert query: '{err}'")

# retrieving the data from the table based on the given query
def select_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(f"Error in select query: '{err}'")

# performing the execute many query over the table, 
# this method will help us to inert multiple records using a single instance
def insert_many_data(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Exception as err:
        print(f"Error in insert many data query: '{err}'")