# 수영장
import sys
sys.stdin = open('input.txt', 'r')

# 경우의 수를 찾기 위한 함수
def find_plan(month, cost):
    global result

    # 최소 비용을 찾고 있는데 이미 산출한 결과보다 크면 더이상 진행할 이유가 없다.
    if cost > result:
        return

    # 월 초과
    if month > 11:
        if cost < result:
            result = cost
        return

    # 해당 월 이용 계획 있음
    if plan[month] > 0:
        # 1일 권 사용
        find_plan(month + 1, cost + plan[month] * d)
        # 1달 권 사용
        find_plan(month + 1, cost + o)
        # 3달권 사용
        find_plan(month + 3, cost + t)
        # 1년권은 이미 경우의 수에 있으므로 포함하지 않는다.
    # 없다면 다음 월로 넘어감
    else:
        find_plan(month + 1, cost)

# 테스트 케이스 개수
T = int(input())
for test_case in range(1, T+1):
    # 1일, 1달, 3달, 1년
    d, o, t, y = map(int, input().split())
    # 월별 이용계획
    plan = list(map(int, input().split()))
    # 모든 경우의 수를 탐색해야한다.
    # 어느 경우든 1년 이용권 사용은 있기때문에 기본값을 1년 이용권으로 한다.
    result = y
    # 경우의 수 찾기
    # 현재 월, 현재 금액
    find_plan(0, 0)

    # 결과 출력
    print('#{} {}'.format(test_case, result))

