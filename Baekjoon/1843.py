# from itertools import combinations, combinations_with_replacement
#
# # 입력값
# N = int(input())
# arr = [i for i in range(1, N+1)]
# A = 0
# B = 0
# C = 0
#
# # 제약 조건 A
# # 조합을 구하고 맞는 것만 세기
# # comb = [X, Y, Z]
# comb_A = combinations(arr, 3)
# for X, Y, Z in list(comb_A):
#     # 기본 조건 + 제약조건 A
#     if X + Y == Z and X != Y and Y != Z and Z != X:
#         A += 1
#
# print(A)
#
# # 약수를 담을 배열
# divisor = []
# for k in arr:
#     if N % k == 0:
#         divisor.append(k)
#
# # 중복 가능 조합
# comb_B = combinations_with_replacement(divisor, 3)
# for X, Y, Z in list(comb_B):
#     # 이미 약수로만 이뤄졌기때문에 기본 조건만 확인한다.
#     if X + Y == Z:
#         B += 1
# print(B)
#
# # 소수 기본 배열
# prime = [2, 3, 5]
#
# for k in range(6, N+1):
#     is_prime = True
#     for p in prime:
#         if k % p == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime.append(k)
#
# comb_C = combinations_with_replacement(prime, 3)
# for X, Y, Z in list(comb_C):
#     # 이미 소수로만 이뤄졌기때문에 기본 조건만 확인한다.
#     if X + Y == Z:
#         C += 1
#
# print(C)
#

# 입력값
N = int(input())
arr = [i for i in range(1, N+1)]
A = 0
B = 0
C = 0

# 제약 조건 A : 세 자연수 X, Y, Z는 모두 N 이하이며, 서로 다르다.
# X = 1이면 Y = 2, 3, ... N - 1 까지 가능 (앞뒤로 1개씩 빠짐)
# X = 2이면 Y = 3, 4, ... N - 2 까지 가능 (앞뒤로 2개씩 빠짐)
# X는 배열의 중간값까지 가능
# N = 6일때 X는 2까지 가능하다
# N = 7일때는 3까지 가능
for X in range(1, ((N // 2) + N % 2)):
    A += (N - (2 * X))
print(A)

# 제약 조건 B: 세 자연수 X, Y, Z는 모두 N의 양의 약수이다.
divisor = []
# 약수 구하기
for k in arr:
    if N % k == 0:
        divisor.append(k)

for xndex in range(len(divisor)):
    for yndex in range(xndex, len(divisor)):
        if (divisor[xndex] + divisor[yndex]) <= N and N % (divisor[xndex] + divisor[yndex]) == 0:
            B += 1
print(B)

# 제약 조건 C: 세 자연수 X, Y, Z는 모두 N 이하의 양의 소수이다.
# # 3개는 미리 넣어둠
# primes = [2, 3, 5]
# # 소수 구하기
# for k in range(6, N):
#     is_prime = True
#     for p in primes:
#         if k % p == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(k)
# 위의 방법으로 실행했더니 시간이 너무 오래걸린다...

prime_checker = [0 for _ in range(N+1)]
# 혹시 몰라서 0, 1은 확인 처리
prime_checker[0] = 1
prime_checker[1] = 1
# 소수를 넣을 배열
primes = []

# 2부터 시작
for k in range(2, N+1):
    # 아직 체크 안함
    if prime_checker[k] == 0:
        for adios in range(k, N + 1, k):
            prime_checker[adios] = 1
        prime_checker[k] = 0
        primes.append(k)

# 2를 제외한 소수는 홀수
# 홀수 + 홀수는 짝수
# 짝수는 2의 배수 = 소수 아님
# X는 무조건 2
for k in primes:
    if k + 2 <= N and prime_checker[k + 2] == 0:
        C += 1
print(C)




