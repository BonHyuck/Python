# 등산로 조성
# 각각의 시작점에서 시작하여 탐색한다.

'''
1. 가장 높은 봉우리의 높이 h를 찾는다.
2. 높이가 h인 모든 칸에서 시작
3. 현재 칸에서 인접한 낮은 칸으로 이동하다.
4. 낮지 않은 칸은, 높이 차이가 k보다 작고 깎는 횟수가 낭아있으면 이동한다.
4-1. 이미 등산로에 포함된 칸을 깎지 않도록한다.
4-2. 깎은 칸 방향 탐색 후 다른 방향을 탐색할 때 원래 높이를 복원한다.
5. 각 칸에 들어갈 때 마다, 가장 긴 등산로와 비교해 최대 길이를 갱신한다.
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def start_walking(r, c, arr, cnt):
    global result

    current_height = arr[r][c]

    for k in range(4):
        new_r = r + dx[k]
        new_c = c + dy[k]
        if 0 <= new_r < N and 0 <= new_c < N:
            if visited[new_r][new_c] == 0 and arr[new_r][new_c] < current_height:
                visited[new_r][new_c] = 1
                start_walking(new_r, new_c, arr, cnt + 1)
                visited[new_r][new_c] = 0

    if result < cnt:
        result = cnt

    return


def start_hiking(point):
    row = point[0]
    col = point[1]

    new_box = box[:][:]

    for i in range(N):
        for j in range(N):
            if i != row or j != col:
                for k in range(K + 1):
                    new_box[i][j] -= k
                    start_walking(row, col, new_box, 1)
                    new_box[i][j] += k


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    maximum = 0
    for i in range(N):
        if maximum < max(box[i]):
            maximum = max(box[i])

    max_points = []
    for i in range(N):
        for j in range(N):
            if box[i][j] == maximum:
                max_points.append([i, j])

    for max_point in max_points:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[max_point[0]][max_point[1]] = 1
        start_hiking(max_point)

    print('#{} {}'.format(test_case, result))