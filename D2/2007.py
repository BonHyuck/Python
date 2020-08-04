# SWEA 2007
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    text = list(input())

    i = 1
    while True:
        first_word = text[0:i]
        compare_word = text[i:i * 2]
        if str(first_word) == str(compare_word):
            break
        else:
            i += 1


    print('#{} {}'.format(test_case, i))
