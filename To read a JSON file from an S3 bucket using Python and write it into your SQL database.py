'''[
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
'''

import json
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=yuga;'  # Replace with your SQL Server name or IP address
    'DATABASE=mydb;'     # Replace with your database name
   'UID=yuga;'     # Replace with your SQL Server username
    'PWD=Admin@123'     # Replace with your SQL Server password
    
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# JSON data - can be replaced with json.load(open('file.json'))
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

# Iterate over the list and insert each record into the SQL Server table
for employee in employees:
    # Create a tuple of values for each employee
    record = (
        employee['id'],
        employee['name'],
        employee['age'],
        employee['department'],
        employee['position'],
        employee['salary'],
        employee['hire_date']
    )

    # Execute the insertion query with the current employee's data
    cursor.execute(insert_query, record)

# Commit the transaction to save changes to the database
conn.commit()

# Close the cursor and database connection
cursor.close()
conn.close()

print("Data successfully written to the SQL Server database!")