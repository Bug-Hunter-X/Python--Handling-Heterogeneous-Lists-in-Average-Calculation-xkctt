def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = []
result = calculate_average(my_list) 
print(f"Average: {result}") #This will print 0, as expected

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list) 
print(f"Average: {result}") #This will print 3.0, as expected

my_list = [1, 2, 'a', 4, 5]
result = calculate_average(my_list) 
print(f"Average: {result}") #This will print 3.0, as expected because the code now ignores the string 'a' 