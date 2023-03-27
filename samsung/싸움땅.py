# 위 과정을 1~n번 플레이어가 수행하면 한 라운드 끝.
# 입력 n, m, k: n이 격자 크기, m이 플레이어 수, k가 라운드 수
# n개에 줄에 걸쳐 총의 정보 주어짐. 0은 빈 칸
# m개에 줄에 걸쳐 x, y, d, s가 공백으로 주어짐. (x, y)는 플레이어 위치, d가 방향(0:상, 1:우, 2:하, 3:좌), s가 기본 능력치

# 초기 변수 설정
n, m, k = map(int, input().split())

gun_grid = [[[0] for _ in range(n+1)] for _ in range(n+1)]

gun = [list(map(int, input().split())) for _ in range(n)]
gun.append([[0,0,0,0,0]])

cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    gun_grid[i][j][0] = gun[i-1][j-1]
    
player_info = [list(map(int, input().split())) for _ in range(m)]

player_grid = []
player_direction = []
player_power = [] # 기본 능력치
player_stat = [] # 기본 + 총 능력치

points = [0] * m

for i in range(m):
  player_grid.append([player_info[i][0], player_info[i][1]])
  player_direction.append(player_info[i][2])
  player_power.append(player_info[i][3])
  player_stat.append([player_info[i][3], 0])

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

# 필요 함수 선언
def in_grid(x, y):
  return x > 0 and x < n + 1 and y > 0 and y < n + 1

def is_player(x, y):
  for i in range(m):
    if [x,y] == player_grid[i]:
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
  while(True):
    if(in_grid(player_grid[player][0] + dxs[player_direction[player]], player_grid[player][1] + dys[player_direction[player]]) and not is_player(player_grid[player][0] + dxs[player_direction[player]], player_grid[player][1] + dys[player_direction[player]])):
      player_grid[player][0] += dxs[player_direction[player]]
      player_grid[player][1] += dys[player_direction[player]]
      break
    else:
      if(player_direction[player] != 3):
        player_direction[player] += 1
      else:
        player_direction[player] = 0

def is_match(grid):
  return player_grid.count(grid)

