'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

8
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111

16
0000000000000000
0000000000000000
0000111100001111
0000111100001111
0001111100011111
0011111100111111
0011111100111111
0011111100111111
0000000000000000
0000000000000000
0000111100001111
0000111100001111
0001111100011111
0011111100111111
0011111100111111
0011111100111111
'''

# dr = [0, 0, 1, 1]
# dc = [0, 1, 0, 1]
#
# N = int(input())
# box = [list(map(int, list(input()))) for _ in range(N)]
# arr = []
# r = 0
# c = 0
# while r < N and c < N:
#     text = '('
#     for k in range(4):
#         text += str(box[r+dr[k]][c+dc[k]])
#     text += ')'
#     arr.append(text)
#     if c + 2 < N and c % 4 == 0:
#         c += 2
#     elif c % 4 == 2 and r % 4 == 0 and r + 2 < N:
#         c -= 2
#         r += 2
#     elif r % 4 == 2 and c % 4 == 2 and c + 2 < N:
#         r -= 2
#         c += 2
#     elif c + 2 >= N:
#         c = 0
#         if r + 2 < N:
#             r += 2
#         else:
#             break
#     else:
#         break
# #
# # # 생성된 배열의 길이
# length = len(arr)
# index = 0
# while length > 1:
#     while index < length:
#         text = '('
#         for k in range(4):
#             new_text = arr.pop(0)
#             if new_text == '(0000)':
#                 new_text = '0'
#             elif new_text == '(1111)':
#                 new_text = '1'
#             text += new_text
#             index += 1
#         text += ')'
#         arr.append(text)
#     index = 0
#     length = len(arr)
#
# print(arr[0])
#
# # 솔직히 위의 코드는 뭐가 틀렸는지 모르겠다...
# # 틀렸다니까 다른 방법으로 풀기는 하는데 샘플로 만든 것들은 다 맞았는데
# # 틀리는 반례를 못 찾겠다. 찾기 귀찮아서 그런건 아니다.

def start_division(row, col, length):
    # 모두 같은 값인지 확인
    diff_value = False
    for r in range(length):
        for c in range(length):
            # 같지 않음
            if box[row][col] != box[row+r][col+c]:
                diff_value = True
                break
        # 다른 값이 나옴
        if diff_value:
            break
    # 확인 결과 전부 같은 값
    if not diff_value:
        return str(box[row][col])

    # 위에서 리턴이 안되면 쪼개줘야겠지??
    half_length = length // 2
    value = '('
    # 왼쪽 위
    value += start_division(row, col, half_length)
    # 오른쪽 위
    value += start_division(row, col + half_length, half_length)
    # 왼쪽 아래
    value += start_division(row + half_length, col, half_length)
    # 오른쪽 아래
    value += start_division(row + half_length, col + half_length, half_length)

    return value+')'


N = int(input())
box = [list(map(int, list(input()))) for _ in range(N)]
result = start_division(0, 0, N)
print(result)
