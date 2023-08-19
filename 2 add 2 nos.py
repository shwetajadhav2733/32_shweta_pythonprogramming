def add_binary(A, B):
    if len(A) > len(B):
        return add_binary(B, A)

    diff = len(B) - len(A)
    padding = '0' * diff
    A = padding + A
    res = []
    carry = '0'

    for i in range(len(A) - 1, -1, -1):
        if A[i] == '1' and B[i] == '1':
            if carry == '1':
                res.append('1')
                carry = '1'
            else:
                res.append('0')
                carry = '1'
        elif A[i] == '0' and B[i] == '0':
            if carry == '1':
                res.append('1')
                carry = '0'
            else:
                res.append('0')
                carry = '0'
        else:
            if carry == '1':
                res.append('0')
                carry = '1'
            else:
                res.append('1')
                carry = '0'

    if carry == '1':
        res.append(carry)

    res.reverse()

    index = 0
    while index + 1 < len(res) and res[index] == '0':
        index += 1

    return ''.join(res[index:])

# Driver code
a = "1101"
b = "100"
print(add_binary(a, b))
