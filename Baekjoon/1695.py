# N = int(input())
# arr = list(map(int, input().split()))
# queue = []
# for number in arr:
#     if number in queue:
#         queue.remove(number)
#     else:
#         queue.append(number)
# print(len(queue) - 1)

# N = int(input())
# arr = list(map(int, input().split()))
# start = 0
# end = N-1
# result = 0
# while start <= end:
#     if arr[start] == arr[end]:
#         start += 1
#         end -= 1
#     else:
#         if arr[start] > arr[end]:
#             end -= 1
#             result += 1
#         else:
#             start += 1
#             result += 1
# print(result)
#
# import sys
# sys.setrecursionlimit(1000000)
#
# def find_number(start, end):
#     if start > end:
#         return 0
#
#     result = box[start][end]
#     if result != -1:
#         return result
#
#     if arr[start] == arr[end]:
#         result = find_number(start+1, end-1)
#     else:
#         result = min(find_number(start+1, end) + 1, find_number(start, end - 1) + 1)
#
#     return result
#
#
# N = int(input())
# arr = list(map(int, input().split()))
# box = [[-1 for _ in range(N)] for _ in range(N)]
# result = find_number(0, N - 1)
#
# print(result)

def find_value(s, e):
    if box[s][e] != -1:
        return box[s][e]
    if s >= e:
        box[s][e] = 0
        return box[s][e]
    if arr[s] == arr[e]:
        box[s][e] = find_value(s+1, e-1)
    else:
        box[s][e] = min(find_value(s, e-1), find_value(s+1, e)) + 1

    return box[s][e]

N = int(input())
arr = list(map(int, input().split()))
box = [[-1 for _ in range(5001)] for _ in range(5001)]
for start in range(0, N-1):
    for end in range(start+1, N):
        find_value(start, end)
print(box[0][N-1])