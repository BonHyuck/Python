X, Y = map(int, input().split())
first = 0
for k in range(1, min(X, Y) + 1):
    if X % k == 0 and Y % k == 0:
        first = k
second = first * (X // first) * (Y // first)
print(first)
print(second)