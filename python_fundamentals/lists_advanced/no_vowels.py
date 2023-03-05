word = input()
vowels_list = ['a', 'o', 'u', 'e', 'i']
output = [letter for letter in word if letter.lower() not in vowels_list]
print(''.join(output))