# # 말하는 숫자의 개수
# N = int(input())
# # 숫자를 담을 배열
# arr = []
#
# for _ in range(N):
#     # 입력값 배열에 넣기
#     arr.append(int(input()))
#     # 정렬
#     arr.sort()
#     print(arr[len(arr)//2 - ((len(arr) + 1) % 2)])

# # 말하는 숫자의 개수
# N = int(input())
# # -10000 <= 숫자 <= 10000
# # 숫자 + 10000 = index
# arr = [0 for _ in range(20001)]
#
# for k in range(N):
#     number = int(input())
#     arr[number + 10000] = 1
#     check = (k+2) // 2
#     cnt = 0
#     for i in range(20001):
#         if arr[i] == 1:
#             cnt += 1
#             if cnt == check:
#                 print(i - 10000)
#                 break

# def quick_sort(box):
#     if len(box) <= 1:
#         return box
#     pivot = box[len(box) // 2]
#     left_arr, mid_arr, right_arr = [], [], []
#     for num in box:
#         if num < pivot:
#             left_arr.append(num)
#         elif num > pivot:
#             right_arr.append(num)
#         else:
#             mid_arr.append(num)
#     return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)
#
# # 말하는 숫자의 개수
# N = int(input())
# # 숫자를 담을 배열
# arr = []
#
# for _ in range(N):
#     # 입력값 배열에 넣기
#     arr.append(int(input()))
#     # 정렬
#     arr = quick_sort(arr)
#     print(arr[len(arr)//2 - ((len(arr) + 1) % 2)])

# from collections import deque
#
# # 말하는 숫자의 개수
# N = int(input())
# # 숫자를 담을 배열
# # 첫 번째 숫자 넣어두고 시작
# arr = deque([])
# # print(arr[0])
#
# for i in range(N):
#     # 입력값
#     number = int(input())
#     temp = deque([])
#     if i == 0:
#         arr.append(number)
#     else:
#         while True:
#             # Deque에서 맨 뒤에 숫자를 뺀다.
#             compare = arr.pop()
#             if compare > number:
#                 temp.appendleft(compare)
#             else:
#                 arr.append(compare)
#                 arr.append(number)
#                 arr.extend(temp)
#                 break
#
#             if len(arr) == 0:
#                 arr.append(number)
#                 arr.extend(temp)
#                 break
#     print(arr[(len(arr) - 1)//2])


# # 말하는 숫자의 개수
# N = int(input())
# # 숫자를 담을 배열
# arr = [int(input())]
# print(arr[0])
#
# for _ in range(N-1):
#     number = int(input())
#     inserted = False
#     for k in range(len(arr)-1, -1, -1):
#         # 뒤에서부터 비교해서 넣어주기
#         if arr[k] < number:
#             arr.insert(k+1, number)
#             inserted = True
#             break
#     # 중간에 안넣어졌으면 맨 앞에 넣어주기
#     if not inserted:
#         arr.insert(0, number)
#
#     print(arr[len(arr)//2 - ((len(arr) + 1) % 2)])

# 이분 탐색으로 인덱스 찾기
# num = 입력값으로 받은 비교 숫자
# def make_index(num):
#     start = 0
#     end = len(arr)
#     while start < end:
#         center = (start + end) // 2
#         # 중앙값이 입력값과 같으면 중앙에 넣어주면 끝
#         if arr[center] == num:
#             return center
#         # 중앙값이 입력값보다 크기때문에 중앙값을 끝으로 두고 새로운 중앙값 도출
#         elif arr[center] > num:
#             end = center
#         # 중앙값이 입력값보다 작으면 중앙값보다 한칸 뒤에 있는 숫자를
#         # 시작으로 두고 새로운 중앙값 도출
#         else:
#             start = center + 1
#     return end
#
#
# # 말하는 숫자의 개수
# N = int(input())
# # 숫자를 담을 배열
# arr = []
#
# for _ in range(N-1):
#     number = int(input())
#
#     insert_index = 0
#
#     insert_index = make_index(number)
#
#     arr.insert(insert_index, number)
#
#     print(arr[(len(arr) - 1)//2])

import heapq

def heap_solution(min_heap, max_heap, target):
    # max_heap의 루트 노드가 중간값
    # max_heap의 루트는 항상 min_heap의 루트보다 같거나 작아야 한다
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -target)
    else:
        heapq.heappush(min_heap, target)
    if min_heap and -max_heap[0] > min_heap[0]:
        max_insert = -heapq.heappop(min_heap)
        min_insert = -heapq.heappop(max_heap)

        heapq.heappush(max_heap, max_insert)
        heapq.heappush(min_heap, min_insert)


N = int(input())
min_heap, max_heap = [], []
for step in range(N):
    number = int(input())

    heap_solution(min_heap, max_heap, number)
    print(-max_heap[0])