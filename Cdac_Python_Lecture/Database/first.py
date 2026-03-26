import mysql.connector

print("Hello Ronak Kudal")

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ronak",
    database="test"   # remove .db
)

if con.is_connected():
    print("Connected to MySQL successfully!")