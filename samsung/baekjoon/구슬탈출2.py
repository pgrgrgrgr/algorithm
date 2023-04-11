from collections import deque

N, M = map(int, input().split())

grid = [list(input()) for _ in range(N)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for i in range(N):
  for j in range(M):
    if grid[i][j] == 'R':
      red = [i, j]
    if grid[i][j] == 'B':
      blue = [i, j]
    if grid[i][j] == 'O':
      out = [i, j]

def move(x, y, dx, dy):
  cnt = 0
  while grid[x + dx][y + dy] != '#' and grid[x][y] != 'O':
    x += dx
    y += dy
    cnt += 1
  return x, y, cnt

def bfs():
  global red
  global blue

  rx, ry = red
  bx, by = blue

  visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
  q = deque()
  q.append([rx, ry, bx, by, 1])

  while q:
    rx, ry, bx, by, depth = q.popleft()
    visited[rx][ry][bx][by] = True

    if(depth > 10):
      break

    for dx, dy in zip(dxs, dys):
      nrx, nry, r_cnt = move(rx, ry, dx, dy)
      nbx, nby, b_cnt = move(bx, by, dx, dy)

      if grid[nbx][nby] == 'O':
        continue
      if grid[nrx][nry] == 'O':
        print(depth)
        return
      
      if nrx == nbx and nry == nby:
        if r_cnt > b_cnt:
          nrx -= dx
          nry -= dy
        else:
          nbx -= dx
          nby -= dy

      if not visited[nrx][nry][nbx][nby]:
        visited[nrx][nry][nbx][nby] = True
        q.append([nrx, nry, nbx, nby, depth + 1])
  
  print(-1)

bfs()