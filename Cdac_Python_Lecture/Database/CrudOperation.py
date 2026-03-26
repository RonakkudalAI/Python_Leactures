import mysql.connector

# Connect
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ronak",
    database="test"
)
cursor = conn.cursor()

# Create Product Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Product(
    ProductId INT PRIMARY KEY,
    Name VARCHAR(50),
    Price FLOAT,
    Quantity INT
)
""")

# Menu
while True:
    print("\n===== Product Management =====")
    print("1. Insert Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # INSERT
    if choice == 1:
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        qty = int(input("Enter Quantity: "))

        query = "INSERT INTO Product (ProductId, Name, Price, Quantity) VALUES (%s, %s, %s, %s)"
        values = (pid, name, price, qty)

        cursor.execute(query, values)
        conn.commit()

        print(" Product Inserted!")

    # READ
    elif choice == 2:
        cursor.execute("SELECT * FROM Product")
        data = cursor.fetchall()

        print("\n📦 Product List:")
        for row in data:
            print(row)

    # UPDATE
    elif choice == 3:
        pid = int(input("Enter Product ID to update: "))
        price = float(input("Enter new Price: "))
        qty = int(input("Enter new Quantity: "))

        query = "UPDATE Product SET Price = %s, Quantity = %s WHERE ProductId = %s"
        values = (price, qty, pid)

        cursor.execute(query, values)
        conn.commit()

        print("✅ Product Updated!")

    # DELETE
    elif choice == 4:
        pid = int(input("Enter Product ID to delete: "))

        query = "DELETE FROM Product WHERE ProductId = %s"
        values = (pid,)

        cursor.execute(query, values)
        conn.commit()

        print("✅ Product Deleted!")

    # EXIT
    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("❌ Invalid choice!")

# Close
cursor.close()
conn.close()