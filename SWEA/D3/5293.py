import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    # A : “00”
    # B : “01”
    # C : “10”
    # D : “11”
    A, B, C, D = map(int, input().split())
    # 결과를 담을 변수
    result = "impossible"
    # 00과 11이 있다면 01이나 10이 무조건 있기때문에
    # A와 D가 1 이상이지만 B와 C가 0인 경우는 불가능
    if A and D and B == 0 and C == 0:
        result = "impossible"
    # B와 C의 차이가 1 이하일때 가능하다.
    # 둘의 차이가 2 이상이면 균형이 맞지 않아 생성 불가
    elif abs(B-C) <= 1:
        # 01 이 1개 더 많음
        if B > C:
            result = "0"*(A+1)+"1"*(D+1)+"01"*C
        # 둘이 같음
        elif B == C:
            # 10 이나 01 없이 00만 있음
            if B == 0 and A:
                result = "0"*(A+1)
            # 10 이나 01 없이 11만 있음
            elif B == 0 and D:
                result = "1" * (D + 1)
            # 그외의 경우
            else:
                result = "1" * (D + 1) + "0" * (A + 1) + "10" * (B-1) + "1"
        # 10 이 1개더 많음
        else:
            result = "1"*(D+1)+"0"*(A+1)+"10"*B
    print('#{} {}'.format(test_case, result))