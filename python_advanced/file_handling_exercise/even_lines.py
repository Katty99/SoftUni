symbols = ["-", ",", ".", "!", "?"]

with open('text.txt', 'w+') as text_file:  # This part of the code reads the input file
    while True:
        line = input()
        if line == '':
            break

        for current in line:
            if current in symbols:
                line = line.replace(current, '@')

        text_file.write(f"{line}\n")

with open('text.txt', 'r') as file:
    text = file.readlines()

    for row in range(0, len(text), 2):
        print(*text[row].split()[::-1], sep=' ')