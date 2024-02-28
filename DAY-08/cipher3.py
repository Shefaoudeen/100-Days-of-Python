import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


def cipher_code(text, shift, direction):
    code = ""
    for letter in text:
        if letter in alphabet:
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
        else:
            code += letter
    print(f"The encoded text is {code}")


game_over = False

while not game_over:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher_code(text, shift, direction)
    decision = input(
        "would you like to continue? 'yes' for continue, 'no' for exit :").lower()
    if decision == "no":
        game_over = True

print("Goodbye")
