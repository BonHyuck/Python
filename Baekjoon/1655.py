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