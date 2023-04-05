from collections import deque
# 1 공장 설립 - m개의 belt 설치, n/m개가 각 belt 에 올려지도록 정확한 n개 물건 준비

# 2 물건 하차 - 최대 무게 w_max. 1~m 까지의 belt를 보면서 각 벨트의 맨 앞의 무게가 w_max 이하면 하차. 하차를 모두 진행한 뒤에 하차한 상자 무게 합 출력
# w_max 초과하는 상자이면 맨 뒤로 보냄

# 3 물건 제거 - 주어진 물건의 고유 id인 r_id값에 해당하는 상자를 제거 후 상자들을 앞으로 한 칸 내림
# 그런 상자가 있다면 r_id값 출력, 없으면 -1 출력

# 4 물건 확인 - 물건의 고유 id인 주어진 f_id값에 해당하는 상자 위에 있는 상자들을 모두 앞으로 가져옴
# 그런 상자가 있다면 f_id값 출력, 없으면 -1 출력

# 5 벨트 고장 - 고장 발생 벨트 번호 b_num 주어짐. b_num belt의 바로 오른쪽 벨트에다가 다 옮기기 시작.
# 명령 수행 전 b_num belt가 이미 망가져 있었다면 -1 출력, 아니면 b_num 출력

# 변수 설정
q = int(input())
init = list(map(int, input().split()))
n, m = init[1], init[2]

box_id = init[3:3+n]
box_w = init[3+n:]
box_per_belts = int(n/m)

belts = []
for box in zip(box_id, box_w):
  belts.append(box)
belts = [deque(belts[i*box_per_belts:(i+1)*box_per_belts]) for i in range(int(n/m) - 1)]
# 함수 설정
# 물건 하차
def unload_box(w_max):
  sum = 0
  for belt in belts:
    if(belt):
      if belt[0][1] <= w_max:
        sum += belt.popleft()[1]
      else:
        belt.append(belt.popleft())
    else:
      continue
  print(sum)

# 물건 제거
def remove_box(r_id):
  for belt in belts:
    if(belt):
      tmp = belt[0]
      while(not belt[0][0] == r_id):
        belt.append(belt.popleft())
        if(belt[0] == tmp):
          break
      if(belt[0][0] == r_id):
        print(r_id)
        return
    else:
      continue
  print(-1)
  return
        
# 물건 찾기
def find_box(f_id):
  cnt = 0
  idx = 1
  for belt in belts:
    k = len(belt)
    if(belt):
      while(belt[0][0] != f_id and cnt != k):
        cnt += 1
        belt.append(belt.popleft())
      cnt = 0
      if(belt[0][0] == f_id):
        print(idx)
        return
      idx += 1
    else:
      continue
  print(-1)
  return

# 벨트 고장
def check_belt(b_num):
  while(not belts[(b_num + 1) % m]):
    b_num = (b_num + 1) % m

def failure_belt(b_num):
  if(not belts[b_num]):
    print(-1)
    return
  else:
    check_belt(b_num)
    while(belts[b_num]):
      belts[(b_num + 1) % m].append(belts[b_num].popleft())
    print(b_num + 1)
    return

def simulate(order, arg):
  if(order == 200):
    unload_box(arg)
  elif(order == 300):
    remove_box(arg)
  elif(order == 400):
    find_box(arg)
  elif(order == 500):
    failure_belt(arg - 1)

for i in range(q - 1):
  order, arg = input().split()
  simulate(int(order), int(arg))

  
# q 개의 명령어가 수행될 것
# 1 - 100 n m ID1 ID2 ... IDn W1 W2 ... Wn
# 2 - 200 w_max
# 3 - 300 r_id
# 4 - 400 f_id
# 5 - 500 b_num
