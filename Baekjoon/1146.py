# dp = [0 for _ in range(21)]
# dp[0] = 1
# dp[1] = 2
# for k in range(2, 21):
#     dp[k] = (dp[k-2] * dp[k-1])
#
# print(dp)
#
# N = int(input())
# print(dp[N])
# # 909568

from itertools import permutations, combinations
print(len(list(permutations([1], 1))))
print(len(list(permutations([1,2,], 2))))
print(len(list(permutations([1,2,3], 3))))
print(len(list(permutations([1,2,3,4], 4))))
print(len(list(permutations([1,2,3,4,5], 5))))


perm = [0 for _ in range(21)]
perm[0] = 1
perm[1] = 1
perm[2] = 2
for k in range(3, 21):
    perm[k] = perm[k-1] * k

print(perm)
print(perm[19])