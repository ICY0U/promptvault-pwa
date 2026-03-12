with open('index.html', 'rb') as f:
    data = f.read()

# The bytes \xc3\xa2\xe2\x82\xac\xe2\x80\x9d = â€" (triple-encoded em dash)
# The bytes \xc3\xa2\xe2\x82\xac\xe2\x80\x9c = â€" variant
# The bytes \xc3\xa2\xe2\x82\xac\xe2\x84\xa2 = â€™ (right single quote)
# Also handle cliché -> cliché  (Ã© -> é)
replacements = {
    b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d': b' \xe2\x80\x94 ',  # em dash with spaces
    b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9c': b' \xe2\x80\x94 ',
    b'\xc3\xa2\xe2\x82\xac\xe2\x84\xa2': b'\xe2\x80\x99',  # right single quote
    b'\xc3\xa2\xe2\x82\xac\xe2\x80\x93': b'\xe2\x80\x94',  # another em dash variant
    b'\xc3\x83\xc2\xa9': b'\xc3\xa9',  # é double-encoded
}

count = 0
for bad, good in replacements.items():
    c = data.count(bad)
    count += c
    data = data.replace(bad, good)

with open('index.html', 'wb') as f:
    f.write(data)

print(f'Fixed {count} mojibake occurrences')
