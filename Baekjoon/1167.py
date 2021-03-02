def find_path(start, arr):
    for next, dist in box[start]:
        if arr[next] == -1:
            arr[next] = arr[start] + dist
            find_path(next, arr)

V = int(input())
# 1부터 시작하니까 V+1
box = [[] for _ in range(V+1)]
for v in range(V):
    input_list = list(map(int, input().split()))
    start = input_list.pop(0)
    while input_list:
        next = input_list.pop(0)
        if next == -1:
            break
        dist = input_list.pop(0)
        box[start].append((next, dist))

mid_result = [-1 for _ in range(V+1)]
mid_result[1] = 0
find_path(1, mid_result)

checker = 0
index = 0

for k in range(1, V+1):
    if mid_result[k] > checker:
        checker = mid_result[k]
        index = k

result = [-1 for _ in range(V+1)]
result[index] = 0
find_path(index, result)
print(max(result))


