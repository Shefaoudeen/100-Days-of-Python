alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cipher_code(text, shift, direction):
    code = ""
    for letter in text:
        index = alphabet.index(letter)
        if direction == "encode":
            if index+shift < 26:
                code += alphabet[index+shift]
            else:
                code += alphabet[(index+shift) % 26]
        elif direction == "decode":
            if index-shift >= 0:
                code += alphabet[index-shift]
            else:
                code += alphabet[(index-shift) + 26]

    print(f"The encoded text is {code}")


cipher_code(text, shift, direction)
