def game(heap, moves, to):
    if heap <= 15:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h=[]
    while len(h)==0:
        for i in range(2, 10):
            if heap % i == 0:
                h.append(game(heap - i, moves + 1, to))
        heap-=1
    return any(h)
print("19-",min(s for s in range(16,1000) if not game(s,0,1) and game(s,0,2)))
print("20-",[s for s in range(16,1000) if not game(s,0,1) and not game(s,0,2) and game(s,0,3)])