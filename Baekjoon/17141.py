from itertools import combinations
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_virus(arr):
    # 큐 세팅
    queue = [arr]
    cnt = 0
    # 큐가 있는 동안 반복
    while queue:
        # 시작하자마자 시간을 1 추가한다.
        cnt += 1
        next_list = queue.pop(0)
        mini_queue = []
        for r, c in next_list:
            for k in range(4):
                new_r = r + dx[k]
                new_c = c + dy[k]
                # 인덱스 확인
                if 0 <= new_r < N and 0 <= new_c < N:
                    if new_box[new_r][new_c] == 0:
                        new_box[new_r][new_c] = 2
                        mini_queue.append((new_r, new_c))
        if len(mini_queue):
            queue.append(mini_queue)

    # 전부 퍼트렸는지 확인
    for i in range(N):
        for j in range(N):
            # 1곳이라도 안 퍼졌으면
            if new_box[i][j] == 0:
                # 최소값 출력을 막기위해 큰 수로 설정
                cnt = 987654321
                break
        if cnt == 987654321:
            break
    # 결과값 리턴
    return cnt



# N, M = 연구소 크기, 바이러스 개수
N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
# 바이러스를 놓을 수 있는 모든 자리
virus_possible = []
for r in range(N):
    for c in range(N):
        if box[r][c] == 2:
            virus_possible.append((r, c))

# 경우의 수 추려내기
virus_combs = list(combinations(virus_possible, M))
# 최대한 빨리 = 시간의 최소값 => 일단 큰 수로 지정하여 시작
result = 987654321
# 경우의 수 반복
for virus in virus_combs:
    new_box = deepcopy(box)
    # 일단 바이러스를 놓을 수 있는 모든 구역을 빈칸화한다.
    for r, c in virus_possible:
        new_box[r][c] = 0
    # 이후 경우의 수에 있는 좌표만 바이러스 배치
    for virus_r, virus_c in virus:
        new_box[virus_r][virus_c] = 2
    # 작업이 끝나면 최소값을 결과값으로 넣는다.
    result = min(result, find_virus(virus))

if result == 987654321:
    print(-1)
else:
    print(result-1)