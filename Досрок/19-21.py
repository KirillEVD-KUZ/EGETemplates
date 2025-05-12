def game(heap, moves, to):
    if heap <= 87:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap - 2, moves + 1, to),
         game(heap // 2, moves + 1, to)]
    return any(h)


def game1(heap, moves, to):
    if heap <= 87:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game1(heap - 2, moves + 1, to),
         game1(heap // 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

print("19-",min(s for s in range(89,300) if not game(s,0,1) and game(s,0,2)))
print("20-",[s for s in range(88,300) if not game1(s,0,1) and game1(s,0,3)])
print("21-", [s for s in range(88,300) if not game1(s,0,2) and game1(s,0,4)])