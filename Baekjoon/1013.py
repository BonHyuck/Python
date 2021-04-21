import re

T = int(input())
for test_case in range(T):
    text = input()
    if re.fullmatch('(100+1+|01)+', text) is not None:
        print("YES")
    else:
        print("NO")
    # if result is not None and result.start() == 0 and result.end() == len(text):
    #     print("YES")
    # else:
    #     print("NO")