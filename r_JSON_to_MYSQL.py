import mysql.connector
import json

# Sample JSON record
json_record = '''
{
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}
'''

# Parse the JSON record
data = json.loads(json_record)

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'yuga',
    'password': 'Admin@123',
    'database': 'mydb'
}
cursor = None  # Initialize cursor to None
connection = None  # Initialize connection to None
try:
    # Establish the database connection
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Prepare the INSERT statement
    insert_query = """
    INSERT INTO your_table (id, name, age, email)
    VALUES (%s, %s, %s, %s)
    """

    # Execute the INSERT statement
    cursor.execute(insert_query, (data['id'], data['name'], data['age'], data['email']))
    
    # Commit the transaction
    connection.commit()

    print("Record inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
