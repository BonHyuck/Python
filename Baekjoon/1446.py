'''
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90

'''

def find_best_way(point, moved_distance):
    global distance
    if point == D:
        if moved_distance < distance:
            distance = moved_distance
        return

    if point > D:
        return

    if moved_distance >= D:
        return

    for road in roads:
        start, end, dist = road[0], road[1], road[2]
        if start > point:
            find_best_way(start, moved_distance + (start - point))
        elif start == point:
            if end - start > dist:
                find_best_way(end, moved_distance + dist)
            elif end - start < dist:
                find_best_way(end, moved_distance + (end - start))
        else:
            find_best_way(D, moved_distance + (D - point))



N, D = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(N)]
# print(roads)
distance = D
find_best_way(0, 0)
print(distance)