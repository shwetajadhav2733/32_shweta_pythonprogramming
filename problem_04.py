
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key

print("Sorted list using insertion sort:", numbers)
