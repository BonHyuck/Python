# SWEA 6057
# 삼각형이 있는가
'''
1
3 3
1 2
2 3
1 3
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N : 1~N 까지의 점
    # M : 선의 개수
    N, M = map(int, input().split())
    # 어떤 점을 잇는지 나타내는 배열
    total_list = []

    for i in range(M):
        XY = list(map(int, input().split()))
        total_list.append(XY)

    result = 0

    for i in range(M-1):
        for j in range(i+1, M):
            if sorted([total_list[i][0], total_list[j][1]]) in total_list and i != j:
                result += 1


    print('#{} {}'.format(test_case, result))

