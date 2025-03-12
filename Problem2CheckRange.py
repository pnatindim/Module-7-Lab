# Patric Natindim
# March 12 2025

# Problem 2: Prints whether a number is in or not in range(1,10)

def checkRange(num):
    if num in range(1, 11):
        print(f"{num} is in the range 1-10.")
    else:
        print(f"{num} is NOT in the range 1-10.")


number = int(input("Number: "))
checkRange(number)
