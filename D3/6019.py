# SWEA 6019
# 폰 노이만 기차와 파리
T = int(input())
for test_case in range(1, T+1):
    # D : 기차 사이 거리
    # A : A 기차의 속력
    # B : B 기차의 속력
    # F : 파리의 속력
    D, A, B, F = map(int, input().split())
    print('#{} {}'.format(test_case, D * F / (A + B)))
