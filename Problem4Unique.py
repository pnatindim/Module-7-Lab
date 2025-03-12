# Patric Natindim
# March 12 2025

# Problem 4: Takes a list of numbers and returns a new list with unique elements of the first list

num_list = [1, 3, 3, 3, 6, 2, 3, 5]

def uniqueElements(numbers):
    list = []  
    for num in numbers:
        if num not in list:  
            list.append(num)  
    return list

print("Unique list:", uniqueElements(num_list))
