def game(heap1, heap2, moves, to):
    if heap1 + heap2 >= 65:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    else:
        h = [game(heap1 + 1, heap2, moves + 1, to),
             game(heap1 * 3, heap2, moves + 1, to),
             game(heap1, heap2 + 1, moves + 1, to),
             game(heap1, heap2 * 3, moves + 1, to)]
    return any(h)


def game2(heap1, heap2, moves, to):
    if heap1 + heap2 >= 65:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    else:
        h = [game2(heap1 + 1, heap2, moves + 1, to),
             game2(heap1 * 3, heap2, moves + 1, to),
             game2(heap1, heap2 + 1, moves + 1, to),
             game2(heap1, heap2 * 3, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print("19-", min(s for s in range(1, 65) if not game(s, 6, 0, 1) and game(s, 6, 0, 2)))
print("20-", [s for s in range(1, 65) if not game2(s, 6, 0, 1) and not game2(s, 6, 0, 2) and game2(s, 6, 0, 3)])
print("21-", [s for s in range(1, 65) if not game2(s,6,0,2) and game2(s,6,0,4)])

