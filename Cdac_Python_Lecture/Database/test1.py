import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ronak",
    database="test"
)

cursor = conn.cursor()

# Create table
# create_query = """CREATE TABLE IF NOT EXISTS Customer(
#     customer_id INT PRIMARY KEY,
#     name VARCHAR(50),
#     age INT,
#     city VARCHAR(50)
# );"""

query = "update Customer set city ="


cursor.execute(create_query)

# Insert data
insert_query = """INSERT INTO Customer (customer_id, name, age, city)
VALUES (%s, %s, %s, %s)"""

values = [
    (1, 'Ronak', 22, 'Panvel'),
    (2, 'Manali', 23, 'Pune'),
    (3, 'Shanu', 25, 'Mumbai'),
    (4, 'Kiran', 29, 'Delhi')
]

cursor.executemany(insert_query, values)

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()