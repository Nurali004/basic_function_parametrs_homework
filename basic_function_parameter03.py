# Create a function named find_smallest that takes a list of numbers as a parameter.
def find_smallest(numbers):
# Inside the function, find the smallest number in the given list.
    smallest=min(numbers)
# Return the smallest number.
    return smallest

my_list=[1, 2, 3, 4]
print(find_smallest(my_list))