from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# arr = [i for i in range(100)]
result = 0
for one in list(combinations(arr, 3)):

    if result < sum(one) <= M:
        result = sum(one)
print(result)

