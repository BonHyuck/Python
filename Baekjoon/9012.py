T = int(input())
for test_case in range(T):
    text = input()
    stack = []
    for t in text:
        if t == '(':
            stack.append('(')
        elif t == ')':
            if len(stack) == 0:
                stack.append("FAIL")
                break
            else:
                stack.pop(-1)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')