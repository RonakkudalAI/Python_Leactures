class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def restock(self, amount):
        self.quantity += amount
        print(f"{amount} units added. New quantity: {self.quantity}")

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"{amount} units sold. Remaining quantity: {self.quantity}")
        else:
            print("Not enough stock to sell!")

# --- Application Task ---

# Create a product object
product1 = Product("Laptop", 50000, 10)

# Sell some units
product1.sell(3)

# Restock items
product1.restock(5)

# Display total value of remaining stock
print("Total value of remaining stock:", product1.total_value())