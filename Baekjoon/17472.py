# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # 섬들 번호 부여하기
# def label_island(row, col):
#     visited[row][col] = 1
#     box[row][col] = label
#     for k in range(4):
#         new_r = row + dr[k]
#         new_c = col + dc[k]
#         # 인덱스 검사
#         if 0 <= new_r < N and 0 <= new_c < M:
#             if box[new_r][new_c] > 0 and visited[new_r][new_c] == 0:
#                 label_island(new_r, new_c)
#
#     return
#
# def start_bridge(row, col):
#     # 방향 설정
#     for k in range(4):
#         # 다리의 시작길이
#         steps = 1
#         # 한방향으로 계속 나아가본다.
#         while True:
#             new_r = row + (dr[k] * steps)
#             new_c = col + (dc[k] * steps)
#             # 인덱스 체크
#             if 0 <= new_r < N and 0 <= new_c < M:
#                 # 0이면 계속 뻗어나간다.
#                 if box[new_r][new_c] == 0:
#                     steps += 1
#                     continue
#                 # 시작 위치와 같다면 = 같은 섬
#                 elif box[new_r][new_c] == box[row][col]:
#                     break
#                 # 다른 섬에 도달
#                 elif box[new_r][new_c] > 0:
#                     distance.append(steps-1)
#                     path[steps-1] = path.get(steps-1, [])
#                     path[steps-1].append((box[row][col], box[new_r][new_c]))
#                     break
#             # 인덱스 벗어나면 반복문 끝
#             else:
#                 break
#
#
# N, M = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0 for _ in range(M)] for _ in range(N)]
# label = 1
# for r in range(N):
#     for c in range(M):
#         if box[r][c] == 1 and visited[r][c] == 0:
#             label_island(r, c)
#             label += 1
#
# # 가능한 다리 정보를 담을 딕셔너리
# path = {}
# # 가능한 다리의 길이를 담을 배열
# distance = []
# for r in range(N):
#     for c in range(M):
#         if box[r][c] > 0:
#             start_bridge(r, c)
#
# distance = sorted(list(set(distance)))
#
# connection = [0 for _ in range(label+1)]
# connection[0] = 1
#
# result = 0
# # 짧은 거리의 다리부터 연결해본다.
# for dist in distance:
#     if dist < 2:
#         continue
#     # 전부 연결돼있다.
#     if connection.count(1) == len(connection):
#         break
#     arr = path.get(dist, [])
#     while arr:
#         start, end = arr.pop(0)
#         # 이미 연결된 섬
#         if connection[start] == 1 and connection[end] == 1:
#             continue
#         # 둘 중 하나라도 연결 안됨
#         else:
#             connection[start] =1
#             connection[end] = 1
#             result += dist
#
# if result == 0:
#     print(-1)
# else:
#     print(result)


'''
7 8
0 0 0 1 1 0 0 0
0 0 0 1 1 0 0 0
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 섬들 번호 부여하기
def label_island(row, col):
    visited[row][col] = 1
    box[row][col] = label
    for k in range(4):
        new_r = row + dr[k]
        new_c = col + dc[k]
        # 인덱스 검사
        if 0 <= new_r < N and 0 <= new_c < M:
            if box[new_r][new_c] > 0 and visited[new_r][new_c] == 0:
                label_island(new_r, new_c)

    return

def start_bridge(row, col):
    # 방향 설정
    for k in range(4):
        # 다리의 시작길이
        steps = 1
        # 한방향으로 계속 나아가본다.
        while True:
            new_r = row + (dr[k] * steps)
            new_c = col + (dc[k] * steps)
            # 인덱스 체크
            if 0 <= new_r < N and 0 <= new_c < M:
                # 0이면 계속 뻗어나간다.
                if box[new_r][new_c] == 0:
                    steps += 1
                    continue
                # 시작 위치와 같다면 = 같은 섬
                elif box[new_r][new_c] == box[row][col]:
                    break
                # 다른 섬에 도달
                elif box[new_r][new_c] > 0:
                    distance.append(steps-1)
                    path[steps-1] = path.get(steps-1, [])
                    path[steps-1].append(tuple(sorted((box[row][col], box[new_r][new_c]))))
                    break
            # 인덱스 벗어나면 반복문 끝
            else:
                break


N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
label = 1
for r in range(N):
    for c in range(M):
        if box[r][c] == 1 and visited[r][c] == 0:
            label_island(r, c)
            label += 1

# 가능한 다리 정보를 담을 딕셔너리
path = {}
# 가능한 다리의 길이를 담을 배열
distance = []
for r in range(N):
    for c in range(M):
        if box[r][c] > 0:
            start_bridge(r, c)

distance = sorted(list(set(distance)))

connection = [i for i in range(label+1)]

result = 0
# 짧은 거리의 다리부터 연결해본다.
for dist in distance:
    if dist < 2:
        continue
    arr = list(set(path.get(dist, [])))
    print(dist, arr)
    while arr:
        start, end = arr.pop(0)
        # 이미 연결된 섬
        if connection[start] ==  connection[end]:
            continue
        # 둘 중 하나라도 연결 안됨
        else:


print(distance)



if result == 0:
    print(-1)
else:
    print(result)