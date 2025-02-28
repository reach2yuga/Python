import pandas as pd
import mysql.connector

# Read CSV file
csv_file = "Project-2/customers-100.csv"  # Use forward slashes for cross-platform compatibility
df = pd.read_csv(csv_file)

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="yugandhara",
    password="yugandhara123",
    database="my_db"
)
cursor = conn.cursor()

# Create Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS SampleData (
        IndexId INT PRIMARY KEY,
        CustomerId VARCHAR(255),
        FirstName VARCHAR(255),
        LastName VARCHAR(255),
        Company VARCHAR(255)
    );
""")

# Insert Data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO SampleData2 (IndexId, CustomerId, FirstName, LastName, Company)
        VALUES (%s, %s, %s, %s, %s);
    """, (row[0], row[1], row[2], row[3], row[4]))

# Commit Changes and Close Connection
conn.commit()
cursor.close()
conn.close()
