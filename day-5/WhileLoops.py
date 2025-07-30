#While Loops = A loop that will continue to execute a block of code while its condition remains true.
#basic syntax of while loop: while condition:  block of code

#Example of while loop:

name = input("Enter your name: ")

while name == "" :
    print("You did not enter your name!")
    name = input("Enter your name: ") #this is important to update the variable inside the loop, otherwise it will be an infinite loop.
  
print(f"Hello {name}")


age = int(input("Enter your age: "))

while age <= 0 :
    print("Age can't be negative!")
    age = int(input("Enter your age: "))

print(f"Your age is {age}")


flower = input("Enter your favorite flower (None to quit ): ")

while not flower == "None"  : #not is used to negate the condition.
    print(f"{flower} is a beautiful flower!")
    flower = input("Enter your another favorite flower (None to quit ): ")

print("Thank you for your input!")


num = int(input("Enter a number 1 to 10: "))

while num < 1 or num > 10 : #or is used to check multiple conditions.
  print (f"{num} is not in range 1 to 10")
  num = int(input("Enter a number 1 to 10: "))
print(f"You entered {num}")