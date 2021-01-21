import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    p, q, r = map(int, input().split())
    a, b, c, d = map(int, input().split())

    result = ""

    long = [0, 0]
    short = [0, 0]

    # 우선 2가지 경우로 나눈다
    # 1. 원의 중심이 사각형 안이나 모서리에 있을 때
    if a <= p <= c and b <= q <= d:
        # 원의 중심에서 가장 먼 꼭지점을 구한다
        if p - a > c - p:
            long[0] = p - a
            short[0] = c - p
        else:
            long[0] = c - p
            short[0] = p - a
        if q - b > d - q:
            long[1] = q - b
            short[1] = d - q
        else:
            long[1] = q - d
            short[1] = d - q
        # 내부에 있을땐 2가지 경우로 나뉜
        # 1. 원의 반지름 > 사각형의 꼭지점부터 원의 중심까지의 거리
        if r ** 2 >= (long[0] ** 2) + (long[1] ** 2):
            result = "YN"
        # 2. 원의 반지름 <= 사각형의 꼭지점부터 원의 중심까지의 거리
        else:
            if r > short[0] or r > short[1]:
                result = "YY"
            else:
                result = "NY"
    # 2. 원의 중심이 사각형의 밖에 있을때
    else:
        if abs(p - a) > abs(p - c):
            long[0] = abs(p - a)
            short[0] = abs(p - c)
        else:
            long[0] = abs(p - c)
            short[0] = abs(p - a)
        if abs(q - b) > abs(q - d):
            long[1] = abs(q - b)
            short[1] = abs(q - d)
        else:
            long[1] = abs(q - d)
            short[1] = abs(q - b)

        if r ** 2 >= (long[0] ** 2 + long[1] ** 2):
            result = "YN"
        else:
            result = "YY"

    print('#{} {}'.format(test_case, result))
