
q="111112211111222111122"
while "111" in q or "22" in q:
    q = q.replace("111", "2", 1)
    q = q.replace("222", "1", 1)
    q = q.replace("221", "1", 1)
    q = q.replace("122", "1", 1)
    q = q.replace("22", "2", 1)
print(q)
