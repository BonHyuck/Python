'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''
import sys

sys.setrecursionlimit(100000)


def find_path(r, c):
    for k in range(4):
        if 0 <= r + dr[k] < N and 0 <= c + dc[k] < N:
            if visited[r + dr[k]][c + dc[k]] == 0 and box[r + dr[k]][c + dc[k]] > rain:
                visited[r + dr[k]][c + dc[k]] = 1
                find_path(r + dr[k], c + dc[k])


# 박스 크기
N = int(input())
# N x N 박스 만들기
box = [list(map(int, input().split())) for _ in range(N)]
max_height = 0
for row in box:
    if max(row) > max_height:
        max_height = max(row)

# 연결여부 확인용
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 1

for rain in range(1, max_height):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    safe_zone = 0
    for i in range(N):
        for j in range(N):
            if box[i][j] > rain and visited[i][j] == 0:
                safe_zone += 1
                visited[i][j] = 1
                find_path(i, j)
    if safe_zone > result:
        result = safe_zone

print(result)



