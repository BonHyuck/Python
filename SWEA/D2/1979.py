# SWEA 1979
# 주어진 낱말 퍼즐 내 주어진 글자수의 낱말 갯수 찾기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 주어진 낱말 퍼즐 크기와 글자수 받기
    N, K = map(int, input().split())
    # 결과를 담을 변수
    result = 0
    # 낱말 퍼즐 배열
    square_list = []

    for i in range(0, N):
        square_list.append(list(map(int, input().split())))
    
    # 가로 확인
    for i in range(0, N):
        # 가로 줄의 가능 글자 수
        garo = 0
        # 세로 줄의 가능 글자 수
        sero = 0
        for j in range(0, N):
            # 가로 확인
            if square_list[i][j] == 1:
                garo += 1
            if square_list[i][j] == 0:
                if garo == K:
                    result += 1
                garo = 0

            # 세로 확인
            if square_list[j][i] == 1:
                sero += 1
            if square_list[j][i] == 0:
                if sero == K:
                    result += 1
                sero = 0

            if j == N-1:
                if garo == K:
                    result += 1
                if sero == K:
                    result += 1
                garo = 0
                sero = 0

    print('#{} {}'.format(test_case, result))