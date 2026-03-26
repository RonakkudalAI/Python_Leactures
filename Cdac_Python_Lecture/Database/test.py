import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ronak",
    database="test"
)

cursor = conn.cursor()

# Create Table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Student(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50),
#     age INT,
#     course VARCHAR(50)
# )
# """)

# Insert Data
query = "INSERT INTO Student(name, age, course) VALUES (%s, %s, %s)"
values =( ("Ronak", 22, "CDAC"),
         ("Manali",23,"MSC"),
         ("Shanu",25,"CA"),
         ("Kiran",29,"IT")
)

cursor.execute(query, values)
conn.commit()

print("Done successfully!")
