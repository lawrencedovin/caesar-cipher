letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
print(letters[0])

message = list(input('what is your message?: '))
shift = int(input('how much do you want to shift the letters?: '))

# def caesar_encode(message, shift):
#     new_message = []
#     for i, char in enumerate(message):
#         for j, letter in enumerate(letters):
#             if char[i] == letter[j]:
#                 char[i] = letter[j+shift]
#                 new_message.append(char[i])
#     print(new_message)

print(message)
caesar_encode(message, shift)
