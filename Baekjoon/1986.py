# N x M 체스판
N, M = map(int, input().split())
# 체스판 제작
box = [[0 for _ in range(M)] for _ in range(N)]

# 퀸
queen = []
q_arr = list(map(int, input().split()))
for k in range(q_arr.pop(0)):
    queen.append((q_arr[2 * k] - 1, q_arr[2 * k + 1] - 1))
    box[q_arr[2 * k] - 1][q_arr[2 * k + 1] - 1] = 2
# 나이트
knight = []
k_arr = list(map(int, input().split()))
for k in range(k_arr.pop(0)):
    knight.append((k_arr[2 * k] - 1, k_arr[2 * k + 1] - 1))
    box[k_arr[2 * k] - 1][k_arr[2 * k + 1] - 1] = 2
# 폰
# 일반 장애물이기 때문에 queue 형태로 저장 필요 없음
p_arr = list(map(int, input().split()))
for k in range(p_arr.pop(0)):
    box[p_arr[2 * k] - 1][p_arr[2 * k + 1] - 1] = 2

# 안전한 칸 = 닿을 수 없는 곳
while queen:
    q_row, q_col = queen.pop(0)
    # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
    for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        move = 0
        while True:
            move += 1
            new_r = q_row + (r * move)
            new_c = q_col + (c * move)
            # 인덱스 확인
            if 0 <= new_r < N and 0 <= new_c < M:
                # 다른 말이 있음
                if box[new_r][new_c] == 2:
                    break
                elif box[new_r][new_c] == 0:
                    box[new_r][new_c] = 1
            else:
                break

# 나이트
while knight:
    k_row, k_col = knight.pop(0)
    # 나이트가 갈수 있는 방향
    for r, c in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
        new_r = k_row + r
        new_c = k_col + c
        # 인덱스 확인
        if 0 <= new_r < N and 0 <= new_c < M:
            # 다른 말이 있으면 처리 안하면 됨
            if box[new_r][new_c] == 0:
                box[new_r][new_c] = 1

# 폰은 안해도 됨
result = 0
for k in range(N):
    result += box[k].count(0)
    
print(result)