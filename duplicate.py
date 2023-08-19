def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Example list of integers with duplicates
numbers_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1]

print("Original list:", numbers_list)
unique_numbers = remove_duplicates(numbers_list)
print("Unique numbers:", unique_numbers)