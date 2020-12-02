# SWEA 1859
# 사재기 최대값 도출
# import sys
# sys.stdin = open('input.txt', 'r')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 날짜 수 (배열의 크기)
    N = int(input())
    # 각 날짜의 가격
    price_list = list(map(int, input().split()))
    buy = 0
    sell = 0
    cnt = 0

    while True:
        max_index = price_list.index(max(price_list))
        buy += sum(price_list[0:max_index])
        sell += price_list[max_index] * max_index
        del price_list[0:max_index]
        if len(price_list) <= 1:
            break
        if max_index == 0:
            del price_list[0]
            continue

    result = sell - buy

    print('#{} {}'.format(test_case, result))
