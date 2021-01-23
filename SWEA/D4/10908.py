import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = 0
    for A in range(N+1):
        number = 1
        B = N - A
        if A > B:
            for k in range(N, A, -1):
                number *= k
            if B != 0:
                for j in range(1, B+1):
                    number /= j
        else:
            for k in range(N, B, -1):
                number *= k
            if A != 0:
                for j in range(1, A+1):
                    number /= j

        if number % 2 == 0:
            result += 1

    print('#{} {}'.format(test_case, result))
