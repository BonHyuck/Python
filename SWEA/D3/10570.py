import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    A, B = map(int, input().split())
    cnt = 0
    for k in range(A, B+1):
        # k의 팰린드롬(회문) 여부 확인
        if str(k) != str(k)[::-1]:
            continue

        # 제곱근의 정수 여부 확인
        root = k ** (1 / 2)
        if root == int(root):
            # 제곱근이 정수라면 해당 제곱근의 팰린드롬 여부 확인
            if str(int(root)) == str(int(root))[::-1]:
                cnt += 1

    print('#{} {}'.format(test_case, cnt))