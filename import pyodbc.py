import pyodbc

try:
    connection = pyodbc.connect(
        'DRIVER=ODBC Driver 17 for SQL Server;'
        'SERVER=(LocalDb)\LocalDBDemo;'
        'DATABASE=SQLPractice;'
        'Trusted_Connection=yes;'
    )
    print("Connection successful")
except pyodbc.Error as e:
    print("Error:", e)
