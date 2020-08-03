# SWEA 1954
# 달팽이가 사각형 모양으로 돌면서 숫자를 새긴다.
# input = 달팽이 N

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 달팽이
    N = int(input())
    # 달팽이 크기 배열화
    snail = [[0 for i in range(N)] for j in range(N)]
    # N 훼손 방지, 새로운 변수에 넣기
    p = N
    # 세로줄 index
    x = 0
    # 한 줄 내 index
    y = -1
    # 방향
    d = 1
    # 1부터 입력 시작
    val = 1
    while p >= 0:
        # 가로로 이동하며 값 채우기
        for i in range(p):
            y += d
            snail[x][y] = val
            val += 1
        # 카운터 -1
        p -= 1
        # 세로로 이동하며 값 채우기
        for i in range(p):
            x += d
            snail[x][y] = val
            val += 1
        # 방향 전환
        d = d*-1
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()