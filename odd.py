def check_odd_even(numbers):
    odd_numbers = []
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return odd_numbers, even_numbers

# Example tuple of numbers
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

odd_numbers, even_numbers = check_odd_even(numbers_tuple)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)