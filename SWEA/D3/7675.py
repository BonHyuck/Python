# SWEA 7675
# 문장을 구분하고 분석
###################
#    내 코드       #
###################
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 문장의 개수
    N = int(input())
    # 문장 전체를 잘게 쪼개서 받기
    letters = list(input())

    # 확인용
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_letters = '.?!'
    numbers = '0123456789'

    # 잘개 쪼개진 것을 다시 합쳐 문장의 리스트로 만들기
    sentences = []
    # sentences 리스트에 넣을 한 문장
    one_sentence = ''
    for letter in letters:
        if letter in last_letters:
            one_sentence += letter
            sentences.append(one_sentence)
            one_sentence = ''
        else:
            one_sentence += letter


    # 각 문장의 이름 개수를 담기
    name_count = []

    for sentence in sentences:
        # 각 문장을 띄어쓰기로 구분
        new_list = sentence.split()
        # 각 문장 내 이름을 세기 위한 변수
        cnt = 0
        for word in new_list:
            # 첫문자가 대문자 or 마침표 or 물음표 or 느낌표 or
            if word[0] in capital_letters:
                cnt += 1
                if len(word) > 1:
                    for i in range(1, len(word)):
                        if word[i] in capital_letters or word[i] in numbers:
                            cnt -= 1
                            break
            elif word[-1] in last_letters and len(word) > 1:
                cnt += 1

        name_count.append(cnt)

    result = ''
    for i in name_count:
        result += ' '+str(i)

    print('#{}{}'.format(test_case, result))

###################
#   다른분 코드     #
###################


def solution():
    # 문장 개수
    n = int(input())
    # 문장
    s = input()
    # 결과를 위한 배열
    res = [0 for _ in range(n)]
    # j = index
    # w = 스위치 같은 느낌??
    j = w = 0
    # 문장의 길이만큼 반복
    for i in range(len(s)):
        # 마침표 도달
        if s[i] == '!' or s[i] == '?' or s[i] == '.' or s[i] == ',':
            # 스위치가 켜져있음 = 첫 단어 대문자
            if w == 1:
                # 카운트에 추가
                res[j] += 1
            # 스위치 원위치
            w = 0
            # 다음 인덱스로 넘어가기
            j += 1
        # 그냥 띄어쓰기
        elif s[i] == ' ':
            # 첫 단어 대문자
            if w == 1:
                # 카운트에 추가
                res[j] += 1
            # 스위치 끄기
            w = 0
        else:
            # 스위치 없음: 마침표나 띄어쓰기 직후
            if w == 0:
                # 대문자 확인
                if ord('A') <= ord(s[i]) <= ord('Z'):
                    w = 1
                # 대문자 없으면 해당 단어는 의미 없음
                else:
                    w = -1
            elif w == 1:
                # 그냥 계속 넘어가기 위해(해당 단어는 검사 필요 없음)
                # w = -1 로 설정
                # 띄어쓰기 혹은 마침표 도달까지 w = -1
                if not ord('a') <= ord(s[i]) <= ord('z'):
                    w = -1

    return ' '.join(list(map(str, res)))

# 출력을 위한 함수
def main():
    TC = int(input())
    for test_case in range(1, TC + 1):
        print("#{} {}".format(test_case, solution()))


if __name__ == "__main__":
    main()