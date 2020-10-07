"""
풀긴 풀었으나 다른 사람의 코드를 참고해서 풀었다...
아무래도 아직은 재귀를 100% 활용하지는 못하는 것 같다.
풀이도 한 번에 안 떠올랐기 때문에 아직은 연습이 많이 필요하다.
종이에 작성하면서 알고리즘 설계하는 것을 우선 연습해야겠다.
"""

# paper_count = 사용한 종이의 개수
# left = 남은 개수
def start_cover(paper_count, left):
    global min_paper
    # 전부 다 덮음
    if left == 0:
        if paper_count < min_paper:
            min_paper = paper_count
        return
    # 최소 개수 넘음
    elif paper_count >= min_paper:
        return
    # 종이 다 씀
    elif sum(papers) == 0:
        return
    else:
        for i in range(10):
            for j in range(10):
                # 덮는 부분의 왼쪽 모서리이며 아직 방문하지 않음
                if box[i][j] == 1 and visited[i][j] == 0:
                    # 큰 종이부터 확인
                    for k in range(5, 0, -1):
                        # 종이가 남아있고 인덱스 에러 없음
                        if papers[k] > 0 and i + k <= 10 and j + k <= 10:
                            # 덮을 수 있는 영역
                            cover = 0
                            for row in range(i, i + k):
                                for col in range(j, j + k):
                                    # 아직 안 덮힘
                                    if visited[row][col] == 0:
                                        cover += box[row][col]
                            # k x k 영역 덮기 성공
                            if cover == (k * k):
                                # 다 덮었다!
                                for row in range(i, i + k):
                                    for col in range(j, j + k):
                                        visited[row][col] = 1
                                papers[k] -= 1
                                start_cover(paper_count+1, left - cover)
                                # 해당 종이로 안 덮고 다른 종이로 덮는 경우
                                for row in range(i, i + k):
                                    for col in range(j, j + k):
                                        visited[row][col] = 0
                                papers[k] += 1
                    return


# 10 x 10 크기의 종이
box = [list(map(int, input().split())) for _ in range(10)]
visited = [[0 for _ in range(10)] for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
# 몇개나 덮어야 되는가
counter = 0
# 사용한 종이 개수의 최소값
min_paper = 26
for i in range(10):
    for j in range(10):
        if box[i][j] == 1:
            counter += 1

start_cover(0, counter)

if min_paper >= 26:
    min_paper = -1

print(min_paper)


'''
결과 : 틀렸습니다.
무조건 큰 타일을 먼저 붙이는 것이 최소값은 아닌 것 같다...
'''
# 10 x 10 크기의 종이
# box = [list(map(int, input().split())) for _ in range(10)]
# 1 x 1 ~ 5 x 5
# paper = [0, 5, 5, 5, 5, 5]
# result = 0
#
# # 10 x 10 색종이 탐색하며 1 찾기
# for N in range(5, 0, -1):
#     for i in range(10):
#         for j in range(10):
#             if box[i][j] == 1:
#                 cover = True
#                 for k in range(N):
#                     for l in range(N):
#                         if paper[N] < 1 or i + k >= 10 or j + l >= 10 or box[i + k][j + l] == 0:
#                             cover = False
#                             break
#                     if not cover:
#                         break
#                 if cover:
#                     result += 1
#                     paper[N] -= 1
#                     for k in range(N):
#                         for l in range(N):
#                             box[i + k][j + l] = 0
#
# for i in range(10):
#     if box[i].count(1) > 0:
#         result = -1
#         break
#
# print(result)