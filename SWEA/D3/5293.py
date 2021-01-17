import sys
sys.stdin = open('input.txt', 'r')

def start_search(index):
    global result

    if result != "impossible":
        return

    if index >= length:
        return

    a = b = c = d = 0
    for i in range(length - 1):
        text = str(arr[i]) + str(arr[i+1])
        if text == "00":
            a += 1
        elif text == "01":
            b += 1
        elif text == "10":
            c += 1
        elif text == "11":
            d += 1

        if A < a or B < b or C < c or D < d:
            break

    if A == a and B == b and C == c and D == d:
        result = ''.join(arr)
        return
    else:
        if arr.count(1) == length:
            return
        else:
            for k in range(index, length):
                arr[k] = 1
                start_search(index + 1)
                arr[k] = 0


    return


T = int(input())
for test_case in range(1, T+1):
    # A : “00”
    # B : “01”
    # C : “10”
    # D : “11”
    A, B, C, D = map(int, input().split())
    # 전체 문자열의 길이는 A+B+C+D+1
    length = A+B+C+D+1
    arr = [0] * length
    result = "impossible"
    start_search(0)

    print(result)

    