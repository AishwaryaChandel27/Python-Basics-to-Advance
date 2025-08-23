#For Loop in pyhton is used to iterate over a sequence (list, tuple, dictionary, set, or string).
#The for loop can iterate over the items of any iterable object, and it can iterate over a sequence of numbers using the range() and xrange() functions.
#the best example of for loop is to iterate over a list of items.that can be done using for loop.

n =  int(input("Enter the number of elements in list: "))
a = []
for i in range(0, n):
    elem = int(input("Enter element: "))
    a.append(elem)
    avg = sum(a)/n
    print("Average of elements in the list", round(avg, 2))

