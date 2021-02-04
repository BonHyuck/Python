'''
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90

'''

# 길찾기
def find_best_way(point, moved_distance):
    global distance
    # 딱 맞게 도달해야함
    if point == D:
        # 움직인 거리 비교
        if moved_distance < distance:
            distance = moved_distance
        return
    # 뒤로 못 가니까 넘으면 안됨
    if point > D:
        return
    # 이동 많이 하면 안됨
    if moved_distance >= D:
        return

    # 가능한 모든 지름길 검사
    for road in roads:
        # 시작, 끝, 거리
        start, end, dist = road[0], road[1], road[2]
        # 지름길의 시작점이 현재 위치보다 앞에 있다.
        if start > point:
            # 일단 지름길의 시작점까지 이동
            find_best_way(start, moved_distance + (start - point))
        # 지름길의 시작점이 현재 위치
        elif start == point:
            # 지름길로 가는게 빠르면
            if end - start > dist:
                # 지름길 거리만큼 가고 위치는 끝점으로 이동
                find_best_way(end, moved_distance + dist)
            # 고속도로로 가는게 지름길보다 빠르면
            elif end - start < dist:
                # 고속도로로 가고 위치는 끝점으로 이동
                find_best_way(end, moved_distance + (end - start))
        # 지름길의 시작점이 현재 위치보다 뒤에(이미 지나온 거리)
        #현재 위치부터 끝까지 감
        else:
            find_best_way(D, moved_distance + (D - point))



N, D = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(N)]
# print(roads)
# 최대 거리
distance = D
# 0, 0 : 시작점, 움직인 거리
find_best_way(0, 0)
print(distance)