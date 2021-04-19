dp = [0 for _ in range(101)]
dp[0] = 1
dp[1] = 2
for k in range(2, 101):
    dp[k] = (dp[k-2] * dp[k-1]) % 1000000

print(dp)

N = int(input())
# print(dp[N])
# 909568