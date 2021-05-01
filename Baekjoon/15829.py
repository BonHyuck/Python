N = int(input())
text = input()
total = 0
r = 31
M = 1234567891

for k in range(N):
    total += (ord(text[k]) - 96) * (r ** k)

print(total % M)
