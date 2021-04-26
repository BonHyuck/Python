N = int(input())
stack = []
command = []
for k in range(N):
    command.append(list(input().split()))


answer = []
for input_text in command:
    if input_text[0] == 'push':
        stack.append(int(input_text[1]))
    elif input_text[0] == 'pop':
        if len(stack) > 0:
            answer.append(stack.pop(-1))
        else:
            answer.append(-1)
    elif input_text[0] == 'size':
        answer.append(len(stack))
    elif input_text[0] == 'empty':
        if len(stack) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif input_text[0] == 'top':
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack[-1])

for k in answer:
    print(k)