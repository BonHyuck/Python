# 10 x 10 크기의 종이
box = [list(map(int, input().split())) for _ in range(10)]
# 1 x 1 ~ 5 x 5
paper = [0, 5, 5, 5, 5, 5]
result = 0

# 10 x 10 색종이 탐색하며 1 찾기
for N in range(5, 0, -1):
    for i in range(10):
        for j in range(10):
            if box[i][j] == 1:
                cover = True
                for k in range(N):
                    for l in range(N):
                        if paper[N] < 1 or i + k >= 10 or j + l >= 10 or box[i + k][j + l] == 0:
                            cover = False
                            break
                    if not cover:
                        break
                if cover:
                    result += 1
                    paper[N] -= 1
                    for k in range(N):
                        for l in range(N):
                            box[i + k][j + l] = 0

for i in range(10):
    if box[i].count(1) > 0:
        result = -1
        break

print(result)