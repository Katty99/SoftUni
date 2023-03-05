import re

text = input()
pattern = r'(\:\:|\*\*)([A-Z][a-z]{2,})\1'
matches = re.finditer(pattern, text)
emojis = []
total_points = 1
for current in matches:
    emojis.append(current.group(0))

numbers_pattern = r'[0-9]'
matched_numbers = re.finditer(numbers_pattern, text)
for num in matched_numbers:
    total_points *= int(num.group(0))

cool_emojis = []
print(f"Cool threshold: {total_points}")
cool_emojis_count = 0
for current_emoji in emojis:
    cool_emojis_count += 1
    cool_points = 0
    for char in current_emoji:
        if char.isalpha():
            cool_points += ord(char)
        else:
            continue
    if cool_points > total_points:
        cool_emojis.append(current_emoji)
print(f"{cool_emojis_count} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)