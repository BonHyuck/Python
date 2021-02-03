'''
(@&
?/--
/(\
?
#
'''
while True:
    text = input()

    if text == '#':
        break

    octopus = ['-', '\\', '(', '@', '?', '>', '&', '%', '/']

    text = list(text)
    number = 0
    cnt = 0
    while text:
        c = text.pop(-1)
        n = octopus.index(c)
        if c == '/':
            n = -1
        number += n * (8 ** cnt)
        cnt += 1

    print(number)