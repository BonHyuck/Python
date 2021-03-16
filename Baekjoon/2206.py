dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def find_path():
    queue = [[(0, 0)]]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = -1
    while queue:
        cnt += 1
        next = queue.pop(0)
        mid_queue = []
        while next:
            row, col = next.pop(0)
            for k in range(4):
                new_r = row + dx[k]
                new_c = col + dy[k]
                if new_r == N - 1 and new_c == M - 1:
                    return cnt

                if 0 <= new_r < N and 0 <= new_c < M:
                    if box[new_r][new_c] == 0 and visited[new_r][new_c] == 0:
                        visited[new_r][new_c] = 1
                        mid_queue.append((new_r, new_c))
            if len(mid_queue):
                queue.append(mid_queue)

    return 987654321


N, M = map(int, input().split())
box = [list(map(int, list(input()))) for _ in range(N)]

# 벽의 좌표
walls = []
for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            walls.append((r, c))

result = 987654321
while walls:
    wall_r, wall_c = walls.pop(0)
    box[wall_r][wall_c] = 0
    result = min(result, find_path())
    box[wall_r][wall_c] = 1

if result == 987654321:
    result = -1
print(result)