#LogicalOperator : Logical operators are used to combine conditional statements.
#Logical operators are used to combine conditional statements: and , or , not
#This are used to combine multiple conditions in a single if statement.

#Example 1 : If the number is positive and even.

number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
  print("The number is positive and even.")

elif number > 0 and number % 2 != 0:
  print("The number is positive but not even.")
else:
  print("The number is negative")

#Example 2 : Or operator : if it is a square or a rectangle.

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
side4 = float(input("Enter the length of side 4: "))

if side1 == side2 == side3 == side4 or side1 == side3 and side2 == side4:
  print("It is a square or a rectangle.")

else:
  print("It is not a square or a rectangle.")