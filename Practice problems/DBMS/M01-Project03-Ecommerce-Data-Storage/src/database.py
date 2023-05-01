import mysql.connector
import random
import time
import datetime
from logging_function import writeLog
# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
	# Implement the logic to create the server connection
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, 
            user=user_name, 
            password=user_password
        )
        writeLog("SQL server connection established successfully", "INFO")
        print("SQL server connection established successfully")
    except mysql.connector.Error as e:
        print(f"Error occurred: {e}")
        writeLog(f"Error occurred: {e}", "ERROR")
    return connection 

# This method will create the database
def create_switch_database(connection, db_name):
    # For database creation use this method
    # If you have created your databse using UI, no need to implement anything
    mycursor = connection.cursor()
    try: 
        mycursor.execute("DROP DATABASE IF EXISTS {}".format(db_name))
        mycursor.execute("CREATE DATABASE {}".format(db_name))
        writeLog("Created database {} successfully".format(db_name), "INFO")
        print("Created database {} successfully".format(db_name))
        mycursor.execute("USE {}".format(db_name))
    except Exception as e:
        print(f"Error occurred: {e}")
        writeLog(f"Error occurred: {e}", "ERROR")


# This method will establish the connection with the newly created DB 
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, 
            user=user_name, 
            password=user_password,
            database=db_name
        )
        writeLog("Connected to database {}".format(db_name), "INFO")
        print("Connected to database {}".format(db_name))
    except Exception as e:
        print(f"Error occurred: {e}")
        writeLog(f"Error occurred: {e}", "ERROR")
    return connection 

# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, query):
	# This method will perform creation of the table
	# this can also be used to perform single data point insertion in the desired table
    mycursor = connection.cursor()
    try:
        mycursor.execute(query)
        connection.commit()
        writeLog("Data inserted successfully", "INFO")
        print("Data inserted successfully")
    except Exception as e:
        print(f"Error occurred: {e}")
        writeLog(f"Error occurred: {e}", "ERROR")
    
# retrieving the data from the table based on the given query
def select_query(connection, query):
    # fetching the data points from the table 
    result = None
    mycursor = connection.cursor()
    try:
        mycursor.execute(query)
        result = mycursor.fetchall()
        writeLog("Data retrieved", "INFO")
        print("Data retrieved")
    except Exception as e:
        print(f"Error occurred: {e}")
        writeLog(f"Error occurred: {e}", "ERROR")
    return result
    
# performing the execute many query over the table, 
# this method will help us to inert multiple records using a single instance
def insert_many_data(connection, sql, val):
    # to perform multiple insert operation in the database
    # sql = query
    # val = data being inserted
    mycursor = connection.cursor()
    try:
        mycursor.executemany(sql, val)
        connection.commit()
        writeLog("Multi-line insert completed", "INFO")
        print("Multi-line insert completed")
    except Exception as e:
        print(f"Error occurred: {e}")
        writeLog(f"Error occurred: {e}", "ERROR")