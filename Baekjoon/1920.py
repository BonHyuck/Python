N = int(input())
arr = list(map(int, input().split()))
dic = {}
for number in arr:
    dic[number] = 1
M = int(input())
check = list(map(int, input().split()))
for c in check:
    print(dic.get(c, 0))