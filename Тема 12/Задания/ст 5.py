a="2"+140*"3"
while "2" in a :
    if "23" in a:
        a=a.replace("23", "3332",1)
    else:
        a=a.replace("2", "333",1)
sm=a.count("2")*2 +a.count("3")*3
print(sm)