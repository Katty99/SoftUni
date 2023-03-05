import re

links = input()
pattern = r'(www\.([A-Za-z0-9\-]+)(\.[a-z]+)+)'
valid_urls = []
while links:
    matched = re.search(pattern, links)
    if matched:
        valid_urls.append(matched.group(0))
    links = input()
for valid in valid_urls:
    print(valid)
