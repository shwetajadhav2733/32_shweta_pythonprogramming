
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

prime = []

for num in numbers:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)

print("Prime numbers in the list:", prime)
