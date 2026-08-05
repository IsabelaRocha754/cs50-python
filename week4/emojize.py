import emoji

input = input('Input: ')
output = emoji.emojize(input, language='alias')

print(f"Output: {output}")
