
# Practice for while loop 

# Problem 1: Simple While Loop
# Let's consider a simple example to illustrate the concept of a while loop:
print("=== Example 1: Basic While Loop ===")
i = 0
while i < 5:
    print(i)
    i += 1

print("\n=== Example 2: User Input While Loop ===")
n = int(input("Enter a number: "))
while n < 5:
    print(n)
    n = n + 1

print("\n=== Example 3: Countdown Loop ===")
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off!")

print("\n=== Example 4: Sum Calculator ===")
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Sum of numbers 1 to 10: {total}")
