import pandas as pd
import sqlalchemy as sa
import pyodbc


df = pd.read_excel('C:\\Users\\rushi\\Documents\\Yuga\\ecommerce_customers.xlsx')
#print(df)
connection = pyodbc.connect(
        'DRIVER=ODBC Driver 17 for SQL Server;'
        'SERVER=(LocalDb)\LocalDBDemo;'
        'DATABASE=SQLPractice;'
        'Trusted_Connection=yes;'
    )



# Write DataFrame to SQL Server
df.to_sql(name='DimEmployee', con=connection, index=False, if_exists='fail')