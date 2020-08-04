# SWEA 1860
# 붕어빵을 만드는 데 손님이 먹을수 있을까 없을까
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N = 사람 수
    # M = 시간(초)
    # K = 붕어빵 개수
    N, M, K = map(int, input().split())
    # 손님 도착 시간
    customer = list(map(int, input().split()))
    # 오는 순서대로 정렬
    customer.sort()
    # 결과값
    result = ''

    # 현재 붕어빵 개수
    # K * (customer//M)
    for index, value in enumerate(customer):
        if K * (value // M) >= index + 1:
            result = 'Possible'
        else:
            result = 'Impossible'
            break

    print('#{} {}'.format(test_case, result))