# SWEA 5356
# 단어를 세로로 바꾸기
T = int(input())
for test_case in range(1, T+1):
    arr = []
    len_arr = []
    for i in range(5):
        something = input()
        arr.append(something)
        len_arr.append(len(something))

    result = ''
    for j in range(max(len_arr)):
        for k in range(5):
            if j < len(arr[k]):
                result += arr[k][j]

    print('#{} {}'.format(test_case, result))
