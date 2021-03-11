# first = input()
# second = input()
# # 둘 중 짧은거
# small = ''
# # 둘 중 긴거
# large = ''
# # 결과값
# result = 1
# if len(first) <= len(second):
#     small = first
#     large = second
# else:
#     small = second
#     large = first
#
# while True:
#     find_max = True
#     for index in range(len(small) - result + 1):
#         sample = small[index:index + result]
#         if sample in large:
#             find_max = False
#             break
#     if not find_max:
#         result += 1
#     else:
#         break
#
# print(result - 1)

# first = input()
# second = input()
# # 둘 중 짧은거
# small = ''
# # 둘 중 긴거
# large = ''
# # 결과값
# result = 1
# if len(first) <= len(second):
#     small = first
#     large = second
# else:
#     small = second
#     large = first
#
# while True:
#     find_max = True
#     for index in range(len(small) - result + 1):
#         sample = small[index:index + result]
#         for jndex in range(len(large) - result + 1):
#             if sample == large[jndex:jndex + result]:
#                 find_max = False
#                 break
#         if not find_max:
#             break
#     if not find_max:
#         result += 1
#     else:
#         break
#
# print(result - 1)

# first = input()
# second = input()
# # 둘 중 짧은거
# small = ''
# # 둘 중 긴거
# large = ''
# # 결과값
# result = 1
# if len(first) <= len(second):
#     small = first
#     large = second
# else:
#     small = second
#     large = first
#
# while True:
#     find_max = True
#     for index in range(len(small) - result + 1):
#         sample = small[index:index + result]
#         for jndex in range(len(large) - result + 1):
#             if sample == large[jndex:jndex + result]:
#                 find_max = False
#                 break
#         if not find_max:
#             break
#     if not find_max:
#         result += 1
#     else:
#         break
#
# print(result - 1)

# first = input()
# second = input()
# # 둘 중 짧은거
# small = ''
# # 둘 중 긴거
# large = ''
# # 결과값
# result = 1
# if len(first) <= len(second):
#     small = first
#     large = second
# else:
#     small = second
#     large = first
#
# # 긴 문자열에서 확인할 인덱스
# large_index = [i for i in range(len(large))]
#
# while len(large_index) > 0:
#     length = len(large_index)
#     for _ in range(length):
#         index = large_index.pop(0)
#         if index + result <= len(large):
#             sample = large[index:index + result]
#             if sample in small:
#                 large_index.append(index)
#     if len(large_index) == 0:
#         break
#     else:
#         result += 1
#
# print(result - 1)

first = input()
second = input()

dp = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]
result = 0
for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            result = max(result, dp[i+1][j+1])

print(result)

first = input()
second = input()

dp = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            dp[i+1][j+1] = dp[i][j] + 1

print(max(map(max, dp)))