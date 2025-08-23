#Nested Loop are used to iterate over a sequence of elements and perform some action for each element.(outer loop : Inner loop)

for x in range (3):
    for y in range (1 , 10):
      print(y , end="")
    print()  

#Create a nested loop that prints the following pattern:
#pattern rectangle

row = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(row):
  for y in range(cols):
    print(symbol, end="")
  print()  