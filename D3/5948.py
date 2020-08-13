# SWEA 5948
# 7-3-5 게임
T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    # 합을 담기 위한 리스트
    total = []

    # 부분집합 구하기
    for i in range(1 << len(numbers)):
        arr = []
        for j in range(len(numbers)):
            if i & (1 << j):
                arr.append(numbers[j])
                if len(arr) == 3:
                    if sum(arr) not in total:
                        total.append(sum(arr))
                    continue

    print('#{} {}'.format(test_case, sorted(total, reverse=True)[4]))
