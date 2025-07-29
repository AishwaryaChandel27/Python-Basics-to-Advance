import math 
#Conditional statement in Python : Conditional statements are used to perform different actions based on different conditions.

#If statement : Python supports the usual logical conditions from mathematics: Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Greater than or equal to: a >= b These conditions can be used in several ways, most commonly in "if statements" and loops. An "if statement" is written by using the if keyword.

#If statement are used to execute a block of code if a specified condition is true. If the condition is False, nothing happens: The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

# Example 1 : Right age to vote

age = int(input("Enter your age: "))
if age >= 18:
  print("You are eligible to vote.")
else :
  print("You are not eligible to vote.")

# Example 2 : If all sized are equal it is a square and if its a square find the area of the square.

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
side4 = float(input("Enter the length of side 4: "))

if side1 == side2 == side3 == side4 :
  print("All sides are equal, it is a square.")
  area = side1 * side2 # The area of the square is the length of one side squared.
  
  print("The area of the square is: ", area) # The area of the square
  
else:
  print ("All sides are not equal, it is not a square.")

#Elif statement : The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
#Elif is conditon is used to check multiple conditions.

#Example 3 : If the number is positive, negative or zero.

number = int(input("Enter a number: "))

if number < 0:
  print("The number is negative.")

elif number == 0:
  print("The number is zero.")

else:
  print("The number is positive.")
  # The else keyword catches anything which isn't caught by the preceding conditions.
  