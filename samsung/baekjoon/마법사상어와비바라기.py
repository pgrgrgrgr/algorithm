N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
cloud_grid = [[0] * N for _ in range(N)]

clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [-1, -1, 0, 1, 1, 1, 0, -1]

def in_grid(x, y):
  return 0 <= x < N and 0 <= y < N

# 4, 4 -> 3, 5 (3, 0)
# 0, 0 -> -1, -1 (4, 4)
# 2, 2 -> 3, 3 

def set():
  for x, y in clouds:
    cloud_grid[x][y] = 1

def move(dir):
  for cloud in clouds:
    cloud[0] += dxs[dir]
    cloud[1] += dys[dir]
    if cloud[0] < 0:
      cloud[0] += N
    elif cloud[0] == N:
      cloud[0] = 0
    if cloud[1] < 0:
      cloud[1] += N
    elif cloud[1] == N:
      cloud[1] = 0

def simulate():
  for i in range(N):
    for j in range(N):
      if(cloud_grid[i][j] != 1):
        continue
      grid[i][j] += 1
      cloud_grid[i][j] = -1

      
  chk = 0
  for i in range(N):
    for j in range(N):
      if(cloud_grid[i][j] == -1):
        for k in range(1, len(dxs), 2):
          dx, dy = dxs[k], dys[k]
          nx, ny = i + dx, j + dy
          if in_grid(nx, ny) and grid[nx][ny]:
            chk += 1
        
        grid[i][j] += chk
        chk = 0

  clouds.clear()
        
  for i in range(N):
    for j in range(N):
      if grid[i][j] >= 2 and cloud_grid[i][j] != -1:
        grid[i][j] -= 2
        clouds.append([i,j])

      if cloud_grid[i][j] == -1:
        cloud_grid[i][j] = 0

for _ in range(M):
  di, si = map(int, input().split())
  for i in range(si):
    move(di - 1)
  set()
  simulate()

sum = 0
for i in range(N):
  for j in range(N):
    sum += grid[i][j]

print(sum)