import re

line = input()
pattern = r'\d+'

while line:
    match = re.findall(pattern, line)
    if match:
        print(' '.join(match), end=' ')
    line = input()


