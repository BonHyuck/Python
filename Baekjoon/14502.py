'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

'''
from itertools import combinations
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_safe():
    for v in virus:
        queue = [v]
        while queue:
            r, c = queue.pop(0)
            for k in range(4):
                new_r = r + dx[k]
                new_c = c + dy[k]
                # 인덱스 확인
                if 0 <= new_r < N and 0 <= new_c < M:
                    if new_box[new_r][new_c] == 0:
                        new_box[new_r][new_c] = 2
                        queue.append((new_r, new_c))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_box[i][j] == 0:
                cnt += 1

    return cnt


# N, M = 세로, 가로
N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
# 벽을 세울 수 있는 빈칸
possible = []
# 바이러스
virus = []
for r in range(N):
    for c in range(M):
        if box[r][c] == 0:
            possible.append((r, c))
        elif box[r][c] == 2:
            virus.append((r, c))

combs = list(combinations(possible, 3))
result = 0
for comb in combs:
    # 전체 배열 가져오기
    new_box = deepcopy(box)
    # 벽 세우기
    for r, c in comb:
        new_box[r][c] = 1
    result = max(result, find_safe())


print(result)