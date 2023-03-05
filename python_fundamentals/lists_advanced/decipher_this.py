message = input().split()
deciphered_message = []
for current_word in message:
    number_in_word = [x for x in current_word if x.isdigit()]
    num_str = ''.join(number_in_word)
    number = int(num_str)
    num_to_chr = current_word.replace(num_str, chr(number))
    word_to_list = list(num_to_chr)
    word_to_list[1], word_to_list[-1] = word_to_list[-1], word_to_list[1]
    deciphered_message.append(''.join(word_to_list))
print(*deciphered_message)