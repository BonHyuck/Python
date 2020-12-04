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

# 가로세로 탐색을 위한 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# row : 현재 위치한 곳의 행 index
# col : 현재 위치한 곳의 열 index
# height : 현재 위치한 곳의 높이
# dig : 공사 횟수, 1 = 이미 공사를 1번 했으므로 다음 공사는 없음
# length : 등산로의 길이
def start_hiking(row, col, height, dig, length):
    global result
    
    if length > result:
        result = length

    # 일단 방문 처리
    visited[row][col] = 1

    # 가로세로 탐색
    for k in range(4):
        # 다음에 갈 좌표
        new_row = row + dx[k]
        new_col = col + dy[k]
        # 인덱스 오류 방지
        if 0 <= new_row < N and 0 <= new_col < N:
            new_height = box[new_row][new_col]
            # 아직 방문을 안 했음
            if visited[new_row][new_col] == 0:
                # 높이가 낮은 곳이므로 이동 가능
                if new_height < height:
                    start_hiking(new_row, new_col, new_height, dig, length+1)
                # 높이가 더 높거나 같음
                else:
                    # 아직 공사 안함
                    if dig == 0:
                        for depth in range(1, K+1):
                            box[new_row][new_col] -= depth
                            if box[new_row][new_col] < height:
                                start_hiking(new_row, new_col, box[new_row][new_col], 1, length+1)
                            # 원상복구
                            box[new_row][new_col] += depth

    visited[row][col] = 0

    return


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    # N : 지도 한변의 길이
    # K : 최대 공사 깊이
    N, K = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 가장 높은 지점의 높이를 구하기 위한 변수
    maxPoint = 0
    # 가장 높은 지점의 높이 구하기
    for i in range(N):
        for j in range(N):
            if box[i][j] > maxPoint:
                maxPoint = box[i][j]

    # 높은 지점이 여러개일수 있으니 배열 준비
    maxPoints = []
    # 가장 높은 지점의 행, 열 값을 배열에 저장한다.
    for i in range(N):
        for j in range(N):
            if box[i][j] == maxPoint:
                maxPoints.append((i, j))

    # 결과값
    result = 0

    # 높은 지점의 배열을 Queue의 형태로 사용한다.
    while maxPoints:
        # 가장 앞에 있는 행(r), 열(c) 값을 가져온다.
        r, c = maxPoints.pop(0)
        start_hiking(r, c, box[r][c], 0, 1)

    print('#{} {}'.format(test_case, result))

