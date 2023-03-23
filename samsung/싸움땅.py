# 위 과정을 1~n번 플레이어가 수행하면 한 라운드 끝.
# 입력 n, m, k: n이 격자 크기, m이 플레이어 수, k가 라운드 수
# n개에 줄에 걸쳐 총의 정보 주어짐. 0은 빈 칸
# m개에 줄에 걸쳐 x, y, d, s가 공백으로 주어짐. (x, y)는 플레이어 위치, d가 방향(0:상, 1:우, 2:하, 3:좌), s가 기본 능력치

# 초기 변수 설정
n, m, k = map(int, input().split())

gun_grid = []
for i in range(n):
  gun_grid.append([map(int, input().split())])
print(gun_grid)
player_info = [list(map(int, input().split())) for _ in range(m)]

player_grid = []
player_direction = []
player_power = [] # 기본 능력치
player_stat = [] # 기본 + 총 능력치

points = [0] * m

for i in range(m):
  player_grid.append((player_info[i][0], player_info[i][1]))
  player_direction.append(player_info[i][2])
  player_power.append(player_info[i][3])
  player_stat.append((player_info[i][3], 0))

dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

# 필요 함수 선언
def in_grid(x, y):
  return x >= 0 and x < n and y >= 0 and y < n

def is_player(x, y):
  chk = 0
  for i in range(m):
    if (x,y) == player_grid[i]:
      return True
  return False

def go_opposite(player, direction):
  player_grid[player][0] += dxs[direction - 2]
  player_grid[player][1] += dys[direction - 2]
  if(player_direction[player] <= 1):
    player_direction[player] += 2
  else:
    player_direction[player] -= 2
#0상 1우 2하 3좌
def go_right(player, direction):
  while(not in_grid(player_grid[player], player_grid[player])):
    if(player_direction[player] != 3):
      player_grid[player][0] += dxs[direction + 1]
      player_grid[player][1] += dys[direction + 1]
      player_direction[player] += 1
    else:
      player_grid[player][0] += dxs[0]
      player_grid[player][1] += dys[0]
      player_direction[player] = 0


# 1-1 향하고 있는 방향으로 한 칸 이동, 해당 방향이 격자가 밖인 경우 정반대 방향으로 1칸 이동
# 2-1 이동한 곳에 플레이어가 없다면, 총이 있는지 확인 후 총 획득. 이 때 공격력 더 쎈 총 획득하고 이전 총은 버림
# 2-2-1 이동 방향에 플레이어가 있으면 맞짱. 능력치+총으로, 근데 같으면 능력치로 싸움. 공격력의 차이만큼 승자가 포인트 획득
# 2-2-2 진 플레이어는 갖고 있던 총을 해당 격자에 버리고 한 칸 이동. 이 때 격자 밖이거나 플레이어면 우측 90도로 이동. 이동 칸에 총 있으면 2-1과 같은 방식으로 총 획득
# 2-2-3 이긴 플레이어는 승리한 칸에 있는 총 중 가장 높은거 획득하고 자기 총 버림

def simulate():
  for i in range(m):
    # 1-1
    if(in_grid(player_grid[i][0] + dxs[player_direction[i]], player_grid[i][1] + dys[player_direction[i]])):
      player_grid[i][0] += dxs[player_direction[i]]
      player_grid[i][1] += dys[player_direction[i]]
    else:
      go_opposite(i, player_direction[i])
    # 2-1
    if(player_grid.count(player_grid[i]) == 1):
      if(gun_grid[player_grid[i][0]][player_grid[i][1]] != 0):
        if(player_stat[i][1] < gun_grid[player_grid[i][0]][player_grid[i][1]]):
          player_stat[i][1], gun_grid[player_grid[i][0]][player_grid[i][1]] = gun_grid[player_grid[i][0]][player_grid[i][1]], player_stat[i][1]
    # 2-2-1
    else:
      versus = []
      for j in range(m):
        if(player_grid.count(player_grid[i]) != 1):
          versus.append(j)
      

    
        