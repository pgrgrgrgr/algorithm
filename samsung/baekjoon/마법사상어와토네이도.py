N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

cxs = [-1, 1, 1, -1]
cys = [-1, -1, 1, 1]

tor = [int(N/2), int(N/2)]
sum = 0

def in_grid(x, y):
  return 0 <= x < N and 0 <= y < N

def blow_sand(dir):
  global tor
  global sum

  total = grid[tor[0] + dxs[dir]][tor[1] + dys[dir]]
  target_x = tor[0] + dxs[dir]
  target_y = tor[1] + dys[dir]
  grid[tor[0] + dxs[dir]][tor[1] + dys[dir]] = 0

  rest = total - (int(total * 0.01) + int(total * 0.01) + int(total * 0.07) + int(total * 0.07) + int(total * 0.02) + int(total * 0.02) + int(total * 0.1) + int(total * 0.1) + int(total * 0.05))

  if dir == 0:
    if in_grid(target_x + cxs[2], target_y + cys[2]):
      grid[target_x + cxs[2]][target_y + cys[2]] += int(total * 0.01)
    else:
      sum += int(total * 0.01)
    if in_grid(target_x + cxs[3], target_y + cys[3]):
      grid[target_x + cxs[3]][target_y + cys[3]] += int(total * 0.01)
    else:
      sum += int(total * 0.01)
    if in_grid(target_x + dxs[1], target_y + dys[1]):
      grid[target_x + dxs[1]][target_y + dys[1]] += int(total * 0.07)
    else:
      sum += int(total * 0.07)
    if in_grid(target_x + dxs[1]*2, target_y + dys[1]*2):
      grid[target_x + dxs[1]*2][target_y + dys[1]*2] += int(total * 0.02)
    else:
      sum += int(total * 0.02)
    if in_grid(target_x + dxs[3], target_y + dys[3]):
      grid[target_x + dxs[3]][target_y + dys[3]] += int(total * 0.07)
    else:
      sum += int(total * 0.07)
    if in_grid(target_x + dxs[3]*2, target_y + dys[3]*2):
      grid[target_x + dxs[3]*2][target_y + dys[3]*2] += int(total * 0.02)
    else:
      sum += int(total * 0.02)
    if in_grid(target_x + cxs[0], target_y + cys[0]):
      grid[target_x + cxs[0]][target_y + cys[0]] += int(total * 0.1)
    else:
      sum += int(total * 0.1)
    if in_grid(target_x + cxs[1], target_y + cys[1]):
      grid[target_x + cxs[1]][target_y + cys[1]] += int(total * 0.1)
    else:
      sum += int(total * 0.1)
    if in_grid(target_x + dxs[0]*2, target_y + dys[0]*2):
      grid[target_x + dxs[0] * 2][target_y + dys[0] * 2] += int(total * 0.05)
    else:
      sum += int(total * 0.05)
    if in_grid(target_x + dxs[0], target_y + dys[0]):
      grid[target_x + dxs[0]][target_y + dys[0]] += rest
    else:
      sum += rest
  elif dir == 1:
    if in_grid(target_x + cxs[0], target_y + cys[0]):
      grid[target_x + cxs[0]][target_y + cys[0]] += int(total * 0.01)
    else:
      sum += int(total * 0.01)
    if in_grid(target_x + cxs[3], target_y + cys[3]):
      grid[target_x + cxs[3]][target_y + cys[3]] += int(total * 0.01)
    else:
      sum += int(total * 0.01)
    if in_grid(target_x + dxs[0], target_y + dys[0]):
      grid[target_x + dxs[0]][target_y + dys[0]] += int(total * 0.07)
    else:
      sum += int(total * 0.07)
    if in_grid(target_x + dxs[0]*2, target_y + dys[0]*2):
      grid[target_x + dxs[0]*2][target_y + dys[0]*2] += int(total * 0.02)
    else:
      sum += int(total * 0.02)
    if in_grid(target_x + dxs[2], target_y + dys[2]):
      grid[target_x + dxs[2]][target_y + dys[2]] += int(total * 0.07)
    else:
      sum += int(total * 0.07)
    if in_grid(target_x + dxs[2]*2, target_y + dys[2]*2):
      grid[target_x + dxs[2]*2][target_y + dys[2]*2] += int(total * 0.02)
    else:
      sum += int(total * 0.02)
    if in_grid(target_x + cxs[2], target_y + cys[2]):
      grid[target_x + cxs[2]][target_y + cys[2]] += int(total * 0.1)
    else:
      sum += int(total * 0.1)
    if in_grid(target_x + cxs[1], target_y + cys[1]):
      grid[target_x + cxs[1]][target_y + cys[1]] += int(total * 0.1)
    else:
      sum += int(total * 0.1)
    if in_grid(target_x + dxs[1]*2, target_y + dys[1]*2):
      grid[target_x + dxs[1] * 2][target_y + dys[1] * 2] += int(total * 0.05)
    else:
      sum += int(total * 0.05)
    if in_grid(target_x + dxs[1], target_y + dys[1]):
      grid[target_x + dxs[1]][target_y + dys[1]] += rest
    else:
      sum += rest
  elif dir == 2:
    if in_grid(target_x + cxs[0], target_y + cys[1]):
      grid[target_x + cxs[0]][target_y + cys[0]] += int(total * 0.01)
    else:
      sum += int(total * 0.01)
    if in_grid(target_x + cxs[1], target_y + cys[1]):
      grid[target_x + cxs[1]][target_y + cys[1]] += int(total * 0.01)
    else:
      sum += int(total * 0.01)
    if in_grid(target_x + dxs[1], target_y + dys[1]):
      grid[target_x + dxs[1]][target_y + dys[1]] += int(total * 0.07)
    else:
      sum += int(total * 0.07)
    if in_grid(target_x + dxs[1]*2, target_y + dys[1]*2):
      grid[target_x + dxs[1]*2][target_y + dys[1]*2] += int(total * 0.02)
    else:
      sum += int(total * 0.02)
    if in_grid(target_x + dxs[3], target_y + dys[3]):
      grid[target_x + dxs[3]][target_y + dys[3]] += int(total * 0.07)
    else:
      sum += int(total * 0.07)
    if in_grid(target_x + dxs[3]*2, target_y + dys[3]*2):
      grid[target_x + dxs[3]*2][target_y + dys[3]*2] += int(total * 0.02)
    else:
      sum += int(total * 0.02)
    if in_grid(target_x + cxs[2], target_y + cys[2]):
      grid[target_x + cxs[2]][target_y + cys[2]] += int(total * 0.1)
    else:
      sum += int(total * 0.1)
    if in_grid(target_x + cxs[3], target_y + cys[3]):
      grid[target_x + cxs[3]][target_y + cys[3]] += int(total * 0.1)
    else:
      sum += int(total * 0.1)
    if in_grid(target_x + dxs[2]*2, target_y + dys[2]*2):
      grid[target_x + dxs[2] * 2][target_y + dys[2] * 2] += int(total * 0.05)
    else:
      sum += int(total * 0.05)
    if in_grid(target_x + dxs[2], target_y + dys[2]):
      grid[target_x + dxs[2]][target_y + dys[2]] += rest
    else:
      sum += rest
  elif dir == 3:
    if in_grid(target_x + cxs[1], target_y + cys[1]):
      grid[target_x + cxs[1]][target_y + cys[1]] += int(total * 0.01)
    else:
      sum += int(total * 0.01)
    if in_grid(target_x + cxs[2], target_y + cys[2]):
      grid[target_x + cxs[2]][target_y + cys[2]] += int(total * 0.01)
    else:
      sum += int(total * 0.01)
    if in_grid(target_x + dxs[0], target_y + dys[0]):
      grid[target_x + dxs[0]][target_y + dys[0]] += int(total * 0.07)
    else:
      sum += int(total * 0.07)
    if in_grid(target_x + dxs[0]*2, target_y + dys[0]*2):
      grid[target_x + dxs[0]*2][target_y + dys[0]*2] += int(total * 0.02)
    else:
      sum += int(total * 0.02)
    if in_grid(target_x + dxs[2], target_y + dys[2]):
      grid[target_x + dxs[2]][target_y + dys[2]] += int(total * 0.07)
    else:
      sum += int(total * 0.07)
    if in_grid(target_x + dxs[2]*2, target_y + dys[2]*2):
      grid[target_x + dxs[2]*2][target_y + dys[2]*2] += int(total * 0.02)
    else:
      sum += int(total * 0.02)
    if in_grid(target_x + cxs[0], target_y + cys[0]):
      grid[target_x + cxs[0]][target_y + cys[0]] += int(total * 0.1)
    else:
      sum += int(total * 0.1)
    if in_grid(target_x + cxs[3], target_y + cys[3]):
      grid[target_x + cxs[3]][target_y + cys[3]] += int(total * 0.1)
    else:
      sum += int(total * 0.1)
    if in_grid(target_x + dxs[3]*2, target_y + dys[3]*2):
      grid[target_x + dxs[3] * 2][target_y + dys[3] * 2] += int(total * 0.05)
    else:
      sum += int(total * 0.05)
    if in_grid(target_x + dxs[3], target_y + dys[3]):
      grid[target_x + dxs[3]][target_y + dys[3]] += rest
    else:
      sum += rest

  if in_grid(tor[0] + dxs[dir], tor[1] + dys[dir]):
    tor = [tor[0] + dxs[dir], tor[1] + dys[dir]]

for i in range(1, N):
  if i % 2 != 0:
    for _ in range(i):
      blow_sand(0)
    for _ in range(i):
      blow_sand(1)
  else:
    for _ in range(i):
      blow_sand(2)
    for _ in range(i):
      blow_sand(3)

for _ in range(N - 1):
  blow_sand(0)

print(sum)
