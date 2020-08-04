T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # p = 처음 꽂을 때 올바른 면 확률
    # q = 올바른 면일때 꽂힐 확률
    p, q = map(float, input().split())

    # s1 = 1번 뒤집음 => 잘못된 면으로 시작
    # s2 = 2번 뒤집음 => 잘된 면으로 시작해서 실패
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q

    result = ''
    if s1 < s2:
        result = 'YES'
    else:
        result = 'NO'

    print('#{} {}'.format(test_case, result))




