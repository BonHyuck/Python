# 센서의 개수
N = int(input())
# 집중국의 개수
K = int(input())
# 센서들
arr = sorted(list(map(int, input().split())))

# 집중국의 개수가 센서와 같거나 크면
# 모든 센서 위치에 집중국을 설치하면 됨
if K >= N:
    print(0)
# 집중국을 잘 설치해보자
else:
    # 문제의 요점은 N개의 센서를 K개의 그룹으로 나누는 것
    # 가장 멀리 떨어져 있는 센서를 기점으로 나눈다
    # 같은 그룹안에서 집중국을 어디에 설치하든 상관이 없으므로 그룹을 나누는게 중요할 듯
    distance = []
    for i in range(0, N-1):
        # 이미 정렬이 돼있으니까 다음것과의 거리만 구한다
        distance.append(arr[i+1] - arr[i])
    # 먼 거리부터 차례로 정렬
    distance = sorted(distance, reverse=True)
    # K개의 그룹을 만들기 위해선 K-1번의 disconnect
    # 뭐라고 해야지... 분리? 가 필요하다
    # 가장 먼 거리(index = 0) 부터 분리한다.
    for j in range(K-1):
        distance.pop(0)

    print(sum(distance))



