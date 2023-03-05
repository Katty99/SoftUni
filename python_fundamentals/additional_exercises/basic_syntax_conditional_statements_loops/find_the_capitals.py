word = input()
output_list = []
for index, letter in enumerate(word):
    if letter.isupper():
        output_list.append(index)
print(output_list)