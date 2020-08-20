# SWEA 6057
# 삼각형이 있는가
'''
1
3 3
1 2
2 3
1 3
'''
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     # N : 1~N 까지의 점
#     # M : 선의 개수
#     N, M = map(int, input().split())
#     # 각 점을 담기위한 리스트
#     points = []
#
#     for _ in range(M):
#         points.append(sorted(list(map(int, input().split()))))
#
#     result = 0
#
#     for start in points:
#         for end in points:
#             if end[0] == start[1] and [start[0], end[1]] in points:
#                 result += 1
#
#     print('#{} {}'.format(test_case, result))

T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    lists = [[0 for j in range(N+1)] for i in range(N+1)]
    for i in range(M):
        x,y = list(map(int,input().split()))
        lists[x][y] = 1
        lists[y][x] = 1
    res = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            for k in range(j+1,N+1):
                if lists[i][j] and lists[j][k] and lists[k][i]:
                    res += 1
    print(f'#{tc} {res}')