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


# # 계산되는 인덱스, 계산된 숫자, 총합
# def find_sum(index, cnt, total):
#     global result
#
#     if cnt > 0 and total == S and index == N:
#         result += 1
#         return
#
#     if index >= N:
#         return
#
#     find_sum(index + 1, cnt + 1, total + arr[index])
#     find_sum(index + 1, cnt, total)
#
#
# N, S = map(int, input().split())
# arr = list(map(int, input().split()))
# result = 0
# # 혹시 모르니 일단 정렬
# arr.sort()
# find_sum(0, 0, 0)
#
# print(result)

# N, S = map(int, input().split())
# arr = list(map(int, input().split()))
# result = 0
# # 앞
# front = arr[:N//2]
# # 뒤
# back = arr[N//2:]
# # 앞 배열의 부분집합
# front_sub = []
# # 뒷 배열의 부분집합
# back_sub = []
# # 시간 복잡도가 반으로 줄기는 할듯
# for i in range(2 ** len(front)):
#     sub = []
#     for j in range(len(front)):
#         if i & (1 << j):
#             sub.append(front[j])
#     front_sub.append(sum(sub))
#
# for i in range(2 ** len(back)):
#     sub = []
#     for j in range(len(back)):
#         if i & (1 << j):
#             sub.append(back[j])
#     back_sub.append(sum(sub))
#
# # 정렬해주기
# front_sub.sort()
# back_sub.sort(reverse=True)
# # 더해줄 인덱스
# front_index = 0
# back_index = 0
#
# while front_index < len(front_sub) and back_index < len(back_sub):
#     total = front_sub[front_index] + back_sub[back_index]
#     # 결과 나옴
#     if total == S:
#         front_index += 1
#         back_index += 1
#         front_cnt = 1
#         back_cnt = 1
#         while front_index < len(front_sub) and front_sub[front_index] == front_sub[front_index-1]:
#             front_cnt += 1
#             front_index += 1
#         while back_index < len(back_sub) and back_sub[back_index] == back_sub[back_index - 1]:
#             back_cnt += 1
#             back_index += 1
#         result += front_cnt * back_cnt
#
#     elif total < S:
#         front_index += 1
#     elif total > S:
#         back_index += 1
#
# if S == 0:
#     result -= 1
# print(result)

'''
5 0
-7 -3 -2 5 8
'''

# 배열의 앞부분의 경우를 dict에 담기
def front(start, end, total):
    if start == end:
        dict[total] = dict.get(total, 0) + 1
        return
    # 현재 index의 원소 더하기
    front(start + 1, end, total + arr[start])
    # 현재 index의 원소 더하지 않기
    front(start + 1, end, total)

# 뒷부분 경우 dict에 있는 값과 계산
def back(start, end, total):
    global result
    # 끝까지 도달
    if start == end:
        # total만 더하면 S => S - total의 경우의 수만큼 결과에 더해주기
        result += dict.get(S-total, 0)
        return
    # 현재 index의 원소 더하기
    back(start + 1, end, total+arr[start])
    # 현재 index의 원소 더하지 않기
    back(start + 1, end, total)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
dict = {}

# 앞
front(0, N//2, 0)
# 뒤
back(N//2, N, 0)

# 아무 원소도 없는 경우 1번 빼주기
if S == 0:
    result -= 1

print(result)