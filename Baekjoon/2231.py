arr = [0 for _ in range(1000001)]

for number in range(1, 1000001):
    total = number
    for k in range(len(str(number))):
        total += int(str(number)[k])
    if total <= 1000000 and arr[total] == 0:
        arr[total] = number
print(arr[int(input())])