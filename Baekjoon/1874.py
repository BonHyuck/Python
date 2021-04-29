'''
8
4
3
6
8
7
5
2
1

5
1
2
5
3
4
'''

N = int(input())
arr = [int(input()) for _ in range(N)]
result = []
stack = []
index = 0

for k in range(1, N+1):
    stack.append(k)
    result.append('+')

    while len(stack) > 0 and stack[-1] == arr[index]:
        stack.pop(-1)
        result.append('-')
        index += 1

if len(stack) > 0:
    print('NO')
else:
    for k in result:
        print(k)