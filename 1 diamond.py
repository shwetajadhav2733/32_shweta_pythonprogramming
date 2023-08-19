n = 5

# Upper half of the diamond
for rows in range(1, n + 1):
    # Print spaces before the first asterisk
    print(" " * (n - rows), end="")
    
    # Print first asterisk
    print("*", end="")
    
    # Print spaces between asterisks
    print(" " * ((rows - 1) * 2), end="")
    
    # Print asterisk or newline
    if rows == 1:
        print()
    else:
        print("*")

# Lower half of the diamond
for rows in range(n - 1, 0, -1):
    # Print spaces before the first asterisk
    print(" " * (n - rows), end="")
    
    # Print first asterisk
    print("*", end="")
    
    # Print spaces between asterisks
    print(" " * ((rows - 1) * 2), end="")
    
    # Print asterisk or newline
    if rows == 1:
        print()
    else:
        print("*")
