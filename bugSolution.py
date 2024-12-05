def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    if total == 0:
        return 0 #handle only zero case
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of empty list is: {average_empty}")

my_list_with_zero = [0, 10, 20, 0, 30]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of list with zero is: {average_zero}")

my_list_all_zero = [0,0,0]
average_all_zero = calculate_average(my_list_all_zero)
print(f"The average of list with all zeros is: {average_all_zero}") 