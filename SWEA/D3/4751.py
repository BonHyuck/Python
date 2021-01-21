import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    text = list(input())
    num = 4 * len(text) + 1
    box = [[0 for _ in range(num)] for _ in range(5)]

    for i in range(5):
        for j in range(num):
            if i == 0 or i == 4:
                if j % 4 == 2:
                    box[i][j] = '#'
                else:
                    box[i][j] = '.'
            elif i == 1 or i == 3:
                if j % 2 == 1:
                    box[i][j] = '#'
                else:
                    box[i][j] = '.'
            else:
                if j % 4 == 0:
                    box[i][j] = '#'
                elif j % 4 == 2:
                    box[i][j] = text.pop(0)
                else:
                    box[i][j] = '.'

    for k in range(5):
        for l in range(num):
            print(box[k][l], end="")
        print()
