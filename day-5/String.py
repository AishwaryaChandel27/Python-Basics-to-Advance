#String : A string is a sequence of characters. A string can be enclosed in single quotes or double quotes. A string can be enclosed in triple quotes to span multiple lines.
#String can be concatenated using + operator. A string can be repeated using * operator. A string can be indexed using [] operator. A string can be sliced using [:] operator.
#A string can be iterated using for loop. A string can be checked for membership using in operator. A string can be checked for non-membership using not in operator.
#There are many string methods available in python. Some of them are : capitalize(), lower(), upper(), title(), swapcase(), strip(), lstrip(), rstrip(), replace(), split(), join(), find(), rfind(), index(), rindex(), count(),

#String Methods: Example of string methods

#Substring: A substring is a part of a string. A substring can be extracted using slice operator. A substring can be extracted using index operator. A substring can be extracted using find() method. A substring can be extracted using rfind() method

from re import split


name =  input("Enter your name: ")
result = len(name)  # len() function is used to find the length of a string.
print("The length of your name is: ", result)

cap = name.capitalize()  # capitalize() method is used to capitalize the first letter of a string.
print("Capitalize: ", cap)

find = name.find("a")  # find() method is used to find the index of a substring.
print("Find: ", find)

lastFind = name.rfind("w")  # rfind() method is used to find the index of a substring from right to left.
print ("Last Find: ", lastFind)

low = name.lower()  # lower() method is used to convert a string to lower case.
print("Lower: ", low)

up = name.upper()  # upper() method is used to convert a string to upper case.
print("Upper: ", up)

title = name.title()  # title() method is used to convert a string to title case.
print ("Title: ", title)

swap = name.swapcase()  # swapcase() method is used to swap the case of a string.
print("Swapcase: ", swap)

strip = name.strip("a")  # strip() method is used to remove the leading and trailing spaces of a string.
print ("Strip: ", strip)

lstrip = name.lstrip("w")  # lstrip() method is used to remove the leading spaces of a string.
print("Lstrip: ", lstrip)

rstrip = name.rstrip("c")  # rstrip() method is used to remove the trailing spaces of a string.
print("Rstrip: ", rstrip)

replace = name.replace("w", "c")  # replace() method is used to replace a substring with another substring.
print("Replace: ", replace)

split = name.split("a")  # split() method is used to split a string into a list.
print("Split: ", split)

join = name.join("a")  # join() method is used to join a list into a string.
print = ("Join: ", join)

index = name.index("a")  # index() method is used to find the index of a substring.



