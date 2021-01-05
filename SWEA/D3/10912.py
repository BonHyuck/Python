# 외로운 문자
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    text = input()
    # 각 문자의 개수를 담을 딕셔너리
    char_dict = {}

    # 문자열의 각 알파벳 처리
    for c in text:
        char_dict[c] = char_dict.get(c, 0) + 1

    # 남는 문자를 담을 배열
    result_list = []
    # 반복을 통해 딕셔너리의 각 key, value 처리
    for char, cnt in char_dict.items():
        # 알파벳의 개수가 홀수일때만 처리
        # 짝수의 경우 짝이 맞춰져있음.
        if cnt % 2 == 1:
            # 결과 배열에 넣기
            result_list.append(char)

    result = ''

    if len(result_list) == 0:
        result = "Good"
    else:
        result_list.sort()
        result = ''.join(result_list)

    print('#{} {}'.format(test_case, result))
