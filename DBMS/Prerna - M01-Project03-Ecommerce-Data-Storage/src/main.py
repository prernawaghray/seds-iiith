import database as db

#### Execute setup.py first, then execute this file

# Driver code
if __name__ == "__main__":

    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    PW = "LearnSQL@123" # IMPORTANT! Put your MySQL Terminal password here.
    ROOT = "root"
    DB = "ecommerce_record" # This is the name of the database we will create in the next step - call it whatever you like.
    LOCALHOST = "localhost"
    connection = db.create_server_connection(LOCALHOST, ROOT, PW)

    # creating the schema in the DB 
    db.create_switch_database(connection, DB, DB)

    # Start implementing your task as mentioned in the problem statement 
    # Implement all the test cases and test them by running this file
    print("Inserting additional data points in the Orders Table:")
    insert_into_orders1 = """
        INSERT INTO orders VALUES (101,7,1,23456,4,400);
    """
    db.create_insert_query(connection, insert_into_orders1)
    print("First insertion complete.")
    insert_into_orders2 = """
            INSERT INTO orders VALUES (102,5,2,1056,4,400);
        """
    db.create_insert_query(connection, insert_into_orders2)
    print("Second insertion complete.")
    insert_into_orders3 = """
            INSERT INTO orders VALUES (103,6,3,99999,2,600);
        """
    db.create_insert_query(connection, insert_into_orders3)
    print("Third insertion complete.")
    insert_into_orders4 = """
            INSERT INTO orders VALUES (104,10,4,45678,9,700);
        """
    db.create_insert_query(connection, insert_into_orders4)
    print("Fourth insertion complete.")
    insert_into_orders5 = """
            INSERT INTO orders VALUES (105,12,5,24986,3,200);
        """
    db.create_insert_query(connection, insert_into_orders5)
    print("Fifth insertion complete.")
    print("Data insertion into the Orders Table is complete.")

    # printing the count (cardinality) of Orders table
    select_count_orders = """SELECT COUNT(*) FROM orders"""
    results = db.select_query(connection, select_count_orders)
    print("The total count of Orders Table:", results)

    # printing details of all orders inserted into the Orders Table
    print("Details of all orders inserted into the Orders Table:")
    select_orders = """SELECT * FROM orders"""
    results = db.select_query(connection, select_orders)
    for result in results:
        print(result)
    print("Query complete.")

    # printing the order with minimum value
    print("The order with minimum value is:")
    select_min_orders = """SELECT * FROM orders WHERE total_value IN (SELECT MIN(total_value) FROM orders)"""
    results = db.select_query(connection, select_min_orders)
    for result in results:
        print(result)

    # printing the order with maximum value
    print("The order with maximum value is:")
    select_max_orders = """SELECT * FROM orders WHERE total_value IN (SELECT MAX(total_value) FROM orders)"""
    results = db.select_query(connection, select_max_orders)
    for result in results:
        print(result)

    # printing the orders with value greater than average order value
    print("The orders with value greater than average order value:")
    select_order_details = """SELECT * FROM orders WHERE total_value > (SELECT AVG(total_value) FROM orders)"""
    results = db.select_query(connection, select_order_details)
    for result in results:
        print(result)

    # creating customer leaderboard table
    print("Creating the customer leaderboard table:")
    create_customer_leaderboard = """
        CREATE TABLE customer_leaderboard (
        customer_id varchar(10) NOT NULL PRIMARY KEY,
        total_value float(50) NOT NULL,
        customer_name varchar(50) NOT NULL,
        customer_email varchar(50) NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES users(user_id)
        )
    """
    db.create_insert_query(connection, create_customer_leaderboard)
    print("Customer Leaderboard Table created.")

    print("Inserting data into the Customer Leaderboard Table:")
    insert_leaderboard_table = """ INSERT INTO customer_leaderboard (SELECT customer_id, MAX(total_value), user_name,
    user_email FROM orders, users WHERE users.user_id=orders.customer_id GROUP BY customer_id); """
    db.create_insert_query(connection, insert_leaderboard_table)
    print("Data inserted into the Customer Leaderboard Table.")

    #printing the customer leaderboard table values
    print("Customer Leaderboard Table data:")
    select_customer_leaderboard = """SELECT * FROM customer_leaderboard"""
    results = db.select_query(connection, select_customer_leaderboard)
    for result in results:
        print(result)