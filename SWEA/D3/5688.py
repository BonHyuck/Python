# SWEA 5688
# 세제곱근
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    number = N ** (1/3)
    if abs(int(round(number, 0)) - number) > 1E-6:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, int(round(number, 0))))