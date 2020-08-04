# SWEA 1984
# 10개의 수 중 최소값과 최대값을 제외한 8개 숫자의 평균 구하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    # 최대값, 최소값 구해놓기
    maximum = max(numbers)
    minimum = min(numbers)

    # 각각의 값을 확인하여 최대값과 최소값을 0으로 한다.
    for index, value in enumerate(numbers):
        if value == maximum or value == minimum:
            numbers[index] = 0

    print('#{} {}'.format(test_case, int(round(sum(numbers)/8, 0))))