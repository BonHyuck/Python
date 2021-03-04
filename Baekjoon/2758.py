# def find_lotto(number, length):
#     global result
#
#     if length >= N:
#         result += 1
#         return
#
#     for next in range(number * 2, M//(2**(N-length-1)) + 1):
#         find_lotto(next, length + 1)
#
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     # 결과 값
#     result = 0
#     # 시작값의 경우의 수는 마지막 수//(2^(N-1)
#     for k in range(1, M//(2**(N-1)) + 1):
#         find_lotto(k, 1)
#
#     print(result)

# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     # 결과 값
#     result = 0
#     queue = []
#     # 시작값의 경우의 수는 마지막 수//(2^(N-1)
#     start_queue = []
#     for k in range(1, M//(2**(N-1)) + 1):
#         start_queue.append(k)
#     queue.append(start_queue)
#     index = 1
#     while index < N:
#         index += 1
#         prev_numbers = queue.pop(0)
#         next_numbers = []
#         for prev in prev_numbers:
#             for k in range(prev * 2, M//(2**(N - index)) + 1):
#                 next_numbers.append(k)
#         queue.append(next_numbers)
#
#     print(len(queue[0]))

# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     # 결과 값
#     result = 0
#     arr = [[0 for _ in range(N+1)] for _ in range(M+1)]
#     index = 1
#     # 시작값의 경우의 수는 마지막 수//(2^(N-1)
#     for k in range(1, M//(2**(N-1)) + 1):
#         arr[k][index] = 1
#
#     while index < N:
#         for prev in range(M//(2**(N - index + 1)) + 1, M//(2**(N - index)) + 1):
#             if arr[prev][index] >= 1:
#                 for next in range(prev * 2, M//(2**(N - index - 1)) + 1):
#                     arr[next][index+1] += arr[prev][index]
#         index += 1
#
#     for k in range(1, M+1):
#         if arr[k][N] > 0:
#             result += arr[k][N]
#     print(result)

# T = int(input())
# for text_case in range(1, T+1):
#     N, M = map(int, input().split())
#     # 결과 값
#     result = 0
#     arr = [[0 for _ in range(N+1)] for _ in range(M+1)]
#     # 시작은 어떤 수든 올 수 있다고 치자
#     for k in range(1, M+1):
#         arr[k][1] = 1
#
#     # 숫자가 몇번째인가?
#     for index in range(2, N+1):
#         # index번째의 어떤숫자를 확인해야하는가
#         for number in range(1, M+1):
#             # 전에 나오는 수의 두배 혹은 두배 이상이 현재 수
#             for prev_number in range(1, number // 2 + 1):
#                 arr[number][index] += arr[prev_number][index-1]
#
#     for k in range(1, M+1):
#         if arr[k][N] > 0:
#             result += arr[k][N]
#
#     print(result)

arr = [[0 for _ in range(11)] for _ in range(2001)]
# 시작은 어떤 수든 올 수 있다고 치자
for k in range(1, 2001):
    arr[k][1] = 1
# 숫자가 몇번째인가?
for index in range(2, 11):
    # index번째의 어떤숫자를 확인해야하는가
    for number in range(1, 2001):
        arr[number][index] = 0
        # 전에 나오는 수의 두배 혹은 두배 이상이 현재 수
        for prev_number in range(1, number // 2 + 1):
            arr[number][index] += arr[prev_number][index - 1]

T = int(input())
for text_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 결과 값
    result = 0

    for k in range(1, M + 1):
        result += arr[k][N]

    print(result)