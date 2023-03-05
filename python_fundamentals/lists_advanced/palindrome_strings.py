list_of_words = input().split(' ')
searched_palindrome = input()
palindrome_list = []
for current_word in list_of_words:
    if current_word == current_word[::-1]:
        palindrome_list.append(current_word)
searched_count = palindrome_list.count(searched_palindrome)
print(palindrome_list)
print(f"Found palindrome {searched_count} times")