def simulate():
  for i in range(m):
    # 1-1 향하고 있는 방향으로 한 칸 이동, 해당 방향이 격자가 밖인 경우 정반대 방향으로 1칸 이동
    if(in_grid(player_grid[i][0] + dxs[player_direction[i]], player_grid[i][1] + dys[player_direction[i]])):
      player_grid[i][0] += dxs[player_direction[i]]
      player_grid[i][1] += dys[player_direction[i]]
    else:
      go_opposite(i, player_direction[i])
    # 2-1 이동한 곳에 플레이어가 없다면, 총이 있는지 확인 후 총 획득. 이 때 공격력 더 쎈 총 획득하고 이전 총은 버림
    if(is_match(player_grid[i]) == 1):
      if(len(gun_grid[player_grid[i][0]][player_grid[i][1]]) > 0):
        gun_grid[player_grid[i][0]][player_grid[i][1]] = list(reversed(sorted(gun_grid[player_grid[i][0]][player_grid[i][1]])))
        if(player_stat[i][1] < gun_grid[player_grid[i][0]][player_grid[i][1]][0]):
          player_stat[i][1], gun_grid[player_grid[i][0]][player_grid[i][1]][0] = gun_grid[player_grid[i][0]][player_grid[i][1]][0], player_stat[i][1]
    # 2-2-1 이동 방향에 플레이어가 있으면 맞짱. 능력치+총으로, 근데 같으면 능력치로 싸움. 공격력의 차이만큼 승자가 포인트 획득
    # 2-2-2 진 플레이어는 갖고 있던 총을 해당 격자에 버리고 한 칸 이동. 이 때 격자 밖이거나 플레이어면 우측 90도로 이동. 이동 칸에 총 있으면 2-1과 같은 방식으로 총 획득
    # 2-2-3 이긴 플레이어는 승리한 칸에 있는 총 중 가장 높은거 획득하고 자기 총 버림
    else:
      versus = []
      for j in range(m):
        if(player_grid[i] == player_grid[j]):
          versus.append(j)
      if(sum(player_stat[versus[0]]) > sum(player_stat[versus[1]])):
        points[versus[0]] += abs(sum(player_stat[versus[0]]) - sum(player_stat[versus[1]]))
        gun_grid[player_grid[i][0]][player_grid[i][1]].append(player_stat[versus[1]][1])
        gun_grid[player_grid[i][0]][player_grid[i][1]] = list(reversed(gun_grid[player_grid[i][0]][player_grid[i][1]]))
        player_stat[versus[1]][1] = 0
        if(in_grid(player_grid[versus[1]][0] + dxs[player_direction[versus[1]]], player_grid[versus[1]][1] + dys[player_direction[versus[1]]]) and not is_player(player_grid[versus[1]][0] + dxs[player_direction[versus[1]]], player_grid[versus[1]][1] + dys[player_direction[versus[1]]])):
          player_grid[versus[1]][0] += dxs[player_direction[versus[1]]]
          player_grid[versus[1]][1] += dys[player_direction[versus[1]]]
          gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]])))
          if(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] > 0):
            player_stat[versus[1]][1], gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] = gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0], player_stat[versus[1]][1]
        else:
          go_right(versus[1], player_direction[versus[1]])
          gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]])))
          if(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] > 0):
            player_stat[versus[1]][1], gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] = gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0], player_stat[versus[1]][1]
        gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]])))
        if(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] > player_stat[versus[0]][1]):
          player_stat[versus[0]][1], gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] = gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0], player_stat[versus[0]][1]

      elif(sum(player_stat[versus[0]]) < sum(player_stat[versus[1]])):
        points[versus[1]] += sum(player_stat[versus[1]]) - sum(player_stat[versus[0]])
        gun_grid[player_grid[i][0]][player_grid[i][1]].append(player_stat[versus[0]][1])
        gun_grid[player_grid[i][0]][player_grid[i][1]] = list(reversed(gun_grid[player_grid[i][0]][player_grid[i][1]]))
        player_stat[versus[0]][1] = 0
        if(in_grid(player_grid[versus[0]][0] + dxs[player_direction[versus[0]]], player_grid[versus[0]][1] + dys[player_direction[versus[0]]]) and not is_player(player_grid[versus[0]][0] + dxs[player_direction[versus[0]]], player_grid[versus[0]][1] + dys[player_direction[versus[0]]])):
          player_grid[versus[0]][0] += dxs[player_direction[versus[0]]]
          player_grid[versus[0]][1] += dys[player_direction[versus[0]]]
          gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]])))
          if(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] > 0):
            player_stat[versus[0]][1], gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] = gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0], player_stat[versus[0]][1]
        else:
          go_right(versus[0], player_direction[versus[0]])
          gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]])))
          if(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] > 0):
            player_stat[versus[0]][1], gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] = gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0], player_stat[versus[0]][1]
        gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]])))
        if(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] > player_stat[versus[1]][1]):
          player_stat[versus[1]][1], gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] = gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0], player_stat[versus[1]][1]

      else:
        if(player_stat[versus[0]][0] > player_stat[versus[1]][0]):
          points[versus[0]] += sum(player_stat[versus[0]]) - sum(player_stat[versus[1]])
          gun_grid[player_grid[i][0]][player_grid[i][1]].append(player_stat[versus[1]][1])
          gun_grid[player_grid[i][0]][player_grid[i][1]] = list(reversed(gun_grid[player_grid[i][0]][player_grid[i][1]]))
          player_stat[versus[1]][1] = 0
          if(in_grid(player_grid[versus[1]][0] + dxs[player_direction[versus[1]]], player_grid[versus[1]][1] + dys[player_direction[versus[1]]]) and not is_player(player_grid[versus[1]][0] + dxs[player_direction[versus[1]]], player_grid[versus[1]][1] + dys[player_direction[versus[1]]])):
            player_grid[versus[1]][0] += dxs[player_direction[versus[1]]]
            player_grid[versus[1]][1] += dys[player_direction[versus[1]]]
            gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]])))
            if(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] > 0):
              player_stat[versus[1]][1], gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] = gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0], player_stat[versus[1]][1]
          else:
            go_right(versus[1], player_direction[versus[1]])
            gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]])))
            if(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] > 0):
              player_stat[versus[1]][1], gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] = gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0], player_stat[versus[1]][1]
          gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]])))
          if(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]]):
            player_stat[versus[0]][1], gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] = gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0], player_stat[versus[0]][1]

        elif(player_stat[versus[0]][0] < player_stat[versus[1]][0]):
          points[versus[1]] += sum(player_stat[versus[1]]) - sum(player_stat[versus[0]])
          gun_grid[player_grid[i][0]][player_grid[i][1]].append(player_stat[versus[0]][1])
          gun_grid[player_grid[i][0]][player_grid[i][1]] = list(reversed(gun_grid[player_grid[i][0]][player_grid[i][1]]))
          player_stat[versus[0]][1] = 0
          if(in_grid(player_grid[versus[0]][0] + dxs[player_direction[versus[0]]], player_grid[versus[0]][1] + dys[player_direction[versus[0]]]) and not is_player(player_grid[versus[0]][0] + dxs[player_direction[versus[0]]], player_grid[versus[0]][1] + dys[player_direction[versus[0]]])):
            player_grid[versus[0]][0] += dxs[player_direction[versus[0]]]
            player_grid[versus[0]][1] += dys[player_direction[versus[0]]]
            gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]])))
            if(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] > 0):
              player_stat[versus[0]][1], gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] = gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0], player_stat[versus[0]][1]
          else:
            go_right(versus[0], player_direction[versus[0]])
            gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]])))
            if(gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] > 0):
              player_stat[versus[1]][1], gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0] = gun_grid[player_grid[versus[0]][0]][player_grid[versus[0]][1]][0], player_stat[versus[1]][1]
          gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]] = list(reversed(sorted(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]])))
          if(gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] > player_stat[versus[1]][1]):
            player_stat[versus[1]][1], gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0] = gun_grid[player_grid[versus[1]][0]][player_grid[versus[1]][1]][0], player_stat[versus[1]][1]

