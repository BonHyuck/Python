'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

'''
import sys
sys.setrecursionlimit(1000000000)

def find_air(r, c):
    box[r][c] = -1
    for k in range(4):
        if 0 <= r+dr[k] < N and 0 <= c+dc[k] < M:
            if box[r+dr[k]][c+dc[k]] == 0:
                find_air(r+dr[k], c+dc[k])
            elif box[r+dr[k]][c+dc[k]] >= 1:
                box[r + dr[k]][c + dc[k]] += 1
    return


def check_cheese():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] > 2:
                cnt += 1
                box[i][j] = 0
            elif box[i][j] <= 0:
                box[i][j] = 0
            else:
                box[i][j] = 1
    return cnt == 0

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 0

while True:
    find_air(0, 0)
    if check_cheese():
        break
    result += 1

print(result)


