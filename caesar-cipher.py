from art import logo

letters = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
choice = True

def caesar_cipher(message, shift, choice):
    caesar_message = ''
    for char in message:
        if char in letters:
            shifted_letter = letters[letters.index(char) + shift] if choice == 'encode' else letters[letters.index(char) - shift]
            caesar_message += shifted_letter
        else:
            caesar_message += char
    print(f'Here is the {choice}d message: {caesar_message}')

print(logo)

while(choice):
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt > ").lower()
    if choice == 'encode' or choice == 'decode':
        message = input('Type your message > ').lower()
        shift = int(input('Type the shift number > '))
        caesar_cipher(message, shift, choice)
        try_again = input("Try again? Type 'yes' or 'no' > ").lower()
        if try_again != 'yes':
            break
    else:
        break
