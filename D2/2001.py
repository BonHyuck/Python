T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N * N 사각형 내 M * M의 파리채
    N, M = map(int, input().split())
    # 배열로 받기
    square_list = []
    # 결과 값
    result = 0

    # 사각형으로 만들기
    for i in range(0, N):
        new_list = list(map(int, input().split()))
        square_list.append(new_list)
    # 비교를 위한 값
    sample = 0
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1): # 여기까지가 시작점 잡기
            # start_point = square_list[i][j]
            for k in range(0, M):
                for l in range(0, M):
                    sample += square_list[i + k][j + l]

            if sample > result:
                result = sample
            sample = 0

    print('#{} {}'.format(test_case, result))



