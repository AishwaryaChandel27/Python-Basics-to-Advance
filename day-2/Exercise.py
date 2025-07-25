# Exercise 1: Rectangle Area calculator

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width

print("The area of the rectangle is: " + str(area)+"cm²")

# Exercise 2: Shopping Cart Program
# Create a shopping cart program where users can add items, view the cart, and calculate the total cost.

item = input("Enter the item you want to add to the cart: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

total = price * quantity

print(f"You have added {quantity} {item}(s) to your cart.")
print(f"The total cost for {item}(s) is: ${total:.2f}")