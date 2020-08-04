# SWEA 1926
# 369 게임
N = int(input())
numbers = list(map(str, range(1, N + 1)))
result = ''

for i in numbers:
    str_list = list(i)
    cnt = 0
    for k in str_list:
        if k == '3' or k == '6' or k == '9':
            cnt += 1

    if cnt >= 1:
        for j in range(0, cnt):
            result += '-'
    else:
        result += i

    result += ' '

print(result)