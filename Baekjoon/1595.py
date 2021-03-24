# Input이 몇번 들어올지 모르니까 그냥 필요한건 최대치로 만들어두기
distance = [[0 for _ in range(10001)] for _ in range(10001)]
visited = [0 for _ in range(10001)]

yes_input = True
while yes_input:
    try:
        # 시작, 끝, 거리
        S, E, D = map(int, input().split())

    except ValueError:
        yes_input = False

