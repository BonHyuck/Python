# 가려는 채널
N = int(input())
# 고장난 버튼 수
M = int(input())
# 고장난 버튼들
broken = list(map(int, input().split()))
# # 그냥 누르기
# result = abs(N - 100)
# push_button = 0
# # 버튼 안눌러도 됨
# no_click = True
# for b in broken:
#     if str(b) in str(N):
#         no_click = False
#         break
# # 고장난 버튼 없으니까 바로 채널로 갈수 있음
# if no_click:
#     # 버튼 숫자 누르기
#     length = len(str(N))
#     if length < result:
#         result = length
# else:
#     # 다음으로 가까운 채널이 어디인가.
#     step = 0
#     while True:
#         step += 1
#         prev = N - step
#         next = N + step
#
#         yes_prev = True
#         yes_next = True
#
#         for b in broken:
#             if str(b) in str(prev):
#                 yes_prev = False
#                 break
#         for b in broken:
#             if str(b) in str(next):
#                 yes_next = False
#                 break
#
#         if yes_prev:
#             push_button = prev
#             break
#         if yes_next:
#             push_button = next
#             break
#     if result > abs(N - push_button) + len(str(push_button)):
#         result = abs(N - push_button) + len(str(push_button))
#
# print(result)

# 가려는 채널
N = int(input())
# 고장난 버튼 수
M = int(input())
broken = []
if M != 0:
    # 고장난 버튼들
    broken = list(map(int, input().split()))
# 그냥 +, - 버튼으로 이동
result = abs(N - 100)

# 아예 처음부터 조진다.
# N은 0부터 500000까지 가능하지만 500000보다 큰 수에서 내려올수도 있으니
# 0부터 500000까지 올라오는만큼 더 뽑아준다.
for k in range(1000001):
    # 해당 번호 (k)에 숫자 버튼으로 도착 가능한가??
    yes_number = True
    for letter in str(k):
        # 숫자 버튼으로 못감
        if int(letter) in broken:
            yes_number = False
            break
    # 숫자만 눌러서 도착 가능하다
    if yes_number:
        # 숫자 누르기 + +,- 버튼 횟수
        length = len(str(k)) + abs(N - k)
        if result > length:
            result = length
print(result)