for _ in range(k):
  simulate()

for i in points:
  print(i, end=" ")

# codetree 답안

# EMPTY = (-1, -1, -1, -1, -1, -1)

# # 변수 선언 및 입력:
# n, m, k = tuple(map(int, input().split()))

# # 각 칸마다 놓여있는 총 목록을 관리합니다.
# gun = [
#     [[] for _ in range(n)]
#     for _ in range(n)
# ]
# for i in range(n):
#     nums = list(map(int, input().split()))
#     for j in range(n):
#         # 총이 놓여 있는 칸입니다.
#         if nums[j] != 0:
#             gun[i][j].append(nums[j])

# # 각 칸마다 플레이어 정보를 관리합니다.
# # 순서대로 (num, x, y, d, s, a) 정보를 관리합니다.
# # (x, y)위치에서 방향 d를 보고 있으며
# # 초기 능력치가 s인 num번 플레이어가
# # 공격력이 a인 총을 들고 있음을 뜻합니다.
# # 총이 없으면 a는 0입니다.
# players = []
# for i in range(m):
#     x, y, d, s = tuple(map(int, input().split()))
#     players.append((i, x - 1, y - 1, d, s, 0))

# # 입력으로 주어지는
# # 방향 순서대로 
# # dx, dy를 정의합니다.
# # ↑, →, ↓, ←
# dxs = [-1, 0, 1,  0]
# dys = [ 0, 1, 0, -1]

# # 플레이어들의 포인트 정보를 기록합니다.
# points = [0] * m


# # (x, y)가 격자를 벗어나는지 확인합니다.
# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n


# # 현재 (x, y)위치에서 방향 d를 보고 있을 때
# # 그 다음 위치와 방향을 찾아줍니다.
# def get_next(x, y, d):
#     nx, ny = x + dxs[d], y + dys[d]
#     # 격자를 벗어나면
#     # 방향을 뒤집어
#     # 반대 방향으로 한 칸 이동합니다.
#     if not in_range(nx, ny):
#         # 반대 방향 : 0 <. 2 / 1 <. 3
#         d = (d + 2) if d < 2 else (d - 2)
#         nx, ny = x + dxs[d], y + dys[d]

#     return (nx, ny, d)


# # 해당 칸에 있는 Player를 찾아줍니다.
# # 없다면 EMPTY를 반환합니다.
# def find_player(pos):
#     for i in range(m):
#         _, x, y, _, _, _ = players[i]
#         if pos == (x, y):
#             return players[i]

