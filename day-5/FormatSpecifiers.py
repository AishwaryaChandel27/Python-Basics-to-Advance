#Format Specifiers = {value:flags} format a value based on what Flags are inserted
#Flags are used to format a value based on what flags are inserted

# .(number) = round to that many decimal places (fixed-point)
# :(number) = minimum field width
# :03 = allocate 3 spaces and pad with 0's
# :< = left align/justify
# :> = right align/justify
# :^ = center align/justify
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# , = comma delimiter
# :% = percentage format


#example of format specifiers:

price1 = 49.99
price2 = 19.99
price3 = 29.99


print(f'Price 1: ${price1:,.2f}') # :,.2f = comma delimiter, 2 decimal places, fixed-point
print(f'Price 2: ${price2:,.2f}')
print(f'Price 3: ${price3:,.2f}')

print(f'Price 1: ${price1:000.2f}') # :03.2f = allocate 3 spaces and pad with 0's, 2 decimal places, fixed-point


print(f'Price 1: ${price1:^10.2f}')