N = int(input())
queue = []
answer = []
for k in range(N):
    input_text = list(input().split())
    if input_text[0] == 'push':
        queue.append(int(input_text[1]))
    elif input_text[0] == 'pop':
        if len(queue) > 0:
            answer.append(queue.pop(0))
        else:
            answer.append(-1)
    elif input_text[0] == 'size':
        answer.append(len(queue))
    elif input_text[0] == 'empty':
        if len(queue) > 0:
            answer.append(0)
        else:
            answer.append(1)
    elif input_text[0] == 'front':
        if len(queue) > 0:
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif input_text[0] == 'back':
        if len(queue) > 0:
            answer.append(queue[-1])
        else:
            answer.append(-1)

for k in answer:
    print(k)