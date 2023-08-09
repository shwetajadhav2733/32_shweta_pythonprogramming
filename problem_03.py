
numbers_tuple = tuple(int(x) for x in input("Enter a tuple of numbers separated by spaces: ").split())
odd = []
even= []
for num in numbers_tuple:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Odd numbers in the tuple:", odd)
print("Even numbers in the tuple:", even)
