N = int(input())
arr = list(map(int, input().split()))
primes = [1 for _ in range(1001)]
primes[0] = 0
primes[1] = 0
for index in range(2, 501):
    if primes[index] == 1:
        for k in range(2, 1001):
            if index != k and k % index == 0:
                primes[k] = 0

result = 0
for p in arr:
    if primes[p] == 1:
        result += 1
print(result)