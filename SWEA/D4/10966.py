import sys
sys.stdin = open('input.txt', 'r')

# 상하좌우를 위한 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_plz(N, M):
    queue = [(0, 0)] * (N * M)
    front = -1
    rear = -1
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if box[i][j] == 'W':
                rear += 1
                # 앞부분을 물의 좌표로 우선 채운다.
                queue[rear] = (i, j)
                # 물은 방문처리
                visited[i][j] = 1
    # 두개의 좌표가 다름 = 방문 안한 곳이 있음
    while front != rear:
        # 다음 좌표 확인
        front += 1
        # 현재 좌표
        r, c = queue[front]
        for k in range(4):
            # 상하좌우로 이동
            new_r = r + dx[k]
            new_c = c + dy[k]
            # 인덱스 확인 + 땅 여부 확인 + 방문 안한 곳
            if 0 <= new_r < N and 0 <= new_c < M and box[new_r][new_c] == 'L' and visited[new_r][new_c] == 0:
                rear += 1
                # 다음 좌표를 새김으로써 확인 표시
                queue[rear] = (new_r, new_c)
                # 시작점에서 한칸 떨어진 곳
                visited[new_r][new_c] = visited[r][c] + 1
    result = 0
    for i in range(N):
        for j in range(M):
            result += visited[i][j]
    # 물은 포함한 모든 좌표가 1씩 더 가지고 있음
    # 그래서 결과에 모든 좌표에 들어있는 1을 빼줘야한다.
    return result - N * M


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    box = [input() for _ in range(N)]
    print('#{} {}'.format(test_case, find_plz(N, M)))