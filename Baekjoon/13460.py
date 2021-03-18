N, M = map(int, input().split())
box = [list(input()) for _ in range(N)]
red = (0, 0)
blue = (0, 0)
hole = (0, 0)
for r in range(N):
    for c in range(M):
        if box[r][c] == 'R':
            red = (r, c)
        elif box[r][c] == 'B':
            blue = (r, c)
        elif box[r][c] == 'O':
            hole = (r, c)
result = 11
