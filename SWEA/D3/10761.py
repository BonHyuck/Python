import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    # 입력값 받아오기
    arr = list(input().split())
    # 눌러야하는 버튼 개수
    N = arr.pop(0)
    # 버튼을 순서대로 저장할 배열
    buttons = []
    # O가 누를 버튼 리스트
    orange_buttons = []
    # B가 누를 버튼 리스트
    blue_buttons = []
    for i in range(len(arr) // 2):
        color, button = arr[i*2], int(arr[i*2+1])
        buttons.append((color, button))
        if color == 'O':
            orange_buttons.append(button)
        else:
            blue_buttons.append(button)
    # O의 현재 위치
    orange = 1
    # B의 현재 위치
    blue = 1
    # 눌러야하는 버튼
    button_color, button_number = buttons.pop(0)

    time = 1

    while button_number != 0:
        # B가 누를 차례라면
        if button_color == 'B':
            # 버튼 번호 확인
            # 버튼이 B보다 뒤에 있으면 뒤로 1칸
            if button_number < blue:
                blue -= 1
            # 현재 버튼이 위치해 있음
            elif button_number == blue:
                # 누르고 새로운 버튼으로 시작
                if len(buttons) > 0:
                    button_color, button_number = buttons.pop(0)
                    blue_buttons = blue_buttons[1:]
                else:
                    button_number = 0
                    break
            # 버튼이 앞에 있음
            else:
                blue += 1

            # O도 행동을 해야함
            if len(orange_buttons) > 0:
                if orange_buttons[0] < orange:
                    orange -= 1
                elif orange_buttons[0] > orange:
                    orange += 1

        # O가 누를 차례라면
        else:
            if button_number < orange:
                orange -= 1
            # 현재 버튼이 위치해 있음
            elif button_number == orange:
                # 누르고 새로운 버튼으로 시작
                if len(buttons) > 0:
                    button_color, button_number = buttons.pop(0)
                    orange_buttons = orange_buttons[1:]
                else:
                    button_number = 0
                    break
            # 버튼이 앞에 있음
            else:
                orange += 1

            # O도 행동을 해야함
            if len(blue_buttons) > 0:
                if blue_buttons[0] < blue:
                    blue -= 1
                elif blue_buttons[0] > blue:
                    blue += 1

        time += 1

    print('#{} {}'.format(test_case, time))