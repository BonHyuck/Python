N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
answer = []
index = 0
while arr:
    index = (index + K - 1) % len(arr)
    answer.append(arr.pop(index))
print('<', end='')
print(', '.join(map(str, answer)), end='')
print('>')