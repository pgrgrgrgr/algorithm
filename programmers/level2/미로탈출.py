from collections import deque

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def solution(maps):
    answer = 0
    k = len(maps)
    v = len(maps[0])
    chk = False

    for x in range(k):
        for y in range(v):
            if maps[x][y] == 'S':
                start = [x, y, 0]
            if maps[x][y] == 'E':
                exit = [x, y]
            if maps[x][y] == 'L':
                lever = [x, y, 0]

    def bfs(start, end):
        q = deque()
        q.append(start)

        visited = [[False for _ in range(v)] for _ in range(k)]
        visited[start[0]][start[1]] = True

        def in_grid(x, y):
            return 0 <= x < k and 0 <= y < v
        
        while q:
            cx, cy, d = q.popleft()
            d += 1
            if [cx, cy] == [end[0], end[1]]:
                end[2] = d
                q.clear()
                return d

            for dx, dy in zip(dxs, dys):
                nx, ny = cx + dx, cy + dy
                if in_grid(nx, ny) and not visited[nx][ny] and not maps[nx][ny] == 'X':
                    q.append([nx, ny, d])
                    visited[nx][ny] = True
                if chk and in_grid(nx, ny) and maps[nx][ny] == 'E':
                    return d
    
    l = bfs(start, lever)
    chk = True
    e = bfs(lever, exit)

    if l == None or e == None:
        return -1
    else:
        return e - 1

print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))