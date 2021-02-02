'''
3 3
1 1 0
1 1 1
1 0 1
1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''

# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
# def check_path(row, col, direction):
#     global result
#     if box[row][col] == 0:
#         box[row][col] = 2
#         result += 1
#
#     # 4방향 모두 확인
#     four_dir = 0
#     for k in range(4):
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         if box[new_r][new_c] != 0:
#             four_dir += 1
#     # 4 방향 모두 청소가 돼있거나 벽
#     if four_dir == 4:
#         back_d = (direction + 2) % 4
#         back_r = row + dr[back_d]
#         back_c = col + dc[back_d]
#         # 뒤가 벽
#         if box[back_r][back_c] == 1:
#             return
#         else:
#             check_path(back_r, back_c, direction)
#
#     # 왼쪽의 인덱스
#     left_d = (direction + 3) % 4
#     left_r = row + dr[left_d]
#     left_c = col + dc[left_d]
#
#     # 아직 청소 안함
#     if box[left_r][left_c] == 0:
#         check_path(left_r, left_c, left_d)
#     # 회전만 함
#     else:
#         check_path(row, col, left_d)
#
#     return
#
#
#
#
# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(N)]
# result = 0
# check_path(r, c, d)
# print(result)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
result = 0
queue = [(r, c, d)]
while queue:
    row, col, direction = queue.pop(0)
    if box[row][col] == 0:
        box[row][col] = 2
        result += 1

    # 4방향 모두 확인
    four_dir = 0
    for k in range(4):
        new_r = row + dr[k]
        new_c = col + dc[k]
        if box[new_r][new_c] != 0:
            four_dir += 1
    # 4 방향 모두 청소가 돼있거나 벽
    if four_dir == 4:
        back_d = (direction + 2) % 4
        back_r = row + dr[back_d]
        back_c = col + dc[back_d]
        # 뒤가 벽
        if box[back_r][back_c] == 1:
            break
        else:
            queue.append((back_r, back_c, direction))
            continue

    # 왼쪽의 인덱스
    left_d = (direction + 3) % 4
    left_r = row + dr[left_d]
    left_c = col + dc[left_d]

    # 아직 청소 안함
    if box[left_r][left_c] == 0:
        queue.append((left_r, left_c, left_d))
    # 회전만 함
    else:
        queue.append((row, col, left_d))


print(result)


