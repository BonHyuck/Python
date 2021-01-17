import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    # N개의 좌표
    N = int(input())
    # 결과를 담을 변수
    result = 0
    # N번 반복
    for _ in range(N):
        x, y = map(int, input().split())
        # 원점에서 (x,y)까지 거리
        distance = ((x ** 2) + (y ** 2)) ** 0.5
        if distance <= 200:
            # 문제에서 주어진 수식 변경
            # 바깥쪽에 있는 가까운 원이기때문에
            # 1점을 빼줘야한다.
            p = -(distance // 20) + 10
            result += p

    print('#{} {}'.format(test_case, int(result)))

