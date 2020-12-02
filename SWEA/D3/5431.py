# SWEA 5431
# 과제 확인하기
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    # 학생 배열 만들기
    students = [i for i in range(1, N+1)]
    no_work = list(map(int, input().split()))

    for item in no_work:
        if item in students:
            students[students.index(item)] = 0

    result = '#'+str(test_case)
    for number in sorted(students):
        if number != 0:
            result += ' '+str(number)

    print(result)

