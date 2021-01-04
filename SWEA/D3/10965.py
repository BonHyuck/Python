# 제곱수 만들기

import sys
sys.stdin = open('input.txt', 'r')

# 소수는 2로 시작해서 이후에는 홀수만 해당된다.
prime_numbers = [2]
for number in range(3, int(10000000 ** (1/2)), 2):
    for prime in prime_numbers:
        # 소수로 나누어 떨어지면 소수 아님
        if not number % prime:
            break
    else:
        prime_numbers.append(number)

answer = []
T = int(input())
for test_case in range(1, T+1):
    # 초기 숫자 받기
    A = int(input())
    # 결과 값
    result = 1

    # 이미 거듭제곱이면 result = 1 로 끝낼수 있음
    if A ** (1/2) != int(A ** (1/2)):
        for prime in prime_numbers:
            # 해당 숫자 세기
            cnt = 0
            # 해당 소수로 나누어 떨어지는 동안 지속
            while A % prime == 0:
                A = A // prime
                cnt += 1
            # 홀수
            if cnt % 2:
                result *= prime
            # 종료
            if A == 1 or prime > A:
                break
        # A가 1이 되지 못하면
        if A > 1:
            result *= A

    # print('#{} {}'.format(test_case, result))
    answer.append("#{} {}".format(test_case, result))

for i in answer:
    print(i)


    # # 소인수분해
    # dict = {}
    # result = 1
    # if A > 1:
    #     for i in range(2, A):
    #         if i > 2 and i % 2 == 0:
    #             continue
    #         while A > 1 and A % i == 0:
    #             dict[i] = dict.get(i, 0) + 1
    #             A = A / i
    #         if A == 1:
    #             break
    #
    # # print(dict, len(dict))
    # if len(dict) == 0:
    #     result = A
    # else:
    #     for number, count in dict.items():
    #         if count % 2 == 1:
    #             result *= number
    #
    # print('#{} {}'.format(test_case, result))
