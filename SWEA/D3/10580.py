import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 결과값을 담을 변수
    result = 0
    # 전선을 담을 변수
    wires = []

    for j in range(N):
        # 새로운 전선
        A, B = map(int, input().split())
        # 기존의 전선과 비교
        for k in range(len(wires)):
            A2, B2 = wires[k]
            # 새 전선의 시작점이 기존의 전선보다 낮으면서
            # 끝점은 기존의 전선보다 높으면 교차함
            if A < A2 and B > B2:
                result += 1
            # 새 전선의 시작점이 기존의 전선보다 높으면서
            # 끝점은 기존의 전선보다 낮으면 교차함
            elif A > A2 and B < B2:
                result += 1
        # 처리 이후 전선 배열에 넣어주기
        wires.append((A, B))

    print('#{} {}'.format(test_case, result))
