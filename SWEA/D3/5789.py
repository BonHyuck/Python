# SWEA 5789
# 상자 바꾸기
T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0 for _ in range(N)]

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for k in range(N):
            if L-1 <= k <= R-1:
                box[k] = i

    print('#{} {}'.format(test_case, ' '.join(map(str, box))))
