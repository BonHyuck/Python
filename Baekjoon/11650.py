N = int(input())
arr = [[] for _ in range(200001)]

for k in range(N):
    x, y = map(int, input().split())
    arr[x + 100000].append(y)

answer = []
for X in range(200001):
    if len(arr[X]) > 0:
        for Y in sorted(arr[X]):
            answer.append((X - 100000, Y))

for k in answer:
    print(*k)