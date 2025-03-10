def game1(heap, moves, to):
    if heap >= 38:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h=[game1(heap +1, moves+1, to),
       game1(heap * 2, moves+1,to)]
    return any(h)
print("19-", min(s for s in range(1,38) if not game1(s,0,1) and game1(s,0,2)))
print("20-", [s for s in range(1,38) if not game1(s,0,1) and not game1(s, 0, 2)and game1(s,0,3)])
print("21-", [s for s in range(1,38) if game1(s,0,2) or game1(s,0,4)])