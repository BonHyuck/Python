import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    # 사람들
    people = input()
    # 기립박수를 치는 사람 수
    cnt = 0
    # 기립박수를 위해 고용되는 사람 수
    result = 0
    for i in range(len(people)):
        # 기립박수의 조건 충족됨
        if i <= cnt:
            cnt += int(people[i])
        # 기립박수의 조건 충족되지 않음
        else:
            # 고용해야하는 사람에 해당 숫자만큼 더한다.
            result += (i - cnt)
            # 기립박수를 치고 있는 사람 처리
            cnt += 1 + int(people[i])

    print('#{} {}'.format(test_case, result))