text = open('59790.txt').read()
parts = text.split('T')
min_len = len(text)
for i in range(len(parts) - 209):
    min_len = min(min_len, len('*'.join(parts[i:i + 209])) + 2)
print(min_len)
