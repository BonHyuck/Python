# SWEA 5549
# 홀짝
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    if N % 2 == 0:
        print("#{} Even".format(test_case))
    else:
        print("#{} Odd".format(test_case))