N = int(input())
result = 1
number = 1
memo = [6]
index = 0
if N == 1:
    print(result)
else:
    while True:
        if number < N <= number + memo[index]:
            result += 1
            print(result)
            break
        else:
            memo.append(memo[index] + 6)
            number += memo[index]
            result += 1
            index += 1

