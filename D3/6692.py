# SWEA 6692
# 월급을 확률로 받는다...
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 경우의 수
    N = int(input())
    # 확률 리스트
    probability = []
    # 액수 리스트
    money = []
    # 결과 담기
    result = 0
    # 값을 받아서 리스트에 넣기
    for i in range(N):
        p, m = map(float, input().split())
        probability.append(p)
        money.append(m)

    # 계산
    for index in range(0, len(probability)):
        result += (probability[index] * money[index])

    print('#{} {}'.format(test_case, result))


