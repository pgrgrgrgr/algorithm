T = int(input())

def in_grid(x, y, n):
  return 0 <= x < n and 0 <= y < n

for _ in range(T):
  N = int(input())
  grid = [list(map(int, input().split())) for _ in range(N)]

  scores = []

  # 상, 우, 하, 좌
  dxs = [-1, 0, 1, 0]
  dys = [0, 1, 0, -1]
  
  for i in range(N):
    for j in range(N):
      if grid[i][j] == 0:
        for d in range(len(dxs)):
          score = 0
          dx, dy = i, j
          dir = d
          nx, ny = dx + dxs[d], dy + dys[d]
          

          while(True):
            if (nx, ny) == (dx, dy):
              scores.append(score)
              break
            if not in_grid(nx, ny, N):
              dir = (dir + 2) % 4
              nx += dxs[dir]
              ny += dys[dir]
              score += 1
            if grid[nx][ny] == -1:
              scores.append(score)
              break
            elif grid[nx][ny] == 1:
              if dir == 0:
                dir = 2
              elif dir == 1:
                dir = 3
              elif dir == 2:
                dir = 1
              elif dir == 3:
                dir = 0
              score += 1
            elif grid[nx][ny] == 2:
              if dir == 0:
                dir = 1
              elif dir == 1:
                dir = 3
              elif dir == 2:
                dir = 0
              elif dir == 3:
                dir = 2
              score += 1
            elif grid[nx][ny] == 3:
              if dir == 0:
                dir = 3
              elif dir == 1:
                dir = 2
              elif dir == 2:
                dir = 0
              elif dir == 3:
                dir = 1
              score += 1
            elif grid[nx][ny] == 4:
              if dir == 0:
                dir = 2
              elif dir == 1:
                dir = 0
              elif dir == 2:
                dir = 3
              elif dir == 3:
                dir = 1
              score += 1
            elif grid[nx][ny] == 5:
              dir = (dir + 2) % 4
              score += 1
            elif grid[nx][ny] == 6 or grid[nx][ny] == 7 or grid[nx][ny] == 8 or grid[nx][ny] == 9 or grid[nx][ny] == 10:
              print(grid[nx][ny])
              for x in range(N):
                for y in range(N):
                  if (grid[x][y] == grid[nx][ny]) and (nx, ny) != (x, y):
                    nx, ny = x, y
            nx += dxs[dir]
            ny += dys[dir]
            
  print(score)