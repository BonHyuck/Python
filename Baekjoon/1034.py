# def switch_on(col, cnt, row_on, new_box):
#     global result
#     if cnt == K:
#         if result < row_on:
#             result = row_on
#         return
#
#     # 스위치 클릭
#     for row in range(N):
#         new_box[row][col] = 1 - new_box[row][col]
#
#     # 확인
#     mid_result = 0
#     for r in range(N):
#         if new_box[r].count(1) == M:
#             mid_result += 1
#
#     # 다음 클릭으로 넘어가기
#     for c in range(M):
#         switch_on(c, cnt + 1, mid_result, new_box)
#
#
# from copy import deepcopy
#
#
# N, M = map(int, input().split())
# box = [list(map(int, input())) for _ in range(N)]
# K = int(input())
# result = 0
#
# # 초기값 세팅
# for r in range(N):
#     if box[r].count(1) == M:
#         result += 1
#
#
# # 어떤 스위치를 누를것인가?
# for c in range(M):
#     # 스위치 위치, 누른 횟수, 켜진 행
#     arr = deepcopy(box)
#     switch_on(c, 0, result, arr)
#
# print(result)

N, M = map(int, input().split())
box = [list(map(int, input())) for _ in range(N)]
K = int(input())
result = 0
# 각 행 탐색 시작
for row in range(N):
    # 행의 0의 개수
    zeros = 0
    # 열을 확인하면서
    for col in range(M):
        # 0의 개수 세기
        if box[row][col] == 0:
            zeros += 1
    # 행의 결과 값
    cnt = 0
    # 0의 개수가 K보다 작고 (행을 켤 수 있음) && On?Off 를 반복하면서 결과적으로 행을 켤 수 있음
    if zeros <= K and zeros % 2 == K % 2:
        # 다른 행도 같은 패턴을 갖는지 확인
        for r in range(N):
            if box[row] == box[r]:
                cnt += 1
    result = max(result, cnt)
print(result)