N = int(input())
sang = list(map(int, input().split()))
dic = {}
for s in sang:
    dic[s] = dic.get(s, 0) + 1

M = int(input())
check = list(map(int, input().split()))
result = []
for number in check:
    result.append(dic.get(number, 0))
print(*result)