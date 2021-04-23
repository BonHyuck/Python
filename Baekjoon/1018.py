
def find_chess(row, col):
    # 선택된 왼쪽 위의 색 가져오기
    color = box[row][col]
    # 선택된 왼쪽 위의 색 기준 칠해야되는 칸
    paint = 0
    for new_r in range(row, row+8):
        for new_c in range(col, col+8):
            # 색이 달라야하는 칸
            if (new_r + new_c) % 2 != (row + col) % 2:
                if box[new_r][new_c] == color:
                    paint += 1
            # 색이 같아야하는 칸
            else:
                if box[new_r][new_c] != color:
                    paint += 1

    if color == 'W':
        color = 'B'
    else:
        color = 'W'

    another_paint = 0
    for new_r in range(row, row+8):
        for new_c in range(col, col+8):
            # 색이 달라야하는 칸
            if (new_r + new_c) % 2 != (row + col) % 2:
                if box[new_r][new_c] == color:
                    another_paint += 1
            # 색이 같아야하는 칸
            else:
                if box[new_r][new_c] != color:
                    another_paint += 1

    return min(paint, another_paint)


N, M = map(int, input().split())
box = [list(map(str, input())) for _ in range(N)]
# 결과값
result = 987654321
# 맨 왼쪽 위칸을 중심으로 탐색
# N-1+8까지의 행만 검사
for r in range(N-7):
    # M-1+8까지의 열만 검사
    for c in range(M-7):
        result = min(find_chess(r, c), result)

print(result)

'''
8 8
WWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB'''