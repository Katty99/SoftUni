def palindrome(word, first_index, last_index=-1):
    if first_index == len(word) // 2:
        return f"{word} is a palindrome"
    elif word[first_index] != word[last_index]:
        return f"{word} is not a palindrome"
    return palindrome(word, first_index + 1, last_index - 1)


print(palindrome("abba", 0))
