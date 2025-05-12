a=140*"8"
while "888" in a or "2222" in a :
    if "2222" in a:
        a=a.replace("2222", "88",)
    else:
        a=a.replace("888", "22",)
print(a)