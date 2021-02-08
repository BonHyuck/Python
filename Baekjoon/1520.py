'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
#
# def find_path(row, col):
#     global result
#
#     if row == M-1 and col == N-1:
#         result += 1
#         return
#
#     for k in range(4):
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         if 0 <= new_r < M and 0 <= new_c < N:
#             if box[new_r][new_c] < box[row][col] and visited[new_r][new_c] == 0:
#                 visited[new_r][new_c] = 1
#                 find_path(new_r, new_c)
#                 visited[new_r][new_c] = 0
#
#     return
#
# M, N = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(M)]
# visited = [[0 for _ in range(N)] for _ in range(M)]
# visited[0][0] = 1
# result = 0
# find_path(0, 0)
# print(result)

#
# # 우하좌상 순서대로 탐색
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# M, N = map(int, input().split())
#
# box = [list(map(int, input().split())) for _ in range(M)]
# visited = [[0 for _ in range(N)] for _ in range(M)]
# visited[0][0] = 1
# queue = [(0, 0)]
# while queue:
#     row, col = queue.pop(0)
#     for k in range(4):
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         if 0 <= new_r < M and 0 <= new_c < N:
#             if box[new_r][new_c] < box[row][col]:
#                 visited[new_r][new_c] = visited[new_r][new_c] + 1
#                 queue.append((new_r, new_c))
#
# print(visited[M-1][N-1])
#
# import sys
# sys.setrecursionlimit(1000000000)
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# def find_path(row, col):
#     if row == 0 and col == 0:
#         return 1
#
#     mid_result = 0
#     for k in range(4):
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         if 0 <= new_r < M and 0 <= new_c < N:
#             if box[new_r][new_c] > box[row][col]:
#                 mid_result += find_path(new_r, new_c)
#
#     return mid_result
#
# M, N = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(M)]
# result = find_path(M-1, N-1)
# print(result)

'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''

# import sys
# sys.setrecursionlimit(1000000)
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# def find_path(row, col):
#     global result
#
#     if row == M-1 and col == N-1:
#         result += 1
#         return
#
#     for k in range(4):
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         if 0 <= new_r < M and 0 <= new_c < N:
#             if box[new_r][new_c] < box[row][col]:
#                 find_path(new_r, new_c)
#
#     return
#
# M, N = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(M)]
# visited = [[0 for _ in range(N)] for _ in range(M)]
# visited[0][0] = 1
# result = 0
# find_path(0, 0)
# print(result)



import sys
sys.setrecursionlimit(1000000000)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find_path(row, col):
    # 끝까지 갔다가 돌아오는 형식이기때문에
    # 끝에서 1을 리턴해서 합산식 구성
    if row == M-1 and col == N-1:
        return 1
    # 이미 가본 곳은 돌아보지 않는다.
    if visited[row][col] > -1:
        return visited[row][col]
    # 위에 걸리지 않으면 기본값으로 체크, 0 = 확인 시작
    visited[row][col] = 0

    # 4방향으로 확인
    for k in range(4):
        new_r = row + dr[k]
        new_c = col + dc[k]
        if 0 <= new_r < M and 0 <= new_c < N:
            if box[new_r][new_c] < box[row][col]:
                # 현재 값 = 원래 있던 값 + 끝까지 가서 끌어온 값
                visited[row][col] += find_path(new_r, new_c)

    # 배열의 해당 행열 값 리턴
    return visited[row][col]

# 입력값 받기
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
# 못 가는 것( = 0)과 안 가본 것( = -1)은 다름
visited = [[-1 for _ in range(N)] for _ in range(M)]
find_path(0, 0)
print(visited[0][0])