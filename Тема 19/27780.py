def game(heap1, heap2, moves, to):
    if heap1 + heap2 >= 74:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap1 + 1, heap2, moves + 1, to),
         game(heap1 * 2, heap2, moves + 1, to),
         game(heap1, heap2 + 1, moves + 1, to),
         game(heap1, heap2 * 2, moves + 1, to)]
    return any(h)


def game2(heap1, heap2, moves, to):
    if heap1 + heap2 >= 74:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game2(heap1 + 1, heap2, moves + 1, to),
         game2(heap1 * 2, heap2, moves + 1, to),
         game2(heap1, heap2 + 1, moves + 1, to),
         game2(heap1, heap2 * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print("19 - ", min(s for s in range(1, 74) if not game(12, s, 0, 1) and game(12, s, 0, 2)))
print("20-",[s for s in range(1,101) if not game2(5,s,0,1 ) and   game2(5,s,0,3)])
print("20 - ", [s for s in range(1, 74) if not game2(12, s, 0, 1) and game2(12, s, 0, 3)])
print("21 - ", [s for s in range (1,74) if game2(12,s,0,2) or game2(12,s,0,4)])