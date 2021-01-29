'''
2
3 2 1
1 2
2 3
2
5 3 1
1 2
1 3
1 4
2

'''


T = int(input())
for test_case in range(1, T+1):
    # n개의 도미노 타일 : 1 ~ n 까지
    # m개의 숫자쌍, (x, y) : x 가 넘어지면 y 도 넘어진다
    # l개의 숫자, z : z를 손으로 넘어트린다.
    # 넘어진 도미노의 개수
    N, M, L = map(int, input().split())

    # 0: 안넘어진 도미노, 1: 넘어진 도미노, index: 도미노 번호
    domino = [0 for _ in range(N+1)]

    fall_dict = {}

    # m개의 숫자쌍
    for m in range(M):
        x, y = map(int, input().split())
        fall_dict[x] = fall_dict.get(x, [])
        fall_dict[x].append(y)

    fall_queue = []

    # 넘기기 시작
    for l in range(L):
        z = int(input())
        fall_queue.append(z)
        # queue에 내용이 있을 때만
        while fall_queue:
            # 넘어지는 도미노
            fall_domino = fall_queue.pop(0)
            # 아직 안넘어감
            if domino[fall_domino] == 0:
                domino[fall_domino] = 1
                # 다음에 넘어질 것들이 뒤에 붙는다.
                fall_queue.extend(fall_dict.get(fall_domino, []))

    print(domino.count(1))
