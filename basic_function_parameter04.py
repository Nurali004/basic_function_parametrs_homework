# Create a function named calculate_average that takes a list of numbers as a parameter.
def calculate_average(numbers):
# Inside the function, calculate the average of all the numbers in the given list.
    calculate= sum(numbers) / len(numbers)
# Return the average.
    return calculate

# Return the average.

my_list=[1, 2, 3, 4]
print(calculate_average(my_list))