# SWEA 1983
# 학생의 성적을 구분하고 특정 학생의 성적 출력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 첫번째로 학생 수와 성적을 알고 싶어하는 학생의 Index
    N, K = map(int, input().split())

    letter_grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']
    new_letter_grade = []
    for i in range(0, len(letter_grade)):
        for j in range(0, N//10):
            new_letter_grade.append(letter_grade[i])

    grade_list = []

    # 점수 받아서 계산 후 리스트에 넣기
    for i in range(0, N):
        one_student = list(map(int, input().split()))
        student_grade = one_student[0]*0.35 + one_student[1]*0.45 + one_student[2]*0.2
        grade_list.append(student_grade)

    this_student = grade_list[K-1]

    find_student = grade_list.copy()
    find_student.sort(reverse=True)

    for index, value in enumerate(find_student):
        if this_student == value:
            print('#{} {}'.format(test_case, new_letter_grade[index]))