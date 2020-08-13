# SWEA 10505
# 평균 이하의 소득 구하기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 사람 수
    N = int(input())
    # 소득 배열
    salary = list(map(int, input().split()))
    # 평균 값
    avg = 0
    # 평균 구하기
    for item in salary:
        avg += item
    avg = avg/len(salary)
    # 평균 이하의 사람 수
    cnt = 0
    for item in salary:
        if item <= avg:
            cnt += 1

    print('#{} {}'.format(test_case, cnt))
