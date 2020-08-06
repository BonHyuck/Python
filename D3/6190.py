# SWEA 6190
# 숫자의 곱이 단조인지 확인하기
##################
#    틀린 코드    #
##################
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    maximum = -1

    for index in range(0, N-1):
        for jndex in range(index+1, N):
            result = numbers[index] * numbers[jndex]
            ascending = True
            for i in range(0, len(str(result))-1):
                if int(str(result)[i]) > int(str(result)[i+1]):
                    ascending = False
                    break
            if ascending and result > maximum:
                maximum = result

    print('#{} {}'.format(test_case, maximum))


##################
#    맞은 코드    #
##################

def find_number(input_list):
    result_list = []

    for index in range(len(input_list)-1, 0, -1):
        for jndex in range(index-1, -1, -1):
            result_list.append(input_list[index] * input_list[jndex])

    result_list.sort(reverse=True)

    for k, number in enumerate(result_list):
        number = str(number)
        for i in range(len(number)-1, 0, -1):
            if int(number[i]) < int(number[i-1]):
                break
            else:
                if i == 1:
                    return number

        if k == len(result_list) - 1:
            return -1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    print('#{} {}'.format(test_case, find_number(numbers)))
