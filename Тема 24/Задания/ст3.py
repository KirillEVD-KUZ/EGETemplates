text=open("ст3.txt").readline()
while "AA" in text:
    text=text.replace("AA","A")
text=text.replace("B","*").replace("C","*").replace("D","*")
parts=text.split("*")
target_part=[]
for part in parts:
    if len(part)>0 and part[0]=="AA":
        part_2=part.split("A")
        for p in part_2:
            if len(p)>0:
                target_part.append(p)
print(max(target_part,key=len))
