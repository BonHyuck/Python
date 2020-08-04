# SWEA 2005
# 파스칼 삼각형 만들기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = int(input())
    triangle_list = []
    
    # 일단 주어진 삼각형 크기 잡기
    for i in range(1, number+1):
        triangle_list.append([1]*i)

    # 반복으로 중간에 있는 숫자 바꿔주기
    # 전후 리스트와 리스트의 index 파악
    for i in range(1, len(triangle_list) - 1):
        prev_list = triangle_list[i]
        next_list = triangle_list[i + 1]

        for j in range(1, len(prev_list)):
            next_list[j] = prev_list[j - 1] + prev_list[j]
    
    # 테스트 케이스 번호 우선 출력
    print('#{}'.format(test_case))

    # 리스트 전체 돌기
    for each_list in triangle_list:
        # 각 리스트내 요소들은 한 줄 출력
        for element in each_list:
            print(element, end=' ')
        # 엔터 한번 쳐주기
        print()