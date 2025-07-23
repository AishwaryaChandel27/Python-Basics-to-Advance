#Typecasting = The process of converting a value of one data type to another data type string, integer, float, boolean
#str(), int(), float(), bool()

name = "Aisha"  #a string cannot be added to an integer,Float or boolean
#name += 1 #TypeError: can only concatenate str (not "int") to str

age = 23
gpa = 3.99
is_girl = True

print(type(name))  #Type is use to display the type of variable
print(type(age))  #int
print(type(gpa))  #float
print(type(is_girl))  #boolean

#Changing the type of variable

age = str(age)  #int to string
age += "1"  #string concatenation"
print(age)  #231

gpa = int(gpa)  #float to int
print(gpa)  #3

is_girl = str(is_girl)  #boolean to string
print(is_girl)  #True

#There are three types of typecasting

#1. Implicit Typecasting = Python automatically converts one data type to another without any user intervention
