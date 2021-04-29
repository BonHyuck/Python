K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
start = 1
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    mid_result = 0
    for k in arr:
        mid_result += k // mid
    if mid_result >= N:
        if result < mid:
            result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
