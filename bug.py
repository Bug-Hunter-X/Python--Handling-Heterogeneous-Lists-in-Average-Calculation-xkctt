def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list) 
print(f"Average: {result}") #This will print 0, as expected

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list) 
print(f"Average: {result}") #This will print 3.0, as expected

my_list = [1, 2, 'a', 4, 5]
result = calculate_average(my_list) 
print(f"Average: {result}") # This will throw TypeError: unsupported operand type(s) for +: 'int' and 'str'