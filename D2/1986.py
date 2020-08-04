# SWEA 1986
# 1 ~ N 까지 홀수는 더하고 짝수는 뺀 결과 출력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # 결과용 변수
    result = 0

    for i in range(1, N+1):
        if i % 2 == 0:
            result -= i
        else:
            result += i

    print('#{} {}'.format(test_case, result))