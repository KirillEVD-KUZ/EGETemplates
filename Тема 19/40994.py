def game(heap, moves, step, op):
    if heap >= 50:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    if op == 1:
        res = [game(heap + 2, moves + 1, step, 2), game(heap * 2, moves + 1, step, 3)]
    elif op == 2:
        res = [game(heap + 1, moves + 1, step, 1), game(heap * 2, moves + 1, step, 3)]
    elif op == 3:
        res = [game(heap + 1, moves + 1, step, 1), game(heap + 2, moves + 1, step, 2)]
    else:
        res = [game(heap + 1, moves + 1, step, 1), game(heap + 2, moves + 1, step, 2),
               game(heap * 2, moves + 1, step, 3)]
    return any(res) if ((moves + 1) % 2 == step % 2) else all(res)

print(min(s for s in range (1 , 50) if not game(s, 0, 1, 0) and game (s,0,2,0)))
print([s for s in range(1,34) if not game(s,0,1,0) and game(s,0,3,0)])
print([s for s in range(1,34) if game(s,0,4,0) and not game(s,0,2,0)])