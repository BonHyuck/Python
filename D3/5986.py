# SWEA 5986
# 정수론
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    primes = []
    # N보다 작은 소수 구하기
    for number in range(2, N):
        check = True
        for i in range(2, number):
            if number != i and number % i == 0:
                check = False
                break
        if check:
            primes.append(number)
    # 개수를 세기 위한 변수
    cnt = 0

    for i in primes:
        for j in primes:
            if N - (i + j) in primes and i <= j <= N - (i + j):
                cnt += 1

    print('#{} {}'.format(test_case, cnt))
