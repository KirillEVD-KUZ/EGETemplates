"""
Текстовый файл состоит из символов, обозначающих заглавные буквы латинского алфавита. Определите минимальное количество
идущих подряд символов, среди которых пара символов T встречается ровно 150 раз.
"""
text = open('1_24.txt').readline()
parts = text.split('TT')
min_len = len(text)
for i in range(len(parts) - 149):
    min_len = min(min_len, len('**'.join(parts[i:i + 149])) + 4)
print(min_len)

