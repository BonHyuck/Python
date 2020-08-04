# SWEA 10200
# 유튜브 구독자 최대값, 최소값 구하기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 입력 값 받기
    N, A, B = map(int, input().split())
    # 결과 변수 준비
    maximum = 0
    minimum = 0

    # 최대 값은 한 그룹이 다른 그룹의 부분 집합일때 작은 집합
    if A >= B:
        maximum = B
    else:
        maximum = A

    # 최소 값은 둘을 합한 뒤 전체의 차
    if N >= A + B:
        minimum = 0
    else:
        minimum = (A + B) - N

    print('#{} {} {}'.format(test_case, maximum, minimum))
