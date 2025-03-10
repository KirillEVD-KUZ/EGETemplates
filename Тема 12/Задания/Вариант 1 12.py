a=102 * "9"
while "33333" in a or "999" in a :
    if "33333" in a:
        a=a.replace("33333", "99", 1)
    if "999" in a:
        a=a.replace("999", "3", 1)
print(a)