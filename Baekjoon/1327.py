# from copy import deepcopy
# import sys
# sys.setrecursionlimit(1000000)
#
# def find_answer(index, cnt, input_list):
#     global result
#
#     if cnt >= result:
#         return
#
#     new_arr = deepcopy(input_list)
#     end_index = index + K - 1
#     for i in range(index, ((end_index + index) // 2) + 1):
#         new_arr[i], new_arr[end_index+index-i] = new_arr[end_index+index-i], new_arr[i]
#
#     if sorted(arr) != new_arr:
#         for k in range(N - K + 1):
#             if index != k:
#                 find_answer(k, cnt + 1, new_arr)
#     else:
#         if result == -1:
#             result = cnt + 1
#         elif result > cnt + 1:
#             result = cnt + 1
#
#     return
#
# # N : 순열의 크기
# # K : 선택된 숫자 포함 뒤집을 개수
# N, K = map(int, input().split())
# arr = list(map(int, input().split()))
#
# result = 1000000
#
# for k in range(N - K + 1):
#     # 선택된 인덱스, 뒤집은 횟수, 배열
#     find_answer(k, 0, arr)
#
# print(result)

from copy import deepcopy

# N : 순열의 크기
# K : 선택된 숫자 포함 뒤집을 개수
N, K = map(int, input().split())
# 입력된 배열
arr = list(map(int, input().split()))
# 배열을 문자로
text = ''.join(str(k) for k in arr)
answer = ''.join(str(k) for k in sorted(arr))

result = -1

queue = [[arr]]
visited = set([text])

if text == answer:
    result = 0
else:
    while queue:
        mid_queue = []
        result += 1
        seq = queue.pop(0)
        finish = False
        for sample in seq:
            if ''.join(str(s) for s in sample) == answer:
                finish = True
                break
            for index in range(N - K + 1):
                check = deepcopy(sample)
                for jndex in range(K // 2):
                    check[index + jndex], check[index + K - jndex - 1] = check[index + K - jndex - 1], check[index + jndex]
                if ''.join(str(c) for c in check) not in visited:
                    mid_queue.append(check)
                    visited.add(''.join(str(c) for c in check))

        if finish:
            break

        if len(mid_queue) == 0:
            result = -1
            break
        else:
            queue.append(mid_queue)

print(result)
