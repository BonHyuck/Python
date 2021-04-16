'''
1 1 1
1
1 1 1
'''

from _collections import deque

N, M, K = map(int, input().split())
# 겨울에 추가될 양분
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
# print(type(trees[0][0]))
foods = [[5 for _ in range(N)] for _ in range(N)]

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for k in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for r in range(N):
    for c in range(N):
        trees[r][c] = deque(sorted(trees[r][c]))

# K년 동안 반복
for _ in range(K):
    # 봄 + 여름
    for r in range(N):
        for c in range(N):
            food = foods[r][c]
            cnt = 0
            length = len(trees[r][c])
            while cnt < length:
                one_tree = trees[r][c].popleft()
                # 아직 양분이 있음
                if food > 0:
                    food -= one_tree
                    one_tree += 1

                    foods[r][c] = food
                    trees[r][c].append(one_tree)
                # 양분 다 씀
                else:
                    # 나무 죽음
                    foods[r][c] += one_tree // 2
                cnt += 1

    # 가을
    for r in range(N):
        for c in range(N):
            foods[r][c] += A[r][c]
            for k in range(len(trees[r][c])):
                if trees[r][c][k] % 5 == 0:
                    for i in range(8):
                        new_r = r + dr[i]
                        new_c = c + dc[i]
                        if 0 <= new_r < N and 0 <= new_c < N:
                            trees[r][c].appendleft(1)

result = 0
for r in range(N):
    for c in range(N):
        result += len(trees[r][c])

# print(trees)
print(result)



# from collections import deque
# from itertools import islice
#
# n, m, k = map(int, input().split())
# addfood = [list(map(int, input().split())) for _ in range(n)]
# trees = [[deque() for _ in range(n)] for _ in range(n)]
# foods = list([5] * n for _ in range(n))
#
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     trees[x-1][y-1].append(z)
#
# dr = [-1, -1, -1, 0, 0, 1, 1, 1]
# dc = [-1, 0, 1, -1, 1, -1, 0, 1]
#
# for _ in range(k):
#
#     for i in range(n):
#         for j in range(n):
#             for t in range(len(trees[i][j])):
#                 if trees[i][j][t] <= foods[i][j]:
#                     foods[i][j] -= trees[i][j][t]
#                     trees[i][j][t] += 1
#                 else:
#                     for k in range(t, len(trees[i][j])):
#                         foods[i][j] += trees[i][j][k] // 2
#                     trees[i][j] = deque(islice(trees[i][j], 0, t))
#                     break
#
#     for i in range(n):
#         for j in range(n):
#             for t in trees[i][j]:
#                 if t % 5 == 0:
#                     for d in range(8):
#                         nr, nc = i + dr[d], j + dc[d]
#                         if 0 <= nr < n and 0 <= nc < n:
#                             trees[nr][nc].appendleft(1)
#
#     for i in range(n):
#         for j in range(n):
#             foods[i][j] += addfood[i][j]
#
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if trees[i][j]:
#             cnt += len(trees[i][j])
#
# print(cnt)