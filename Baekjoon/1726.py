
# 동쪽 1 => 0, 서쪽 2 => 1, 남쪽 3 => 2, 북쪽 4 => 3
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_path():
    # 행, 열, 방향, 움직임 수
    queue = [[start_row, start_col, start_dir, 0]]
    # 방문체크
    # 3차 배열??
    # 행, 열, 방향(동서남북 방향만 바뀌고 같은 위치에 있을수 있기때문에 방향체크를 위해 range(4)
    visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(M)]
    # 시작점과 시작방향은 방문체크
    visited[start_row][start_col][start_dir] = 1
    while queue:
        row, col, dir, cnt = queue.pop(0)
        # 도착지점과 도착방향이면 끝, 결과값 리턴
        if row == end_row and col == end_col and dir == end_dir:
            return cnt
        # 이동거리 먼저 확인 1, 2, 3
        for k in range(1, 4):
            # 해당 거리로 k 만큼 이동
            new_r = row + dx[dir] * k
            new_c = col + dy[dir] * k
            # 인덱스 확인
            if 0 <= new_r < M and 0 <= new_c < N:
                # 이미 방문
                if visited[new_r][new_c][dir] == 1:
                    # 일단 다음칸도 확인
                    continue
                # 벽이라면
                if box[new_r][new_c] == 1:
                    break
                else:
                    visited[new_r][new_c][dir] = 1
                    queue.append([new_r, new_c, dir, cnt + 1])
            # 인덱스 벗어남    
            else:
                break

        
        # 방향 확인
        for new_dir in range(4):
            # 다른 방향 + 아직 방문안함
            if dir != new_dir and visited[row][col][new_dir] == 0:
                # 새로운 방향 방문처리
                visited[row][col][new_dir] = 1
                # 2번 돌아야하는 반대방향
                if (dir + new_dir) % 4 == 1:
                    queue.append([row, col, new_dir, cnt + 2])
                else:
                    queue.append([row, col, new_dir, cnt + 1])


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
start_row, start_col, start_dir = map(int, input().split())
end_row, end_col, end_dir = map(int, input().split())
# 인덱스가 1부터 시작하므로 1씩 빼주기
# 방향도 인덱스처럼 쓸 수 있게 0씩 빼주기
start_row -= 1
start_col -= 1
start_dir -= 1
end_row -= 1
end_col -= 1
end_dir -= 1
print(find_path())

