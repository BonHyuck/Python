N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
houses = []
chicken = []
# 치킨집과 일반집 구분 => 배열에 넣기
for r in range(N):
    for c in range(N):
        if box[r][c] == 1:
            houses.append((r, c))
        elif box[r][c] == 2:
            chicken.append((r, c))

paths = []
# 집마다 모든 치킨집까지의 거리 정리
for (r, c) in houses:
    arr = []
    for (cr, cc) in chicken:
        arr.append(abs(r - cr) + abs(c - cc))
    paths.append(arr)

# 생존가능한 치킨집의 인덱스 조합
possible_chicken = []
# 부분집합 구하기 
for i in range(1 << len(chicken)):
    arr = []
    for j in range(len(chicken)):
        if i & (1 << j):
            arr.append(j)
    if len(arr) == M:
        possible_chicken.append(arr)

result = float('inf')

while possible_chicken:
    survive_chicken = possible_chicken.pop(0)
    mid_result = 0
    # 각 집마다 최소 거리 검사
    for path in paths:
        compare = 987654321
        for k in survive_chicken:
            if compare > path[k]:
                compare = path[k]
        mid_result += compare

    if result > mid_result:
        result = mid_result


print(result)


