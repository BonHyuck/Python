# def find_path(cnt, mag):
#     global result
#     if cnt >= N:
#         if mag < result:
#             result = mag
#         return
#
#     if mag > result:
#         return
#
#     for i in range(1, N+1):
#         # 이미 방문한 정점에서 시작
#         if visited[i] == 1:
#             for j in range(1, N+1):
#                 if visited[j] == 0 and powers[i][j] > 0:
#                     # 방문처리
#                     visited[j] = 1
#                     find_path(cnt + 1, mag + powers[i][j])
#                     visited[j] = 0
#
#     return
#
#
# # N개의 정점, M개의 간선
# N, M = map(int, input().split())
# # 방문 체크 배열 미리 생성
# visited = [0] * (N + 1)
# # 간선정보 저장 배열
# powers = [[0 for _ in range(N+1)] for _ in range(N+1)]
# edges = []
# for k in range(M):
#     v1, v2, m = map(int, input().split())
#     powers[v1][v2] = m
#     powers[v2][v1] = m
#     edges.append((v1, v2, m))
#
# # print(powers)
# # print(edges)
# for v1, v2, m in edges:
#     visited[v1] = 1
#     visited[v2] = 1
#     result = float('inf')
#     find_path(2, m)
#
#     visited[v1] = 0
#     visited[v2] = 0
#
#     print(result)
#
