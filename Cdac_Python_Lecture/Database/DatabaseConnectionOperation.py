# import mysql.connector

# #Connect
# conn = mysql.connector.connect(
#     host ="localhost",
#     user="root"
#     password="Ronak"
#     database="test"


# )
# cursor = conn.cursor()

# #Create DataBase
# cursor.execute("""
# CREATE Table IF NOT EXIST Student(
#                Student_id int Primary Key,
#                Name Varchar(50) NOT NULL,
#                Course varchar(50)
# )
# """)
# #Menu
# while True:
#    print("============Student Information System==========")
#    print("1.Inser Student Information")
#    print("2.Display Information")
#    print("3.Update student Information")
#    print("4.Delete Student Information")
#    print("5.Exiting")

#    choice = int(input("Enter you Coice"))  
   
#    #Insert 
#    if choice ==1:
#       st_id=int(input("Enter id"))
#       name = input("Enter Name")
#       course=input("Enter Course")

#       query= "Insert INTO Student(Student_id,Name,Course) VALUES (%s,%s,%s)"
#       values=(st_id,name,course)
#       cursor.execute(query,values)
#       conn.commit()
      
#       print("Student is added")

#     elif choice == 2:
#         cursor.execute("Select * From Student")
#         data = cursor.fetchall()

#         print("\nStudent List")
#         for row in data:
#             print(row)
      