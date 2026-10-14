# Create a Product class with product name, price, and quantity. Add an instance method to calculate the total cost. Take input from the user and display the product name and total cost.
class Product:
    def total(self):
        return self.price * self.quantity

p = Product()
p.name = input("Enter product name: ")
p.price = float(input("Enter price: "))
p.quantity = int(input("Enter quantity: "))

print("Product:", p.name)
print("Total Cost:", p.total())