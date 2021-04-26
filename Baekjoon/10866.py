from collections import deque

N = int(input())
deq = deque()
answer = deque()
for k in range(N):
    text = list(input().split())
    if text[0] == 'push_front':
        deq.appendleft(int(text[1]))
    elif text[0] == 'push_back':
        deq.append(int(text[1]))
    elif text[0] == 'pop_front':
        if len(deq) > 0:
            answer.append(deq.popleft())
        else:
            answer.append(-1)
    elif text[0] == 'pop_back':
        if len(deq) > 0:
            answer.append(deq.pop())
        else:
            answer.append(-1)
    elif text[0] == 'size':
        answer.append(len(deq))
    elif text[0] == 'empty':
        if len(deq) > 0:
            answer.append(0)
        else:
            answer.append(1)
    elif text[0] == 'front':
        if len(deq) > 0:
            answer.append(deq[0])
        else:
            answer.append(-1)
    elif text[0] == 'back':
        if len(deq) > 0:
            answer.append(deq[-1])
        else:
            answer.append(-1)

for k in answer:
    print(k)