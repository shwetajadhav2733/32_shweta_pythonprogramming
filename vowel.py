def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)

print("Number of vowels:", vowel_count)