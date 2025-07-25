#input() function in Python to get user input
#This function reads a line from input (usually the user) and returns it as a string (removing the trailing newline).

name = input("Enter your name: ")
print("Hello, " + name + "!")

Age = input("Enter your age: ")
print("You are " + Age + " years old.")

#once you into a number you need to first convert it to int or float , As the input() function always returns a string.

year = input("Enter the year you were born: ")
age = 2025 - int(year)
print("You will be " + str(age) + " years old in 2025.")