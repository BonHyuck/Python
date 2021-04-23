while True:
    X, Y, Z = map(int, input().split())
    if X == 0 and Y == 0 and Z == 0:
        break
    H = max(X, Y, Z)
    test = 0
    if X != H:
        test += X ** 2
    if Y != H:
        test += Y ** 2
    if Z != H:
        test += Z ** 2
    if test == H ** 2:
        print("right")
    else:
        print("wrong")