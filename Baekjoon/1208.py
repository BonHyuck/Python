# N, S = map(int, input().split())
# arr = list(map(int, input().split()))
# result = 0
#
# for i in range(2 ** N):
#     sub = []
#     for j in range(N):
#         if i & (1 << j):
#             sub.append(arr[j])
#     if len(sub) > 0:
#         if sum(sub) == S:
#             result += 1
#
# print(result)

# from itertools import combinations
#
# N, S = map(int, input().split())
# arr = list(map(int, input().split()))
# result = 0
#
# if sum(arr) == S:
#     result += 1
#
# for k in range(1, N):
#     sub_arr = list(combinations(arr, k))
#     for sample in sub_arr:
#         if sum(sample) == S:
#             result += 1
#
# print(result)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = 0