def game1(heap1, heap2, moves, to):
    if heap1 + heap2 >= 82:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game1(heap1 + 1, heap2, moves + 1, to),
         game1(heap1 * 4, heap2, moves + 1, to),
         game1(heap1, heap2 + 1, moves + 1, to),
         game1(heap1, heap2 * 4, moves + 1, to)]
    return any(h)


def game2(heap1, heap2, moves, to):
    if heap1 + heap2 >= 82:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game2(heap1 + 1, heap2, moves + 1, to),
         game2(heap1 * 4, heap2, moves + 1, to),
         game2(heap1, heap2 + 1, moves + 1, to),
         game2(heap1, heap2 * 4, moves + 1, to)]
    return any(h) if (moves-1) %2==to%2 else all(h)

print("19-", min(s for s in range(1,78) if not game1(4, s,0,1) and game1(4, s, 0,2)))
print("20-",[s for s in range(1,78) if not game2(4,s,0,1) and not game2(4,s,0,2) and game2(4,s,0,3)])
print("21 -",[s for s in range(1,78) if game2(4,s,0,2 ) or game2(4,s,0,4)])

