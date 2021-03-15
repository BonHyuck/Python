'''
16
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

'''

# dx = [-1, 0]
# dy = [0, -1]
#
#
# # 행, 열, 방향(1: 가로, 2: 세로, 3: 대각
# def find_pipe(row, col, dir):
#     global result
#     # 현재 가로
#     if dir == 1:
#         # 가로로 이동
#         next_row = row
#         next_col = col + 1
#         # 인덱스 확인
#         if 0 <= next_row <= N and 0 <= next_col <= N:
#             # 끝에 도달
#             if next_row == N and next_col == N:
#                 result += 1
#                 return
#             # 다음 파이프 확인
#             if box[next_row][next_col] == 0:
#                 find_pipe(next_row, next_col, 1)
#         # 대각선 이동
#         next_row = row + 1
#         next_col = col + 1
#         # 인덱스 확인
#         if 0 <= next_row <= N and 0 <= next_col <= N:
#             # 끝에 도달
#             if next_row == N and next_col == N:
#                 result += 1
#                 return
#             # 다음 파이프 확인
#             if box[next_row][next_col] == 0:
#                 checkbox = True
#                 for k in range(2):
#                     check_row = next_row + dx[k]
#                     check_col = next_col + dy[k]
#                     if not (0 <= check_row <= N and 0 <= check_col <= N and box[check_row][check_col] == 0):
#                         checkbox = False
#                         break
#                 if checkbox:
#                     find_pipe(next_row, next_col, 3)
#     elif dir == 2:
#         # 세로로 이동
#         next_row = row + 1
#         next_col = col
#         # 인덱스 확인
#         if 0 <= next_row <= N and 0 <= next_col <= N:
#             # 끝에 도달
#             if next_row == N and next_col == N:
#                 result += 1
#                 return
#             # 다음 파이프 확인
#             if box[next_row][next_col] == 0:
#                 find_pipe(next_row, next_col, 2)
#         # 대각선 이동
#         next_row = row + 1
#         next_col = col + 1
#         # 인덱스 확인
#         if 0 <= next_row <= N and 0 <= next_col <= N:
#             # 끝에 도달
#             if next_row == N and next_col == N:
#                 result += 1
#                 return
#                 # 다음 파이프 확인
#             if box[next_row][next_col] == 0:
#                 checkbox = True
#                 for k in range(2):
#                     check_row = next_row + dx[k]
#                     check_col = next_col + dy[k]
#                     if not (0 <= check_row <= N and 0 <= check_col <= N and box[check_row][check_col] == 0):
#                         checkbox = False
#                         break
#                 if checkbox:
#                     find_pipe(next_row, next_col, 3)
#     elif dir == 3:
#         # 가로로 이동
#         next_row = row
#         next_col = col + 1
#         # 인덱스 확인
#         if 0 <= next_row <= N and 0 <= next_col <= N:
#             # 끝에 도달
#             if next_row == N and next_col == N:
#                 result += 1
#                 return
#             # 다음 파이프 확인
#             if box[next_row][next_col] == 0:
#                 find_pipe(next_row, next_col, 1)
#         # 세로로 이동
#         next_row = row + 1
#         next_col = col
#         # 인덱스 확인
#         if 0 <= next_row <= N and 0 <= next_col <= N:
#             # 끝에 도달
#             if next_row == N and next_col == N:
#                 result += 1
#                 return
#             # 다음 파이프 확인
#             if box[next_row][next_col] == 0:
#                 find_pipe(next_row, next_col, 2)
#         # 대각선 이동
#         next_row = row + 1
#         next_col = col + 1
#         # 인덱스 확인
#         if 0 <= next_row <= N and 0 <= next_col <= N:
#             # 끝에 도달
#             if next_row == N and next_col == N:
#                 result += 1
#                 return
#             # 다음 파이프 확인
#             if box[next_row][next_col] == 0:
#                 checkbox = True
#                 for k in range(2):
#                     check_row = next_row + dx[k]
#                     check_col = next_col + dy[k]
#                     if not (0 <= check_row <= N and 0 <= check_col <= N and box[check_row][check_col] == 0):
#                         checkbox = False
#                         break
#                 if checkbox:
#                     find_pipe(next_row, next_col, 3)
#
# N = int(input())
# box = [list(map(int, input().split())) for _ in range(N)]
# # 인덱스 맞춰주기
# N -= 1
# # 시작 파이프 놓기
# box[0][0] = 2
# box[0][1] = 2
# # (N, N)에 도달하는 경우의 수
# result = 0
# # 길찾기 시작
# find_pipe(0, 1, 1)
#
# print(result)


N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
# 인덱스 맞춰주기
N -= 1
# 시작 파이프 놓기
box[0][0] = 2
box[0][1] = 2
visited[0][0] = 1
visited[0][1] = 1

