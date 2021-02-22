dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 행, 현재 열, 붙어있는 개수, 병사 색깔
def find_path(row, col, cnt, letter):
    global white, blue
    queue = [[(row, col)]]
    temp = cnt
    while queue:
        queue_arr = queue.pop(0)
        temp_queue = []
        for i, j in queue_arr:
            box[i][j] = 0
            for k in range(4):
                new_r = i + dx[k]
                new_c = j + dy[k]
                if 0 <= new_r < M and 0 <= new_c < N:
                    if box[new_r][new_c] == letter:
                        temp += 1
                        box[new_r][new_c] = 0
                        temp_queue.append((new_r, new_c))
        if len(temp_queue) > 0:
            queue.append(temp_queue)

    if letter == "W":
        white += temp ** 2
    elif letter == "B":
        blue += temp ** 2

# N: 가로, M: 세로
N, M = map(int, input().split())
box = []
for _ in range(M):
    box.append(list(input()))

# 내 병사
white = 0
# 적국 병사사
blue = 0

for r in range(M):
    for c in range(N):
        if box[r][c] != 0:
            find_path(r, c, 1, box[r][c])

print(white, blue)