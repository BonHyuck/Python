'''
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8

5
14 9 12 10 5
1 11 5 4 11
7 15 2 13 50
6 3 16 8 300
123 54 123 214 333

6
14 9 12 10 5 9
1 11 5 4 11 100
7 15 2 13 50 70
6 3 16 8 300 1237
123 54 123 47 29 3
11 22 33 44 55 66

'''

import sys
sys.setrecursionlimit(1000000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check_panda(row, col):
    # visited가 0일때 시작이니까 1로 세팅해주기
    visited[row][col] = 1
    # 근처에 접근 가능한 밭
    nearby = []
    for k in range(4):
        new_r = row + dr[k]
        new_c = col + dc[k]
        # 인덱스 검사
        if 0 <= new_r < N and 0 <= new_c < N:
            # 다음 박스로 이동 가능
            if box[row][col] < box[new_r][new_c]:
                if visited[new_r][new_c] == 0:
                    # 깊이 들어가자
                    check_panda(new_r, new_c)
                nearby.append(visited[new_r][new_c])
    if nearby:
        visited[row][col] = max(nearby) + 1
    else:
        visited[row][col] = 1

# N x N 대나무 숲의 크기
N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]
# 아예 아무것도 없이 시작해보자
visited = [[0 for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        # 방문 안 한 곳만 찾는건 맞는듯
        if visited[r][c] == 0:
            check_panda(r, c)
result = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] > result:
            result = visited[r][c]
print(result)

# import sys
# sys.setrecursionlimit(1000000)
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def check_panda(row, col, days):
#     # 아직 방문을 안 했다면 (visited = 0) 시작점으로 세팅
#     if visited[row][col] == 0:
#         visited[row][col] = days
#     for k in range(4):
#         # 상하좌우 검사
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         # 인덱스 검사
#         if 0 <= new_r < N and 0 <= new_c < N:
#             # 다음 대나무 밭으로 이동 가능한가?
#             if box[row][col] < box[new_r][new_c]:
#                 # 가능하다면
#                 if visited[new_r][new_c] <= days + 1:
#                     visited[new_r][new_c] = days + 1
#                     check_panda(new_r, new_c, days + 1)
#
#     return
#
#
# # N x N 대나무 숲의 크기
# N = int(input())
# box = [list(map(int, input().split())) for _ in range(N)]
# # 아예 아무것도 없이 시작해보자
# visited = [[0 for _ in range(N)] for _ in range(N)]
# cnt = 0
# result = 1
# # 모든 지점을 검사한다.
# for r in range(N):
#     for c in range(N):
#         # 더 깊이 들어가지말고 아직 방문 안한곳만??
#         if visited[r][c] == 0:
#             check_panda(r, c, 1)
#
#
# for r in range(N):
#     for c in range(N):
#         if result < visited[r][c]:
#             result = visited[r][c]
#
# print(result)

#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def check_panda(row, col):
#     queue = [(row, col)]
#     while queue:
#         r, c = queue.pop(0)
#         for k in range(4):
#             new_r = r + dr[k]
#             new_c = c + dc[k]
#             # 인덱스 확인
#             if 0 <= new_r < N and 0 <= new_c < N:
#                 if box[r][c] < box[new_r][new_c] and visited[new_r][new_c] <= visited[r][c]:
#                     visited[new_r][new_c] = visited[r][c] + 1
#                     queue.append((new_r, new_c))
#
# # N x N 대나무 숲의 크기
# N = int(input())
# box = [list(map(int, input().split())) for _ in range(N)]
# visited = [[1 for _ in range(N)] for _ in range(N)]
#
# # 모든 지점을 검사한다.
# for r in range(N):
#     for c in range(N):
#         check_panda(r, c)
#
# result = 1
# for r in range(N):
#     for c in range(N):
#         if visited[r][c] > result:
#             result = visited[r][c]
#
# print(result)






# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def get_end_points():
#     for r in range(N):
#         for c in range(N):
#             end = True
#             for k in range(4):
#                 if 0 <= r + dr[k] < N and 0 <= c + dc[k] < N:
#                     if box[r][c] < box[r + dr[k]][c + dc[k]]:
#                         end = False
#                         break
#             if end:
#                 end_points.append((r, c))
#     return
#
#
# def check_panda(row, col, days):
#     global result
#     if result < days:
#         result = days
#
#     for k in range(4):
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         if 0 <= new_r < N and 0 <= new_c < N:
#             if box[row][col] > box[new_r][new_c] and visited[new_r][new_c] == 0:
#                 visited[new_r][new_c] = 1
#                 check_panda(new_r, new_c, days + 1)
#
#     return
#
#
# # N x N 대나무 숲의 크기
# N = int(input())
# box = [list(map(int, input().split())) for _ in range(N)]
# end_points = []
# get_end_points()
#
# result = 1
#
# while end_points:
#     r, c = end_points.pop(0)
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     visited[r][c] = 1
#     check_panda(r, c, 1)
#
# print(result)

#
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def check_panda(row, col):
#     queue = [(row, col)]
#
#     while queue:
#         r, c = queue.pop(0)
#         for k in range(4):
#             new_r = r + dr[k]
#             new_c = c + dc[k]
#             # 인덱스 확인
#             if 0 <= new_r < N and 0 <= new_c < N:
#                 if box[r][c] < box[new_r][new_c] and visited[new_r][new_c] <= visited[r][c]:
#                     visited[new_r][new_c] = visited[r][c] + 1
#                     queue.append((new_r, new_c))
#
#
# # N x N 대나무 숲의 크기
# N = int(input())
# box = [list(map(int, input().split())) for _ in range(N)]
# visited = [[1 for _ in range(N)] for _ in range(N)]
#
# for r in range(N):
#     for c in range(N):
#         check_panda(r, c)
#
# result = 1
# for r in range(N):
#     for c in range(N):
#         if visited[r][c] > result:
#             result = visited[r][c]
#
# print(result)

#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # row : 현재 행, col : 현재 열, days : 생존 일 수
# def check_panda(row, col, days):
#     global result
#
#     for k in range(4):
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         # 인덱스 검사
#         if 0 <= new_r < N and 0 <= new_c < N:
#             # 개수 검사
#             # 전에 먹은거보다 많아야 됨
#             if box[row][col] < box[new_r][new_c]:
#                 # 이제 먹을 수 있음
#                 check_panda(new_r, new_c, days + 1)
#
#     if result < days:
#         result = days
#
#     return
#
# # N x N 대나무 숲의 크기
# N = int(input())
# box = [list(map(int, input().split())) for _ in range(N)]
# result = 0
#
# # 모든 시작점 전부 검사
# for r in range(N):
#     for c in range(N):
#         check_panda(r, c, 1)
#
# print(result)
