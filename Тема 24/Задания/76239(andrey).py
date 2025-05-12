text = open("76239.txt").read()
pairs = ['++', '--', '-+', '+-']
for pair in pairs:
    text = text.replace(pair, f'{pair[0]} {pair[1]}')
text = (text.replace('-06', '-0 6').
        replace('+06', '+0 6').replace('+07', '+0 7').replace('-07', '-0 7').
        replace('-08', '-0 8').replace('+08', '+0 8').replace('+09', '+0 9').
        replace('-09', '-0 9'))
parts = [p.strip('+-').lstrip('0') for p in text.split()]
expr = []
for part in parts:
    if len(part) > 0:
        expr.append(part)
print(expr)
print(max(expr, key=len))
print(len(max(expr, key=len)))
