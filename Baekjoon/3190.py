dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 보드의 크기
N = int(input())
box = [[0 for _ in range(N)] for _ in range(N)]
# 결과 값
result = 0
# 뱀 위치 표시
# 현재 뱀 머리 위치
snake_row = 0
snake_col = 0
# 뱀 표시
# 꼬리 -> 머리
snake = [(0, 0)]
# 뱀 = 1
box[0][0] = 1
# 뱀의 방향
# 0, 1, 2, 3 = 상하좌우
snake_direction = 3
# 사과의 개수
K = int(input())
# 사과 등록
for k in range(K):
    row, col = map(int, input().split())
    # 사과 = 2
    box[row-1][col-1] = 2
time = []
# 뱀의 방향 전환 횟수
L = int(input())
prev_time = 0
for k in range(L):
    X, C = input().split()
    # 혹시 모르니까 정수로 바꿔주기
    X = int(X)
    time.append((X-prev_time, C))
    prev_time = X

# 주어진 방향전환이 다 끝나고도 계속 움직여야한다.
time.append((100, 'L'))

while time:
    X, C = time.pop(0)
    finish = False
    for x in range(X):
        next_row = snake_row + dx[snake_direction]
        next_col = snake_col + dy[snake_direction]
        # 벽에 부딪히나? => ㄴㄴ
        if 0 <= next_row < N and 0 <= next_col < N:
            # 일단 몸 길이를 늘린다.
            snake_row = next_row
            snake_col = next_col
            snake.append((next_row, next_col))
            # 자기 자신 확인
            if box[next_row][next_col] == 1:
                finish = True
                break
            # 위를 무사히 넘었다면
            result += 1
            # 사과 확인
            if box[next_row][next_col] == 2:
                box[next_row][next_col] = 1
                continue
            # 사과 없음
            else:
                box[next_row][next_col] = 1
                # 맨끝 꼬리 삭제
                tail_row, tail_col = snake.pop(0)
                box[tail_row][tail_col] = 0
        else:
            finish = True
            break
    # 방향 전환
    # 왼쪽
    if C == 'L':
        # 상(0) => 좌(2)
        # 하(1) => 우(3)
        # 좌(2) => 하(1)
        # 우(3) => 상(0)
        if snake_direction == 0 or snake_direction == 1:
            snake_direction += 2
        else:
            snake_direction = (snake_direction + 1) % 2
    elif C == 'D':
        # 상(0) => 우(3)
        # 하(1) => 좌(2)
        # 좌(2) => 상(0)
        # 우(3) => 하(1)
        if snake_direction == 2 or snake_direction == 3:
            snake_direction = snake_direction % 2
        else:
            snake_direction = 3 - snake_direction
                
    if finish:
        break

print(result+1)
