# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def find_gold(row, col):
#     global max_dist
#     cnt = 0
#     visited = [[0 for _ in range(C)] for _ in range(R)]
#     lands = [[[row, col]]]
#     visited[row][col] = 1
#     while lands:
#         cnt += 1
#         next_land = []
#         now_land = lands.pop(0)
#         for l in now_land:
#             for k in range(4):
#                 r = l[0] + dx[k]
#                 c = l[1] + dy[k]
#                 if 0 <= r < R and 0 <= c < C:
#                     if box[r][c] == 'L' and visited[r][c] == 0:
#                         visited[r][c] = 1
#                         next_land.append([r, c])
#         if len(next_land) > 0:
#             lands.append(next_land)
#         else:
#             break
#
#     if max_dist < cnt - 1:
#         max_dist = cnt - 1
#     return
#
#
# R, C = map(int, input().split())
# box = [list(input()) for _ in range(R)]
# max_dist = 0
# for i in range(R):
#     for j in range(C):
#         if box[i][j] == 'L':
#             find_gold(i, j)
#
# print(max_dist)

'''
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_gold(row, col):
    global max_dist
    visited = [[0 for _ in range(C)] for _ in range(R)]
    lands = [[row, col]]
    visited[row][col] = 1
    while lands:
        l = lands.pop(0)
        for k in range(4):
            r = l[0] + dx[k]
            c = l[1] + dy[k]
            if 0 <= r < R and 0 <= c < C:
                if box[r][c] == 'L' and visited[r][c] == 0:
                    visited[r][c] = visited[l[0]][l[1]] + 1
                    lands.append([r, c])
                    if visited[r][c] > max_dist:
                        max_dist = visited[r][c]
    return


R, C = map(int, input().split())
box = [list(input()) for _ in range(R)]
max_dist = 0
for i in range(R):
    for j in range(C):
        if box[i][j] == 'L':
            find_gold(i, j)

print(max_dist-1)
