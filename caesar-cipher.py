letters = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]

def caesar_encode(message, shift):
    caesar_message = ''
    for char in message:
        if char in letters:
            shifted_letter = letters[letters.index(char)+shift]
            caesar_message += shifted_letter
        else:
            caesar_message += char
    print(caesar_message)

def caesar_decode(message, shift):
    caesar_message = ''
    for char in message:
        if char in letters:
            unshifted_letter = letters[letters.index(char) - shift]
            caesar_message += unshifted_letter
        else:
            caesar_message += char
    print(caesar_message)

choice = input("Type 'encode' to encrypt, type 'decode' to decrypt > ").lower()
while(choice != False):
    if choice == 'encode' or choice == 'decode':
        message = input('Type your message > ')
        shift = int(input('Type the shift number > '))
        caesar_encode(message, shift) if choice == 'encode' else caesar_decode(message, shift)
    else:
        choice = False
