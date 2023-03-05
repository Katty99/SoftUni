import re

words = input()
words_list = []
pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})'
matches = re.findall(pattern, words)
valid_pairs_found = 0
pairs_dictionary = {}
for current_match in matches:
    valid_pairs_found += 1
    words_list.append(current_match[1])
    words_list.append(current_match[2])
for x in range(0, len(words_list), 2):
    reversed_word = words_list[x + 1][::-1]
    if words_list[x] == reversed_word:
        pairs_dictionary[words_list[x]] = words_list[x + 1]

if valid_pairs_found > 0:
    print(f"{valid_pairs_found} word pairs found!")
    if pairs_dictionary:
        print("The mirror words are:")
        dict_to_print = ", ".join(" <=> ".join([key, value]) for key, value in pairs_dictionary.items())
        print(dict_to_print)
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")