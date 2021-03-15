from itertools import combinations

N = int(input())
equation = list(input())
result = int(equation[0])
# 괄호가 없는 수식 계산
for k in range(1, N // 2 + 1):
    sign = equation[k * 2 - 1]
    number = int(equation[k * 2])
    if sign == '+':
        result += number
    elif sign == '-':
        result -= number
    elif sign == '*':
        result *= number

#괄호가 시작할 수 있는 위치 정하기
parenthesis = [k * 2 for k in range(N // 2)]
# 시작 가능한 모든 위치
possible = []
# 괄호는 1개만 붙히는 경우부터 붙힐 수 있는 모든 괄호를 붙히는 경우까지
for i in range(1, (N // 4) + ((N % 4) // 2) + 1):
    possible.extend(list(combinations(parenthesis, i)))

# 모든 경우의 수를 검토한다.
while possible:
    # 경우의수 1개 추출
    next = list(possible.pop(0))
    # 겹괄호는 안되니까 겹괄호 확인용
    next_possible = True
    # 괄호를 2개 이상 붙힐 때만 확인
    if len(next) > 1:
        for k in range(1, len(next)):
            # 겹괄호의 경우
            if next[k] < next[k-1] + 4:
                next_possible = False
                break
    # 겹괄호가 붙을것 같으면 바로 다음 경우의 수로 넘어가기
    if not next_possible:
        continue

    # 계산을 위한 queue
    queue = []
    # equation의 인덱스
    index = 0
    # 경우의 수의 인덱스
    next_index = 0
    # equation의 끝까지 검사
    while index < N:
        # 경우의 수의 인덱스 검사 + 괄호를 붙히는 곳인가?
        if next_index < len(next) and index == next[next_index]:
            # 첫번째 숫자
            first = int(equation[index])
            # 연산자
            sign = equation[index+1]
            # 두번 째 숫자
            second = int(equation[index+2])
            # 다음 equation으로 넘어간다.
            index += 3
            # 다음 괄호 붙히는 곳으로 넘어간다.
            next_index += 1
            # 계산 후 queue에 업로드
            if sign == '+':
                queue.append(first + second)
            elif sign == '-':
                queue.append(first - second)
            elif sign == '*':
                queue.append(first * second)
            continue
        # 위의 조건문을 거치지 못하면
        # queue에 그냥 붙히고 다음으로 넘어간다.
        queue.append(equation[index])
        index += 1
    # 괄호를 계산이후 결과 집계
    mid_result = int(queue[0])
    for k in range(1, len(queue) // 2 + 1):
        sign = queue[k * 2 - 1]
        number = int(queue[k * 2])
        if sign == '+':
            mid_result += number
        elif sign == '-':
            mid_result -= number
        elif sign == '*':
            mid_result *= number
    if mid_result > result:
        result = mid_result

print(result)



