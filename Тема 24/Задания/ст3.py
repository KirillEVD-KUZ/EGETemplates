text=open("ст3.txt").readline()

while 'AA' in text:
    text = text.replace('AA', 'A')
text=text.replace("B","*").replace("C","*").replace("D","*").replace('--', '-*-').replace('++', '+*+').replace('+-', '+*-').replace('-+', '-*+')
parts=text.split("*")
target_parts = []
for part in parts:
    if len(part) > 0 and part[0]=="A":
        parts_2 = part.split("A")
        for p in parts_2:
            if len(p) > 2 and p[0] != '+':
                target_parts.append(p)
print(max(target_parts, key=len))
print(eval(max(target_parts, key=len)))
