'''
4 6 8
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4
3 3 1 2 7
1 5 8 4 3
3 6 2 1 2
2 2 2 3 5
'''

# 상하우좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# R : 행
# C : 열
# M : 상어 수
R, C, M = map(int, input().split())
box = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(M):
    # r : 상어 행
    # c : 상어 열
    # s : 상어 속도
    # d : 상어 이동 방향 1, 2, 3, 4 : 상하우좌 -> 0, 1, 2, 3 으로 변경
    # z : 상어 크기
    r, c, s, d, z = map(int, input().split())
    # -1은 인덱스에 맞추기 위해서
    box[r-1][c-1] = (s, d-1, z)

result = 0
# 낚시왕이 1칸씩 움직임
for index in range(C):
    # 제일 가까운 상어 잡기
    for i in range(R):
        if box[i][index] != 0:
            s, d, z = box[i][index]
            result += z
            box[i][index] = 0
            break
    # 상어 이동
    # 이동 결과를 담을 배열
    move_result = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            # 상어가 있음
            if box[r][c] != 0:
                speed, direction, size = box[r][c]
                # 왕복 없이 이동 구현
                if direction == 0 or direction == 1:
                    speed %= ((2 * R) - 2)
                elif direction == 2 or direction == 3:
                    speed %= ((2 * C) - 2)

                row = r
                col = c

                for _ in range(speed):
                    # 1. 위로
                    if direction == 0:
                        if row - 1 < 0 or row - 1 >= R:
                            direction = 1
                            row += 1
                        else:
                            row -= 1
                    # 2. 아래로
                    elif direction == 1:
                        if row + 1 < 0 or row + 1 >= R:
                            direction = 0
                            row -= 1
                        else:
                            row += 1
                    # 3. 오른쪽으로
                    elif direction == 2:
                        if col + 1 < 0 or col + 1 >= C:
                            direction = 3
                            col -= 1
                        else:
                            col += 1
                    # 4. 왼쪽으로
                    elif direction == 3:
                        if col - 1 < 0 or col - 1 >= C:
                            direction = 2
                            col += 1
                        else:
                            col -= 1

                if move_result[row][col] == 0 or size > move_result[row][col][2]:
                    move_result[row][col] = (speed, direction, size)

    box = move_result
    
print(result)



# # R : 행
# # C : 열
# # M : 상어 수
# R, C, M = map(int, input().split())
# box = [[0 for _ in range(C)] for _ in range(R)]
#
# for _ in range(M):
#     # r : 상어 행
#     # c : 상어 열
#     # s : 상어 속도
#     # d : 상어 이동 방향 1, 2, 3, 4 : 상하우좌
#     r, c, s, d, z = map(int, input().split())
#     box[r-1][c-1] = (s, d, z)
#
# # 낚시왕의 현재 위치
# index = -1
# # 낚시왕이 잡은 상어 크기 총합
# result = 0
#
# while index < C-1:
#     # 낚시왕의 이동
#     index += 1
#     # 제일 가까운 상어 잡기
#     for i in range(R):
#         if box[i][index] != 0:
#             s, d, z = box[i][index]
#             result += z
#             box[i][index] = 0
#             break
#
#     # 상어 이동
#     # 이동 결과를 담을 배열
#     move_result = [[0 for _ in range(C)] for _ in range(R)]
#     for r in range(R):
#         for c in range(C):
#             # 상어가 있음
#             if box[r][c] != 0:
#                 row = r
#                 col = c
#                 s, d, z = box[r][c]
#                 speed = s
#                 direction = d
#                 size = z
#                 while speed >= 0:
#                     # 1. 위로
#                     if direction == 1:
#                         if row - 1 < 0 or row - 1 >= R:
#                             direction = 2
#                             row += 1
#                         else:
#                             row -= 1
#                     # 2. 아래로
#                     elif direction == 2:
#                         if row + 1 < 0 or row + 1 >= R:
#                             direction = 1
#                             row -= 1
#                         else:
#                             row += 1
#                     # 3. 오른쪽으로
#                     elif direction == 3:
#                         if col + 1 < 0 or col + 1 >= C:
#                             direction = 4
#                             col -= 1
#                         else:
#                             col += 1
#                     # 4. 왼쪽으로
#                     elif direction == 4:
#                         if col - 1 < 0 or col - 1 >= C:
#                             direction = 3
#                             col += 1
#                         else:
#                             col -= 1
#                     speed -= 1
#
#                 if move_result[row][col] == 0:
#                     move_result[row][col] = (s, d, z)
#                 else:
#                     s1, d1, z1 = move_result[row][col]
#                     if z > z1:
#                         move_result[row][col] = (s, d, z)
#
#     for r in range(R):
#         for c in range(C):
#             box[r][c] = move_result[r][c]
#
# print(result)