from string import punctuation

with open('text.txt', 'r') as text_file:
    with open('output.txt', 'w') as output_file:
        line_number = 1
        text = text_file.readlines()

        for current in text:
            characters_count = 0
            symbols_count = 0

            for char in current:
                if char.isalpha():
                    characters_count += 1

                elif char in punctuation:
                    symbols_count += 1

            output_file.write(f"Line {line_number}: {''.join(current[:-1])} ({characters_count})({symbols_count})\n")
            line_number += 1
