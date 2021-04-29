T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [i for i in range(N)]
    queue = list(map(int, input().split()))
    result = 0

    while queue:
        maximum = max(queue)
        priority = queue.pop(0)
        paper = arr.pop(0)
        if priority != maximum:
            queue.append(priority)
            arr.append(paper)
        else:
            result += 1
            if paper == M:
                break

    print(result)