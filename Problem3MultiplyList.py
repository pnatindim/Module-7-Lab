# Patric Natindim
# March 12 2025

# Problem 3: Multiplies all the numbers in a list

num_list = [5, 2, 7, -1]

def multiplyList(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

print("Product:", multiplyList(num_list))
