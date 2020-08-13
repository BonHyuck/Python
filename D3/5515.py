# SWEA 5515
# 요일 맞추기
T = int(input())
for test_case in range(1, T+1):
    # M = month, D = day
    M, D = map(int, input().split())
    # 며칠 지났는지 확인
    day_passed = 0

    for i in range(1, M):
        # 2월, 4월, 6월, 8월, 9월, 11월
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10:
            day_passed += 31
        # 2월 지나 3월까지
        elif i == 2:
            day_passed += 29
        else:
            day_passed += 30

    day_passed += (D - 1)

    day_number = 4 + day_passed % 7

    if day_number > 6:
        day_number -= 7

    print('#{} {}'.format(test_case, day_number))
