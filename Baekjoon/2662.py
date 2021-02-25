# from itertools import combinations_with_replacement
#
# # N = 투자 금액
# # M = 기업 수
# N, M = map(int, input().split())
# # 가능한 투자 금액
# money = [i for i in range(0, N+1)]
# # 각 기업의 투자금액에 따른 이익
# invest = {
#     0: [0 for _ in range(M)]
# }
# for k in range(N):
#     arr = list(map(int, input().split()))
#     key = arr.pop(0)
#     invest[key] = arr
#
# # 가능한 모든 조합
# possible = list(combinations_with_replacement(money, M))
# # 위 조합 중 합이 투자금액인 조합
# real_possible = []
# for p in possible:
#     if sum(p) == N:
#         real_possible.append(p)
# # 결과값
# result = 0
# result_arr = []
# for pos in real_possible:
#     mid_result = 0
#     for k in range(len(pos)):
#         mid_result += invest[pos[k]][k]
#     if mid_result > result:
#         result_arr = pos
#         result = mid_result
#
# print(result)
# print(*result_arr)

# 현재 기업의 인덱스, 투자금, 투자결과
def start_investment(index, investment, return_value, string_index):
    global result, result_coord

    # 기업 수 확인
    # 마지막 기업!
    if index >= M-2:
        # 마지막 기업에 투자할 금액이 있거나 0이면
        if N - investment >= 0:
            if result < (return_value + money[N - investment][M-1]):
                result = (return_value + money[N - investment][M-1])
                result_coord = string_index+" "+str(N - investment)
            return
        # 마지막 기업까지 왔는데 투자금이 마이너스?
        else:
            return

    for k in range(N):
        if investment + k <= N:
            start_investment(index+1, investment+k, return_value+money[k][index+1], string_index+" "+str(k))


# N = 투자 금액
# M = 기업 수
N, M = map(int, input().split())
# 가능한 투자 금액
money = [[0 for _ in range(M)]]
# 순서대로 입력값이 들어오니까 그냥 넣기
for _ in range(N):
    arr = list(map(int, input().split()))
    arr.pop(0)
    money.append(arr)

result = 0
result_coord = ''

# 0번째 기업부터 투자
for i in range(N):
    start_investment(0, i, money[i][0], str(i))

print(result)
print(result_coord)


from itertools import permutations
import sys
sys.setrecursionlimit(1000000)

# N = 투자 금액
# M = 기업 수
N, M = map(int, input().split())
# 가능한 투자 금액
money = [i for i in range(0, N+1)]
possible = []
for k in list(permutations(money, M)):
    if sum(k) == N:
        possible.append(k)
invest = [[0 for _ in range(M)]]
for _ in range(N):
    invest.append(list(map(int, input().split()))[1:])

result = 0
result_str = ''
for pos in possible:
    mid_result = 0
    for i in range(len(pos)):
        mid_result += invest[pos[i]][i]
    if mid_result > result:
        result_str = str(pos)
        result = mid_result

print(result)
print(*result_str[1:-1].split(', '))
