# SWEA 5215
# 햄버거 다이어트
T = int(input())
for test_case in range(1, T+1):
    # N = 가능한 재료의 개수
    # L = 최대 칼로리
    N, L = map(int, input().split())
    # 햄버거 재료의 정보를 담기 위한 리스트
    hamburgers = []
    for i in range(N):
        ingredient = list(map(int, input().split()))
        hamburgers.append(ingredient)
    # 가장 높은 점수
    maximum = 0
    # 초기 설정 끝

    # 재료들의 부분집합 구하기 2^N
    for i in range(1 << N):
        # 칼로리와 점수는 각 부분집합마다 구하기
        calorie = 0
        score = 0
        # 각 재료의 인덱스
        for j in range(N):
            # 해당 인덱스의 재료가 있는지 확인 : 없으면 0(False) 있으면 1 이상(True)
            if i & (1 << j):
                score += hamburgers[j][0]
                calorie += hamburgers[j][1]
        if calorie <= L and score > maximum:
            maximum = score

    print('#{} {}'.format(test_case, maximum))
