import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    # 입력값 받기
    N, M = map(int, input().split())

    result = 'ON'

    for i in range(N):
        if M % 2 == 0:
            result = 'OFF'
            break
        M //= 2

    print('#{} {}'.format(test_case, result))