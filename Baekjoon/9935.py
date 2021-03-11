text = input()
bomb = input()
bomb_length = len(bomb)
while bomb in text:
    k = text.index(bomb)
    text = text[0:k] + text[k+bomb_length::]

if len(text) == 0:
    print("FRULA")
else:
    print(text)

text = input()
bomb = input()
result = ''
for c in text:
    result += c
    if c == bomb[-1]:
        if result[len(result)-len(bomb):len(result)] == bomb:
            result = result[:len(result)-len(bomb)]
if len(result):
    print(result)
else:
    print("FRULA")

text = input()
bomb = input()
result = []
for c in text:
    result.append(c)
    if c == bomb[-1]:
        if ''.join(result[-len(bomb):]) == bomb:
            for k in range(len(bomb)):
                result.pop(-1)

if len(result):
    print(''.join(result))
else:
    print("FRULA")