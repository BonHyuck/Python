T = int(input())
for test_case in range(1, T+1):
    H, W, N = map(int, input().split())
    cnt = 0
    height = 0
    width = 0
    for w in range(W):
        for h in range(H):
            cnt += 1
            if cnt == N:
                height = h
                width = w
                break
        if cnt == N:
            break

    height += 1
    width += 1
    result = str(height)
    if 0 < width < 10:
        width = '0'+str(width)
    else:
        width = str(width)
    print(result + width)