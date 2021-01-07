import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    # 문자열 받기
    text = input()
    result = ''

    char_dict = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
    }

    # 뒤에서부터 반복문 시작
    for c in text:
        result = char_dict[c] + result

    print('#{} {}'.format(test_case, result))
