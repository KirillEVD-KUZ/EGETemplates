def game(heap1,heap2,moves,to):
    if heap1+heap2<=150:
        return moves%2==to%2
    if moves==to:
        return 0
    h=[game(heap1-2,heap2,moves+1,to),
       game(heap1//3,heap2,moves+1,to),
       game(heap1,heap2-2,moves+1,to),
       game(heap1,heap2//3,moves+1,to)]
    return any(h)

def game1(heap1,heap2,moves,to):
    if heap1+heap2<=150:
        return moves%2==to%2
    if moves==to:
        return 0
    h=[game1(heap1-2,heap2,moves+1,to),
       game1(heap1//3,heap2,moves+1,to),
       game1(heap1,heap2-2,moves+1,to),
       game1(heap1,heap2//3,moves+1,to)]
    return any(h) if (moves-1)%2==to%2 else all(h)
print("19-", max(s for s in range(134,20000) if not game(17,s,0,1) and game(17,s,0,2)))
print("20-", [s for s in range(134,2000) if not game1(17,s,0,1) and game1(17,s,0,3)])
print("21-", [s for s in range(134,2000) if not game1(17,s,0,2) and game1(17,s,0,4)])