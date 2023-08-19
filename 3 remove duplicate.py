def prepare_key(key):
    key = key.replace("j", "i")
    key = "".join(sorted(set(key), key=key.index))
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for char in key:
        alphabet = alphabet.replace(char, "")
    return key + alphabet

def create_matrix(key):
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    row, col = 0, 0
    for char in key:
        matrix[row][col] = char
        col += 1
        if col == 5:
            col = 0
            row += 1
    return matrix

def find_coords(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def encrypt(plain_text, matrix):
    plain_text = plain_text.replace("j", "i")
    if len(plain_text) % 2 != 0:
        plain_text += "x"
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i + 1]
        row1, col1 = find_coords(matrix, char1)
        row2, col2 = find_coords(matrix, char2)
        if row1 == row2:
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]
    return cipher_text

def main():
    key = "monarchy"
    plain_text = "instruments"
    
    key = prepare_key(key)
    matrix = create_matrix(key)
    
    print("Playfair Key Matrix:")
    for row in matrix:
        print(" ".join(row))
    
    cipher_text = encrypt(plain_text, matrix)
    print("Encrypted Text:", cipher_text)

if __name__ == "__main__":
    main()
