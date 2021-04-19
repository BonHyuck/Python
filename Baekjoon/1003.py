# T = int(input())
#
# fibo = [0, 1]
#
# def fibonacci(n):
#     global one, zero
#     if len(fibo) > n:
#         if n == 0:
#             zero += 1
#         elif n == 1:
#             one += 1
#         return fibo[n]
#     else:
#         fibo.append(fibonacci(n-1) + fibonacci(n-2))
#         return fibo[n-1] + fibo[n-2]
#
#
# for test_case in range(1, T+1):
#     number = int(input())
#     one = 0
#     zero = 0
#     fibonacci(number)
#     print(zero, one)
#
# T = int(input())
#
# def fibonacci(n):
#     global one, zero
#     if n == 0:
#         zero += 1
#         return 0
#     elif n == 1:
#         one += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for test_case in range(1, T+1):
#     number = int(input())
#     one = 0
#     zero = 0
#     fibonacci(number)
#     print(zero, one)

fibo = [0 for _ in range(45)]
fibo[0] = 0
fibo[1] = 1
index = 2
while index < 45:
     fibo[index] = fibo[index-1] + fibo[index-2]
     index += 1

T = int(input())
for test_case in range(1, T+1):
    number = int(input())
    fibo[-1] = 1

    print('{} {}'.format(fibo[number-1], fibo[number]))