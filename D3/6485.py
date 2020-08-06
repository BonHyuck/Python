# SWEA 6485
# 버스 노선
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 버스 노선 개수
    N = int(input())
    # A와 B 배열
    bus = []

    for i in range(N):
        ab = list(map(int, input().split()))
        bus.append(ab)
    # 정류장 개수
    P = int(input())
    # 정류장 번호
    C = []
    for i in range(P):
        oneC = int(input())
        C.append(oneC)

    result = [0 for _ in range(len(C))]

    for AB in bus:
        for cndex, calue in enumerate(C):
            if AB[0] <= calue <= AB[1]:
                result[cndex] += 1

    res = ' '.join(list(map(str, result)))

    print('#{} {}'.format(test_case, res))
