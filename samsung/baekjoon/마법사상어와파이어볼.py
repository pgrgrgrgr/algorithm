N, M, K = map(int, input().split())

grid = [[[] for _ in range(N)] for _ in range(N)]
fireballs = []

for _ in range(M):
  x, y, m, s, d = map(int, input().split())
  fireballs.append([x-1, y-1, m, s, d])

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
  while fireballs:
    i, j, m, s, d = fireballs.pop()
    grid[(i + dxs[d] * s) % N][(j + dys[d] * s) % N].append([m, s, d])

def mix():
  for i in range(N):
    for j in range(N):
      if(len(grid[i][j]) > 1):
        new_m, new_s = 0, 0
        odd, even = 0, 0

        for m, s, d in grid[i][j]:
          new_m += m
          new_s += s

          if d % 2 == 0:
            even += 1
          else:
            odd += 1

        new_d = True if even == len(grid[i][j]) or odd == len(grid[i][j]) else False

        if new_m < 5:
          grid[i][j].clear()
        else:
          new_m = new_m//5
          new_s = int(new_s/len(grid[i][j]))
          grid[i][j].clear()
          if new_d:
            for dir in range(0, len(dxs), 2):
              fireballs.append([i, j, new_m, new_s, dir])
          else:
            for dir in range(1, len(dxs), 2):
              fireballs.append([i, j, new_m, new_s, dir])
      
      if(len(grid[i][j]) == 1):
        fireballs.append([i, j] + grid[i][j].pop())
          



for _ in range(K):
  move()
  mix()

print(sum(ball[2] for ball in fireballs))