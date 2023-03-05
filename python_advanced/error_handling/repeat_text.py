try:
    word = input()
    repeat = int(input())
    print(word * repeat)

except ValueError:
    print('Variable times must be an integer')