'''
3
2 2
1 5
13 29

'''

box = [[0 for _ in range(31)] for _ in range(31)]
for r in range(1, 31):
    for c in range(1, 31):
        bottom = 1
        for number in range(1, r + 1):
            bottom *= number
        if r == 1:
            box[r][c] = c
        elif r == c:
            box[r][c] = 1
        elif r < c:
            top = 1
            for number in range(r):
                top *= (c - number)
            box[r][c] = top/bottom

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    print(int(box[N][M]))

