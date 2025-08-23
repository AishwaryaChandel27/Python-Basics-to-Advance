
# Pattern Problems in Python
# This file contains various pattern printing programs

def print_star_pattern():
    """Print a simple star pattern"""
    rows = int(input("Enter number of rows: "))
    
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()

def print_number_pattern():
    """Print a number pattern"""
    rows = int(input("Enter number of rows: "))
    
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def print_pyramid_pattern():
    """Print a pyramid pattern"""
    rows = int(input("Enter number of rows: "))
    
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()

def main():
    print("Pattern Problems Menu:")
    print("1. Star Pattern")
    print("2. Number Pattern")  
    print("3. Pyramid Pattern")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        print_star_pattern()
    elif choice == "2":
        print_number_pattern()
    elif choice == "3":
        print_pyramid_pattern()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
