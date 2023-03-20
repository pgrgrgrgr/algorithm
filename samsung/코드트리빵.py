import sys
from collections import deque

# input 값 설정
n, m = map(int, input().split())

grid = [
  list(map(int, input().split())) for _ in range(n)
]

cv_store = []
for _ in range(m):
  x, y = map(int, input().split())
  cv_store.append((x - 1, y - 1))

# 초기 값 설정
OUT = (-1, -1) # 격자 밖에 있는 사람들
people = [OUT] * m

curr_t = 0 # 현재 시간

dxs = [-1, 0, 0, 1] # 상, 좌, 우, 하의 우선 순위로 이동
dys = [0, -1, 1, 0] 

# bfs 변수 설정
step = [[0] * n for _ in range(n)]  # 이동 cost 기록
visited = [[False] * n for _ in range(n)] # 이동 grid 기록

# 격자 내에 있는지 check
def in_grid(x, y):
  return 0 <= x and x < n and 0 <= y and y < n

# 이동이 가능한지 check
def can_go(x, y):
  return in_grid(x, y) and not visited[x][y] and grid[x][y] != 2 # 격자 내에 있어야 하고, 방문하지 않았으며, 이동 불가능한 위치가 아니여야 함

# bfs 구현
def bfs(start_pos):
  # grid 초기화
  for i in range(n):
    for j in range(n):
      step[i][j] = 0
      visited[i][j] = False

  q = deque()
  q.append(start_pos)
  sx, sy = start_pos
  visited[sx][sy] = True
  step[sx][sy] = 0

  while(q):
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys): # 이동 우선 순위대로 이동
      nx, ny = x + dx, y + dy
      if(can_go(nx, ny)):
        q.append((nx, ny))
        step[nx][ny] = step[x][y] + 1
        visited[nx][ny] = True

# simulation
def simulate():
  # 격자에 있는 사람들에 한해 1칸 움직이기
  for i in range(m):
    if(people[i] == OUT or people[i] == cv_store[i]): # 격자에 있지 않거나 이미 편의점에 도착했으면 다음 사람
      continue

    bfs(cv_store[i])

    px, py = people[i]

    min_dist = 30
    prior_x, prior_y = -1, -1
    
    for dx, dy in zip(dxs, dys):
      nx, ny = px + dx, py + dy
      if(in_grid(nx, ny) and visited[nx][ny] and min_dist > step[nx][ny]):
        min_dist = step[nx][ny]
        prior_x, prior_y = nx, ny

    people[i] = (prior_x, prior_y)

  # 도착한 사람들은 해당 지역을 이동 불가능하게 설정
  for i in range(m):
    if(people[i] == cv_store[i]):
      px, py = people[i]
      grid[px][py] = 2

  # 현재 시간이 이동할 사람보다 큰 지 check 즉, 모든 사람이 적어도 출발은 했다는 것
  if(curr_t > m):
    return
  
  # 여기선 격자 밖에 있는 사람들을 베이스 캠프에 위치시켜야 함
  bfs(cv_store[curr_t - 1])

  # 가장 가까운 베이스 캠프 선택하기
  min_dist = 30
  prior_x, prior_y = -1, -1

  for i in range(n):
    for j in range(n):
      if(visited[i][j] and grid[i][j] == 1 and min_dist > step[i][j]):
        min_dist = step[i][j]
        prior_x, prior_y = i, j
  people[curr_t - 1] = (prior_x, prior_y)

  # 베이스 캠프 이동 불가 설정
  grid[prior_x][prior_y] = 2

# 전부 편의점에 도착하였는지 check
def end():
  for i in range(m):
    if(people[i] != cv_store[i]):
      return False
  return True

while True:
  curr_t += 1
  simulate()
  if(end()):
    break

print(curr_t)