#     return EMPTY


# # Player p의 정보를 갱신해줍니다.
# def update(p):
#     num, _, _, _, _, _ = p

#     # Player의 위치를 찾아
#     # 값을 갱신해줍니다.
#     for i in range(m):
#         num_i, _, _, _, _, _ = players[i]

#         if num_i == num:
#             players[i] = p
#             break


# # 플레이어 p를 pos 위치로 이동시켜줍니다.
# def move(p, pos):
#     num, x, y, d, s, a = p
#     nx, ny = pos

#     # 가장 좋은 총으로 갱신해줍니다.
#     gun[nx][ny].append(a)
#     gun[nx][ny].sort(reverse=True)
#     a = gun[nx][ny][0]
#     gun[nx][ny].pop(0)

#     p = (num, nx, ny, d, s, a)
#     update(p)


# # 진 사람의 움직임을 진행합니다.
# # 결투에서 패배한 위치는 pos입니다.
# def loser_move(p):
#     num, x, y, d, s, a = p
    
#     # 먼저 현재 위치에 총을 내려놓게 됩니다.
#     gun[x][y].append(a)

#     # 빈 공간을 찾아 이동하게 됩니다.
#     # 현재 방향에서 시작하여
#     # 90'씩 시계방향으로
#     # 회전하다가 
#     # 비어있는 최초의 곳으로 이동합니다.
#     for i in range(4):
#         ndir = (d + i) % 4
#         nx, ny = x + dxs[ndir], y + dys[ndir]
#         if in_range(nx, ny) and find_player((nx, ny)) == EMPTY:
#             p = (num, x, y, ndir, s, 0)
#             move(p, (nx, ny))
#             break


# # p2과 p2가 pos에서 만나 결투를 진행합니다.
# def duel(p1, p2, pos):
#     num1, _, _, d1, s1, a1 = p1
#     num2, _, _, d2, s2, a2 = p2

#     # (초기 능력치 + 총의 공격력, 초기 능력치) 순으로 우선순위를 매겨 비교합니다.

#     # p1이 이긴 경우
#     if (s1 + a1, s1) > (s2 + a2, s2):
#         # p1은 포인트를 얻게 됩니다.
#         points[num1] += (s1 + a1) - (s2 + a2)
#         # p2는 진 사람의 움직임을 진행합니다.
#         loser_move(p2)
#         # 이후 p1은 이긴 사람의 움직임을 진행합니다.
#         move(p1, pos)
#     # p2가 이긴 경우
#     else:
#         # p2는 포인트를 얻게 됩니다.
#         points[num2] += (s2 + a2) - (s1 + a1)
#         # p1은 진 사람의 움직임을 진행합니다.
#         loser_move(p1)
#         # 이후 p2는 이긴 사람의 움직임을 진행합니다.
#         move(p2, pos)


# # 1라운드를 진행합니다.
# def simulate():
#     # 첫 번째 플레이어부터 순서대로 진행합니다.
#     for i in range(m):
#         num, x, y, d, s, a = players[i]

#         # Step 1-1. 현재 플레이어가 움직일 그 다음 위치와 방향을 구합니다.
#         nx, ny, ndir = get_next(x, y, d)
        
#         # 해당 위치에 있는 전 플레이어 정보를 얻어옵니다.
#         next_player = find_player((nx, ny))
        
#         # 현재 플레이어의 위치와 방향을 보정해줍니다.
#         curr_player = (num, nx, ny, ndir, s, a)
#         update(curr_player)
        
#         # Step 2. 해당 위치로 이동해봅니다.
#         # Step 2-1. 해당 위치에 플레이어가 없다면 그대로 움직입니다.
#         if next_player == EMPTY:
#             move(curr_player, (nx, ny))
#         # Step 2-2. 해당 위치에 플레이어가 있다면 결투를 진행합니다.
#         else:
#             duel(curr_player, next_player, (nx, ny))

# # k번에 걸쳐 시뮬레이션을 진행합니다.
# for _ in range(k):
#     simulate()

# # 각 플레이어가 획득한 포인트를 출력합니다.
# for point in points:
#     print(point, end=" ")