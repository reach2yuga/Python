import json

from colorama import Cursor
import mysql.connector

json_string= '''[
  {
    "id": 1,
    "name": "Alice",
    "age": 28,
    "city": "Toronto"
  },
  {
    "id": 2,
    "name": "Bob",
    "age": 34,
    "city": "Vancouver"
  }
]
'''

'''data = json.loads(json_string)

for person in data:
    print(person["name"], person["city"])'''

conn = mysql.connector.connect(
    host = "",
    username = "",
    password ="",
    database =""
)

Cursor() = conn.cursor()