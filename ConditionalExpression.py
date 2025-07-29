#Conditional Expression : Conditional expressions are used to evaluate a condition and return a value based on the condition.
#Conditional expressions are also known as ternary operators.
#Conditional expressions includes expressions that are evaluated to true or false.
#Types of conditional expressions are : if, elif, else, and, or, not, in, not in, is, is not, ==, !=, >, <, >=, <=

#in operator : The in operator is used to check if a value is present in a sequence (list, tuple, string) or dictionary.
#not in operator : The not in operator is used to check if a value is not present in a sequence (list, tuple, string) or dictionary.
#is operator : The is operator is used to check if two variables refer to the same object.
#is not operator : The is not operator is used to check if two variables do not refer to the same object.

#Example 1 
# This function checks a student's attendance and marks status.
# Parameters:
# - name: the name of the student (string)
# - marks: the marks obtained by the student (integer)
# - present_students: a list of student names who are present (list of strings)
#
# Returns a message based on the following conditions:
# 1. If the student is in the present_students list and has marks >= 50 → "Pass and Present"
# 2. If the student is in the list but has marks < 50 → "Fail but Present"
# 3. If the student is not in the list → "Absent"
# Additionally, if the name refers to the same object as the first student in the list (using 'is'),
# append " (Same Object)" to the message.
