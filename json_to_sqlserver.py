import json #The json module is used to work with JSON data
import pyodbc #pyodbc is a module that allows Python to interact with databases using ODBC (Open Database Connectivity)

# SQL Server connection parameters
server = '(localDB)\\yuga'  # e.g., 'localhost' or '192.168.1.1'
database = 'mydb'
username = 'yuga'
password = 'Admin@123'

# JSON data
json_data = """
[
  {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "department": "Engineering",
    "position": "Software Developer",
    "salary": 75000,
    "hire_date": "2019-06-15"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "age": 28,
    "department": "Marketing",
    "position": "Marketing Specialist",
    "salary": 65000,
    "hire_date": "2020-09-10"
  }
]
"""

# Parse the JSON data into a Python list of dictionaries
employees = json.loads(json_data)

# SQL query to insert data into the Employees table
insert_query = """
INSERT INTO Employees (id, name, age, department, position, salary, hire_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

# Establish a connection to the database and insert data
try:
    # Create the connection string
    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password};'
    )

    # Establish the connection
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            # Prepare data for batch insertion
            records = [
                (
                    emp['id'],
                    emp['name'],
                    emp['age'],
                    emp['department'],
                    emp['position'],
                    emp['salary'],
                    emp['hire_date']
                )
                for emp in employees
            ]

            # Execute batch insert
            cursor.executemany(insert_query, records)
            conn.commit()
            print(f"{len(records)} records successfully written to the SQL Server database!")

except pyodbc.Error as e:
    print("Error while connecting to SQL Server:", e)
