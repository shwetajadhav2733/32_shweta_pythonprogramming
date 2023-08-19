def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def extract_primes(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

# Take input from the user for the list of numbers
input_string = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_string.split()]

prime_numbers = extract_primes(numbers)
print("Prime numbers:", prime_numbers)