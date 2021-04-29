N = int(input())
arr = sorted([int(input()) for _ in range(N)])
print(sum(arr)//len(arr))
print(arr[len(arr)//2])
