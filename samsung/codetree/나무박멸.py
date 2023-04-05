# n 격자
# m 박멸이 진행되는 년 수
# k 제초제 범위(대각선)
# c 제초제가 남아있는 년 수

n, m, k, c = tuple(map(int, input().split()))

grid = [list(map(int, input().split())) for i in range(n)]
breed_grid = [[0 for _ in range(n)] for _ in range(n)]
weed_grid = [[0 for _ in range(n)] for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

cxs = [-1, -1, 1, 1]
cys = [1, -1, 1, -1]

sum = 0

def in_grid(x, y):
  return 0 <= x and x < n and 0 <= y and y < n

def grow():
  for i in range(n):
    for j in range(n):
      if grid[i][j] <= 0:
        continue

      chk = 0
      for dx, dy in zip(dxs, dys):
        nx, ny = i + dx, j + dy
        if(not in_grid(nx, ny)):
          continue
        if(grid[nx][ny] > 0):
          chk += 1
      
      grid[i][j] += chk

def breed():
  for i in range(n):
    for j in range(n):
      breed_grid[i][j] = 0

  for x in range(n):
    for y in range(n):
      if(grid[x][y] <= 0):
        continue

      chk = 0
      for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if(not in_grid(nx, ny)):
          continue
        if(weed_grid[nx][ny]):
          continue
        if(grid[nx][ny] == 0):
          chk += 1

      for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if(not in_grid(nx, ny)):
          continue
        if(weed_grid[nx][ny]):
          continue
        if grid[nx][ny] == 0:
          breed_grid[nx][ny] = breed_grid[nx][ny] + grid[x][y] // chk

  for i in range(n):
    for j in range(n):
      grid[i][j] += breed_grid[i][j]

def weed_chk():
  global sum

  max_rm, max_x, max_y = 0, 0, 0
  for i in range(n):
    for j in range(n):
      if grid[i][j] <= 0:
        continue

      cnt = grid[i][j]
      for dx, dy in zip(cxs, cys):
        nx, ny = i, j
        for _ in range(k):
          nx, ny = nx + dx, ny + dy
          if(not in_grid(nx, ny)):
            break
          if(grid[nx][ny] <= 0):
            break
          cnt += grid[nx][ny]

      if max_rm < cnt:
        max_rm = cnt
        max_x = i
        max_y = j
  
  sum += max_rm

  if grid[max_x][max_y] > 0:
    grid[max_x][max_y] = 0
    weed_grid[max_x][max_y] = c

    for dx, dy in zip(cxs, cys):
      nx, ny = max_x, max_y
      for _ in range(k):
        nx, ny = nx + dx, ny + dy
        if(not in_grid(nx, ny)):
          break
        if grid[nx][ny] < 0:
          break
        if grid[nx][ny] == 0:
          weed_grid[nx][ny] = c
          break
          
        grid[nx][ny] = 0
        weed_grid[nx][ny] = c

def rm_weed():
  for i in range(n):
    for j in range(n):
      if(weed_grid[i][j] > 0):
        weed_grid[i][j] -= 1
      
for _ in range(m):
  grow()
  breed()
  rm_weed()
  weed_chk()

print(sum)