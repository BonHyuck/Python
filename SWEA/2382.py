import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    status = [list(map(int, input().split())) for _ in range(K)]

    for i in range(M):
        cell = [[0] * N for _ in range(N)]
        check = len(status)
        for i in range(check):
            micro = status.pop(0)
            r, c = micro[0], micro[1]
            if micro[3] == 1:
                r -= 1
            elif micro[3] == 2:
                r += 1
            elif micro[3] == 3:
                c -= 1
            else:
                c += 1

            if r == 0:
                micro[3] = 2
                micro[2] //= 2
            elif c == 0:
                micro[3] = 4
                micro[2] //= 2
            elif r == N - 1:
                micro[3] = 1
                micro[2] //= 2
            elif c == N - 1:
                micro[3] = 3
                micro[2] //= 2

            if cell[r][c] == 0:
                cell[r][c] = [micro[2], [micro[2], micro[3]]]
            else:
                if cell[r][c][1][0] < micro[2]:
                    cell[r][c][1][0] = micro[2]
                    cell[r][c][1][1] = micro[3]
                cell[r][c][0] += micro[2]

        for j in range(len(cell)):
            for k in range(len(cell[j])):
                if cell[j][k]:
                    status.append([j, k, cell[j][k][0], cell[j][k][1][1]])
    ans = 0
    for row in status:
        ans += row[2]
    print('#{} {}'.format(tc, ans))



'''
1. 이동 전 배열과 이동 후 배열을 이용해 군집의 배치를 표시한다.
2. M 시간 동안 군집을 이동시킨다.
매 시간 빈 배열을 만들어서 군집을 이동시킨 후 기록한다.
'''