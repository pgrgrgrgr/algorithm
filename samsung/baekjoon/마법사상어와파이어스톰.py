from collections import deque

N, Q = map(int, input().split())
size = 2 ** N
grid = [list(map(int, input().split())) for _ in range(size)]
rotate_grid = [[0] * size for _ in range(size)]
L = list(map(int, input().split()))
max_p = 0
sum = 0

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

def in_grid(x, y):
  return 0 <= x < size and 0 <= y < size

def rotate(Li):
  unit = 2 ** Li
  for i in range(0, size, unit):
    for j in range(0, size, unit):
      for x in range(unit):
        for y in range(unit):
          rotate_grid[i + y][j + unit - x - 1] = grid[i + x][j + y]
  

def melt():
  for i in range(size):
    for j in range(size):
      chk = 0
      for dx, dy in zip(dxs, dys):
        nx, ny = i + dx, j + dy
        if not in_grid(nx, ny):
          continue
        if rotate_grid[nx][ny]:
          chk += 1

      if rotate_grid[i][j] == 0:
        grid[i][j] = rotate_grid[i][j]
        
      if rotate_grid[i][j] > 0:
        if chk < 3:
          grid[i][j] = rotate_grid[i][j] - 1
        else:
          grid[i][j] = rotate_grid[i][j] 

def bfs():
  visited = [[False] * size for _ in range(size)]
  
  global sum
  global max_p

  for i in range(size):
    for j in range(size):
      q = deque()
      if grid[i][j] != 0 and visited[i][j] == False:
        sum += grid[i][j]
        
        q.append([i, j])
        visited[i][j] = True
        max = 1
        while q:
          x, y = q.pop()
          for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_grid(nx, ny):
              continue
            if grid[nx][ny] > 0 and visited[nx][ny] == False:
              q.append([nx, ny])
              max += 1
              visited[nx][ny] = True
              sum += grid[nx][ny]
      
        if max > max_p:
          max_p = max
        else:
          max = 0

for Li in L:
  rotate(Li)
  melt()
bfs()

print(sum)
print(max_p)