def game(heap, moves, to):
    if heap >= 100:
        return moves % 2 == to % 2
    if moves == to and game:
        return 0
    h = [game(heap + 2, moves + 1, to),
         game(heap + 4, moves + 1, to),]
    return any(h)

def game2(heap, moves, to):
    if heap >= 100:
        return moves % 2 == to % 2
    if moves == to and game:
        return 0
    h = [game2(heap + 2, moves + 1, to),
         game2(heap + 4, moves + 1, to),
         game2(heap * 2, moves + 1, to)]
    return any(h)
print("19-", min(s for s in range(1,100) if not game(s,0,1) and not game2(s,0,2)))