from collections import deque

N = int(input())
arr = deque([i for i in range(1, N+1)])

while len(arr) > 1:
    arr.popleft()
    number = arr.popleft()
    arr.append(number)
print(*arr)


'''
1
2
2
4
2
4
6
8
475712
'''