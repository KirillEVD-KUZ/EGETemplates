text=open("ст3.txt").readline()
text=text.replace("B","*").replace("C","*").replace("D","*")
parts=text.split("*")
print(parts)
for part in parts:
    if part[0]=="A":
        part[]