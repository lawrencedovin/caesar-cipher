letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]

message = input('what is your message?: ')
shift = int(input('how much do you want to shift the letters?: '))

def caesar_encode(message, shift):
    caesar_message = ''
    for char in message:
        if char == ' ':
            caesar_message += char
        if char in letters:
            caesar_message += (letters[letters.index(char)+shift])
    print(caesar_message)

caesar_encode(message, shift)
