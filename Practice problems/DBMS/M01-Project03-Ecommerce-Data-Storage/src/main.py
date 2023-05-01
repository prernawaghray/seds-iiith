import database as db
from logging_function import writeLog

# Driver code
if __name__ == "__main__":

    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    PW = "LearnSQL123" # IMPORTANT! Put your MySQL Terminal password here.
    ROOT = "root"
    DB = "ecommerece_record" # This is the name of the database we will create in the next step - call it whatever you like.
    LOCALHOST = "localhost"
    
    
    connection = db.create_db_connection(LOCALHOST, ROOT, PW, DB)

    # creating the schema in the DB 
    db.create_switch_database(connection, DB, DB)

    # Start implementing your task as mentioned in the problem statement 
    # Implement all the test cases and test them by running this file

    print("----------------E-commerce data storage Solution ------------------")
    print("\n")
    print("----------------Solution - Problem 2.b ----------------------------")
    print("\n")
    # Here we will start inserting the data points into the orders table
    print("Inserting the additional data points in the orders table: ")
    orders_table = """
    INSERT INTO orders VALUES
    (101, 12456, 2, 300, '4', '13'),
    (102, 32678, 5, 100, '2', '14'),
    (103, 87612, 6, 200, '1', '15'),
    (104, 87623, 7, 120, '3', '6'),
    (105, 8971, 1, 0, '5', '7')
    """
    db.create_insert_query(connection, orders_table)
    # Data insertion in the orders table is completed. 
    print("------------------ Solution - Problem 2.b is completed. -----------")
    print("\n")

    print("-------------------- Solution - Problem 2.c -----------------------")
    print("\n")
    # Here we will start fetching data from the orders table

    print("Here is the details of all orders inserted in the table: ")
    q1 = """
    SELECT *
    FROM orders;
    """
    order_details = db.select_query(connection, q1)
    for result in order_details:
        print(result)

    print("------------------ Solution - Problem 2.c is completed. -----------")
    print("\n")

    print("-------------------- Solution - Problem 3.a -----------------------")
    print("\n")
    
    q2 = """
    SELECT * from orders 
    where total_value = (select MIN(total_value) 
    from orders);
    """

    min_order_detail = db.select_query(connection, q2)
    print("Order with minimum value is: ")
    print(min_order_detail)


    q3 = """
    SELECT * from orders 
    where total_value = (select MAX(total_value) 
    from orders);
    """

    max_order_detail = db.select_query(connection, q3)
    print("Order with maximum value is: ")
    print(max_order_detail)

    print("------------------ Solution - Problem 3.a is completed. -----------")
    print("\n")

    print("-------------------- Solution - Problem 3.b -----------------------")
    print("\n")
    
    print("All the order details with value greater than average order value: ")
    
    q4 = """
    SELECT * FROM orders WHERE total_value > (select AVG(total_value) 
    FROM orders);
    """
    high_order_value = db.select_query(connection, q4)
    for result in high_order_value:
        print(result)

    print("------------------ Solution - Problem 3.b is completed. -----------")
    print("\n")

    print("-------------------- Solution - Problem 3.c -----------------------")
    print("\n")
    
    print("Data fetch query is being created: ")
    q5 = """
    SELECT o.customer_id, MAX(o.total_value) as MAX_Value, c.user_name, c.user_email
    FROM ecommerce_record.orders o 
    LEFT JOIN ecommerce_record.users c ON o.customer_id = c.user_id 
    GROUP BY o.customer_id;
    """

    highest_purchase_per_customer = db.select_query(connection, q5)
    
    sql = '''
    INSERT INTO customer_leaderboard (customer_id, total_value, customer_name, customer_email) 
    VALUES (%s, %s, %s, %s)
    '''
    print("Initiating the data insertion in customer_leaderboard table: ")

    db.insert_many_data(connection, sql, highest_purchase_per_customer)
    print("Data is inserted in the table.")
    print("------------------ Solution - Problem 3.c is completed. -----------")
    print("\n")

