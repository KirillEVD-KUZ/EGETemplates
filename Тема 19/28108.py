def game(heap, moves, to):
    if heap > 30:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap + 1, moves + 1, to),
         game(heap* 3 -2, moves + 1, to)]
    return any(h)


print( min(s for s in range(1, 30) if not game(s, 0, 1) and game(s, 0, 2)))
