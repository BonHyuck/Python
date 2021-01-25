

# 9876543210 = 마지막 수
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start_number = 1
while start_number < 10:
    for i in range(1, start_number+1):
        result_number = start_number * (10 ** i)
        for k in arr:
            if len(str(k))+1 == len(str(result_number)) and result_number // 10 > k:
                result_number += k
                arr.append(result_number)
                result_number -= k
    start_number += 1

arr.sort()

# N번째 감소하는 수
N = int(input())
if len(arr) <= N:
    print(-1)
else:
    print(arr[N])
