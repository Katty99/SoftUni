def palindromes(digits):
    if digits == digits[::-1]:
        return True
    else:
        return False


numbers_list = input().split(', ')
for current_number in numbers_list:
    print(palindromes(current_number))
