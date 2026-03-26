import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ronak",
    database="test"
)

cursor = conn.cursor()

# query = """
#         create table if not exists Employee(
#         EmpId int primary key,
#         Name varchar(50),
#         Mobile_No varchar(50),
#        Departmen varchar(50)
#         )
# """
#Insert Data

#Read Data
cursor.execute("SELECT * FROM Employee")

result = cursor.fetchall()

for row in result:
    print(row)



# cursor.executemany(query,values)
conn.commit()

# print("6 records inserted successfully!")    
print("Data Inserted Successfully!")     


cursor.close()