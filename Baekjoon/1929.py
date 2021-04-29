M, N = map(int, input().split())
arr = [0 for _ in range(1000001)]
arr[0] = 1
arr[1] = 1
for k in range(2, 500001):
    if arr[k] == 0:
        for index in range(k * 2, 1000001, k):
            arr[index] = 1

for k in range(M, N+1):
    if arr[k] == 0:
        print(k)
