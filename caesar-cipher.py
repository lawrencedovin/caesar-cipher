letters = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]

message = input('what is your message?: ')
shift = int(input('how much do you want to shift the letters?: '))

def caesar_encode(message, shift):
    caesar_message = ''
    for char in message:
        if char == ' ':
            caesar_message += char
        if char in letters:
            shifted_letter = letters[letters.index(char)+shift]
            caesar_message += shifted_letter
    print(caesar_message)

caesar_encode(message, shift)
