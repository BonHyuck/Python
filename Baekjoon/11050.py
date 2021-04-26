memo = [0 for _ in range(11)]
memo[0] = memo[1] = 1

def facto(n):
    memo[n] = memo[n-1] * n
    return

for number in range(2, 11):
    facto(number)

N, K = map(int, input().split())
print(int(memo[N] / (memo[N-K]*memo[K])))
