from collections import deque

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def solution(maps):
    answer = []

    def bfs(maps):
        q = deque()
        visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] != 'X' and not visited[i][j]:
                    days = 0    
                    q.append([i, j])
                    visited[i][j] = True
                    days += int(maps[i][j])

                    while q:
                        x, y = q.popleft()
                        for dx, dy in zip(dxs, dys):
                            nx = x + dx
                            ny = y + dy

                            if 0 <= nx < len((maps)) and 0 <= ny < len((maps[0])):
                                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                                    q.append([nx, ny])
                                    days += int(maps[nx][ny])
                                    visited[nx][ny] = True
                    answer.append(days)                    

    bfs(maps)
    answer = sorted(answer)
    if not answer:
        return [-1]
    return answer

print(solution(["XXX","XXX","XXX"]))