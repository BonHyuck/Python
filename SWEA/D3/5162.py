import sys
sys.stdin = open('input.txt', 'r')

# def find_bread(total, money):
#     global result
#
#     if money < 0:
#         return
#
#     for m in [A, B]:
#         if money - m >= 0:
#             find_bread(total + 1, money - m)
#
#     if result < total:
#         result = total
#
#     return
#
# T = int(input())
# for test_case in range(1, T+1):
#     A, B, C = map(int, input().split())
#     result = 0
#
#     find_bread(0, C)
#
#     print('#{} {}'.format(test_case, result))

T = int(input())
for test_case in range(1, T+1):
    A, B, C = map(int, input().split())
    money = 0
    if A >=B :
        money = B
    else:
        money = A

    result = -1

    while C >= 0:
        C -= money
        result += 1

    print('#{} {}'.format(test_case, result))