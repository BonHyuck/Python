'''
9
###.###.###.###.###.###.###.###.###
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.###.###.###.###.###.###.###.###
#.#...#...#...#...#...#...#...#...#
###.###.###.###.###.###.###.###.###

9
...................................
...................................
...................................
...................................
...................................

6
.......................
.......................
.......................
.......................
.......................
5
...................
...................
...................
...................
...................
'''

'''
512
253155555072
494444443.5
'''
N = int(input())
arr = [list(map(str, input())) for _ in range(5)]
box = []
for i in range(N):
    temp = []
    for c in range(5):
        temp.append(arr[c][4*i:4*i+3])
    box.append(temp)
# 각 칸별로 가능한 숫자의 배열
# index = 칸
numbers = []
result = 0
# 0 ~ 9까지 모두 가능하다고 가정
possible = [1 for _ in range(10)]
# 각 칸별로 가능한 번호 추출
for text in box:
    # 켜져있으면 안되는 칸 미리 걸러내기
    if text[1][1] == '#' or text[3][1] == '#':
        result = -1
        break
    # 특정한 곳이 켜져있으면 형성이 안되는 번호 걸러내기
    if text[0][0] == "#":
        possible[1] = 0
    if text[0][1] == '#':
        possible[1] = 0
        possible[4] = 0
    if text[1][0] == '#':
        possible[1] = 0
        possible[2] = 0
        possible[3] = 0
        possible[7] = 0
    if text[1][2] == '#':
        possible[5] = 0
        possible[6] = 0
    if text[2][0] == '#':
        possible[1] = 0
        possible[7] = 0
    if text[2][1] == '#':
        possible[0] = 0
        possible[1] = 0
        possible[7] = 0
    if text[3][0] == '#':
        possible[1] = 0
        possible[3] = 0
        possible[4] = 0
        possible[5] = 0
        possible[7] = 0
        possible[9] = 0
    if text[3][2] == '#':
        possible[2] = 0
    if text[4][0] == '#':
        possible[1] = 0
        possible[4] = 0
        possible[7] = 0
    if text[4][1] == '#':
        possible[1] = 0
        possible[4] = 0
        possible[7] = 0
    temp = []
    # 위의 절차를 거치고 가능한 숫자만 배열에 넣기
    for p in range(10):
        if possible[p] == 1:
            temp.append(p)
        possible[p] = 1
    numbers.append(temp)

if result != -1:
    result_length = 1
    result_total = 0

    for index in range(N):
        result_total += result_total * (len(numbers[index]) - 1)
        for number in numbers[index]:
            result_total += (number * (10 ** (N - 1 - index)) * result_length)
        result_length *= len(numbers[index])
    print(result_total/result_length)
else:
    print(result)

# def start_find(index, made_text):
#     global result_length, result_total
#     if index == N:
#         result_length += 1
#         result_total += int(made_text)
#         return
#
#     for n in numbers[index]:
#         start_find(index + 1, made_text + str(n))
#
#
# N = int(input())
# arr = [list(map(str, input())) for _ in range(5)]
# box = []
# for i in range(N):
#     temp = []
#     for c in range(5):
#         temp.append(arr[c][4*i:4*i+3])
#     box.append(temp)
# # 각 칸별로 가능한 숫자의 배열
# # index = 칸
# numbers = []
# result = 0
# # 0 ~ 9까지 모두 가능하다고 가정
# possible = [1 for _ in range(10)]
# # 각 칸별로 가능한 번호 추출
# for text in box:
#     # 켜져있으면 안되는 칸 미리 걸러내기
#     if text[1][1] == '#' or text[3][1] == '#':
#         result = -1
#         break
#     # 특정한 곳이 켜져있으면 형성이 안되는 번호 걸러내기
#     if text[0][0] == "#":
#         possible[1] = 0
#     if text[0][1] == '#':
#         possible[1] = 0
#         possible[4] = 0
#     if text[1][0] == '#':
#         possible[1] = 0
#         possible[2] = 0
#         possible[3] = 0
#         possible[7] = 0
#     if text[1][2] == '#':
#         possible[5] = 0
#         possible[6] = 0
#     if text[2][0] == '#':
#         possible[1] = 0
#         possible[7] = 0
#     if text[2][1] == '#':
#         possible[0] = 0
#         possible[1] = 0
#         possible[7] = 0
#     if text[3][0] == '#':
#         possible[1] = 0
#         possible[3] = 0
#         possible[4] = 0
#         possible[5] = 0
#         possible[7] = 0
#         possible[9] = 0
#     if text[3][2] == '#':
#         possible[2] = 0
#     if text[4][0] == '#':
#         possible[1] = 0
#         possible[4] = 0
#         possible[7] = 0
#     if text[4][1] == '#':
#         possible[1] = 0
#         possible[4] = 0
#         possible[7] = 0
#     temp = []
#     # 위의 절차를 거치고 가능한 숫자만 배열에 넣기
#     for p in range(10):
#         if possible[p] == 1:
#             temp.append(p)
#         possible[p] = 1
#     numbers.append(temp)
#
# if result != -1:
#     result_length = 0
#     result_total = 0
#     start_find(0, '')
#     print(result_length)
#     print(result_total)
#     print(result_total/result_length)
# else:
#     print(result)