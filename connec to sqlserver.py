import pyodbc

def check_sql_server_connection(server, database, username, password):
    try:
        # Create a connection string
        conn_str = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
        )

        # Establish a connection to the database
        with pyodbc.connect(conn_str) as conn:
            print("Connection to SQL Server was successful!")

            # Optional: You can execute a simple query to confirm
            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION;")  # This retrieves the SQL Server version
            row = cursor.fetchone()
            print("SQL Server Version:", row[0])

    except pyodbc.Error as e:
        print("Error while connecting to SQL Server:", e)

# Replace with your SQL Server connection details
server = '(localDB)\yuga'  # e.g., 'localhost' or '192.168.1.1'
database = 'mydb'
username = 'yuga'
password = 'Admin@123'

# Call the function to check the connection
check_sql_server_connection(server, database, username, password)
