# 벽돌깨기

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


# k : 값을 변경할 인덱스
def set_location(k):
    # 끝까지 변경이 됐다면
    if k >= N:
        # 구슬 발사
        shoot()
        return

    # 0 ~ W-1 까지 인덱스가 가능하다
    for i in range(W):
        drop[k] = i
        # 다음 칸 바꿔주기
        set_location(k + 1)

# 상하좌우 확인을 위한 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def shoot():
    global result

    if result == 0:
        return

    for i in range(H):
        for j in range(W):
            sample[i][j] = box[i][j]
    # 깨진 벽돌 리스트
    queue = deque([])
    # 구슬을 N번 쏜다.
    for k in range(N):
        # 구슬을 쏠 열 번호
        c = drop[k]
        # 구슬을 쏠 행 번호
        r = 0
        for i in range(H):
            # 벽돌이 있음
            if sample[i][c] != 0:
                # 행번호 설정
                r = i
                break

        queue.append((r, c))
        while queue:
            # 깨진 벽돌 좌표
            row, col = queue.popleft()
            # 깨진 벽돌의 숫자만큼 옆으로 퍼져나간다.
            for distance in range(1, sample[row][col]):
                # 상하좌우 4방향 탐색
                for j in range(4):
                    new_row = row + dx[j] * distance
                    new_col = col + dy[j] * distance
                    # 인덱스 오류 방지 + 벽돌 확인
                    if 0 <= new_row < H and 0 <= new_col < W:
                        if sample[new_row][new_col] > 1:
                            queue.append((new_row, new_col))
                        elif sample[new_row][new_col] == 1:
                            sample[new_row][new_col] = 0

            sample[row][col] = 0
        # 벽돌깨기 끝

        # 빈칸이 생겼으므로 아래로 떨어진다.
        # 각 열마다 진행한다.
        for c in range(W):
            stack = []
            for r in range(H):
                if sample[r][c] > 0:
                    stack.append(sample[r][c])
                sample[r][c] = 0

            index = H - 1
            while stack:
                sample[index][c] = stack.pop(-1)
                index -= 1



    # 구슬 쏘기 끝
    total = 0
    for i in range(H):
        for j in range(W):
            if sample[i][j] > 0:
                total += 1

    if total < result:
        result = total
                
        
        

        
        

# 테스트 케이스 개수
T = int(input())
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(H)]
    sample = [[0 for _ in range(W)] for _ in range(H)]
    # 구슬을 쏠 인덱스 리스트
    drop = [0] * N

    # 최소값이 출력돼야 하기 때문에 큰 값으로 설정
    result = float('inf')
    
    # 구슬을 쏠 인덱스 설정 함수
    set_location(0)

    print('#{} {}'.format(test_case, result))




