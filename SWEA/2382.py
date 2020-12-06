'''
1. 이동 전 배열과 이동 후 배열을 이용해 군집의 배치를 표시한다.
2. M 시간 동안 군집을 이동시킨다.
매 시간 빈 배열을 만들어서 군집을 이동시킨 후 기록한다.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 개수 받기
T = int(input())
for test_case in range(1, T+1):
    # N : 정사각형 규역 한 변의 크기
    # M : 경과 시간
    # K : 미생물 군집의 개수
    N, M, K = map(int, input().split())
    # 미생물 배열
    # 행, 열, 개수, 방향
    micro = [tuple(map(int, input().split())) for _ in range(K)]
    
    # 주어진 시간만큼만 반복
    for i in range(M):
        # 현재 미생물의 군집만큼만 반복해야한다.
        loop_length = len(micro)
        # 확인을 위한 배열
        box = [[0 for _ in range(N)] for _ in range(N)]
        # 미생물 움직임 시작
        for j in range(loop_length):
            # 행, 열, 개수, 방향
            r, c, n, d = micro.pop(0)
            # 이동 방향에 따른 위치 조정
            # 상
            if d == 1:
                r -= 1
            # 하
            elif d == 2:
                r += 1
            # 좌
            elif d == 3:
                c -= 1
            # 우
            elif d == 4:
                c += 1

            # 구역의 모서리(약품이 있는 곳)에 도달
            if r == 0 or r == N - 1 or c == 0 or c == N - 1:
                # 개수가 절반으로 줄어든다.
                n = n // 2
                # 방향 변경
                if d % 2 == 1:
                    d += 1
                else:
                    d -= 1

            # 확인을 위한 영역이 비어있음
            if box[r][c] == 0:
                # 총합, 제일 큰 군집 내 미생물 수, 해당 군집의 방향
                box[r][c] = [n, n, d]
            # 이미 자리하고 있는 군집이 있다.
            # 합쳐야한다.
            else:
                # 현재 제일 큰 군집과 진입한 군집 비교
                # 일단 총합 변경
                box[r][c][0] += n
                # 진입하는 군집이 더 크다면
                if box[r][c][1] < n:
                    # 대표 군집의 수 변경
                    box[r][c][1] = n
                    # 방향변경
                    box[r][c][2] = d
        
        # 위의 반복이 끝난후 박스 확인
        for r in range(N):
            for c in range(N):
                # 미생물 군집 존재
                if box[r][c] != 0:
                    # 현재 행, 현재 열, 총합, 방향
                    micro.append((r, c, box[r][c][0], box[r][c][2]))

    # 결과를 담을 변수
    result = 0

    for r, c, n, d in micro:
        result += n

    print('#{} {}'.format(test_case, result))



