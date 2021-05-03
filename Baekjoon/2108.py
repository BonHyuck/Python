N = int(input())
arr = sorted([int(input()) for _ in range(N)])
count_arr = [[] for _ in range(N+1)]
for k in set(arr):
    count_arr[arr.count(k)].append(k)

result = 0
for index in range(N, -1, -1):
    if len(count_arr[index]) > 0:
        if len(count_arr[index]) > 1:
            result = sorted(count_arr[index])[1]
        else:
            result = sorted(count_arr[index])[0]
        break

print(sum(arr)//len(arr))
print(arr[len(arr)//2])
print(result)
print(max(arr) - min(arr))
