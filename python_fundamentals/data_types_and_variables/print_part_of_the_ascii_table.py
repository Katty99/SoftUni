start = int(input())
stop = int(input())
result = ''
for current_char in range(start, stop + 1):
    result += chr(current_char) + ' '
print(result)
