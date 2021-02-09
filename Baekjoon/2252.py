'''
3 6
1 3
2 3
1 2
1 3
1 3
1 3

4 4
4 2
3 1
3 4
4 1
'''
N, M = map(int, input().split())
# box[index] = index 앞에 있는 숫자 배열
# index는 1부터 N까지이므로 (N+1)
box = [0 for _ in range(N+1)]
# 키 비교를 담을 세트 : 중복 제거용
heights = set()
for _ in range(M):
    front, back = map(int, input().split())
    heights.add((front, back))

# back은 front 포함, 앞에 있는 것들 보다 한칸이상 뒤에 있어야함
for front, back in heights:
    box[back] += (box[front] + 1)

# 가능성 추리기
length_list = sorted(list(set(box)))

result = []
# 순서대로
for length in length_list:
    for k in range(1, N+1):
        if box[k] == length:
            result.append(k)
    length += 1

print(*result)



#
# N, M = map(int, input().split())
# box = [set() for _ in range(N+1)]
# for _ in range(M):
#     front, back = map(int, input().split())
#     box[back].add(front)
#
# queue = []
# for k in range(1, N+1):
#     if box[k] == set():
#         box[k] = {0}
#         queue.append(k)
#
# while queue:
#     index = queue.pop(0)
#     for k in range(1, N+1):
#         if box[k] != set() and box[k] != {0}:
#             box[k].discard(index)
#         if box[k] == set():
#             box[k] = {0}
#             queue.append(k)
#     print(index, end=" ")

# N, M = map(int, input().split())
# # box[index] = index 앞에 있는 숫자 배열
# # index는 1부터 N까지이므로 (N+1)
# box = [set() for _ in range(N+1)]
# for _ in range(M):
#     front, back = map(int, input().split())
#     box[back].add(front)
# visited = [0 for _ in range(N+1)]
# queue = []
# for k in range(1, N+1):
#     if box[k] == set():
#         queue.append(k)
#         visited[k] = 1
#
# while queue:
#     index = queue.pop(0)
#     for k in range(1, N+1):
#         box[k].discard(index)
#         if box[k] == set() and visited[k] == 0:
#             visited[k] = 1
#             queue.append(k)
#     print(index, end=" ")

# length_list = sorted(list(set(box)))
# while length_list:
#     length = length_list.pop(0)
#     for k in range(1, N+1):
#         if length == box[k]:
#             print(k, end=' ')

# for length in length_list:
#
# result = []
# while length < N:
#     for k in range(1, N+1):
#         if box[k] == length:
#             print(k, end=' ')
#     length += 1
