'''
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8

'''







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
