A, B, V = map(int, input().split())
V -= A
result = V // (A-B) + 1
print(result)