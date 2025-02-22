from itertools import product

text = open('47228.txt').read()
gl = 'AO'
sogl = 'CDF'
for pair in product(sogl, gl):
    pair = ''.join(pair)
    text = text.replace(pair, '*')
for c in gl + sogl:
    text = text.replace(c, ' ')
print(len(max(text.split(), key=len)))
