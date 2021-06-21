from collections import deque

def solution(numbers, target):
  answer = 0
  sq = 0
  queue = deque()
  n = len(numbers)
  queue.append((numbers[0],sq))
  queue.append((numbers[0]*-1,sq))
  while queue:
    tmp = queue[0][0]
    sq = queue.popleft()[1]
    sq += 1
    if sq == n:
      break
    for i in [1,-1]:
      queue.append((tmp + numbers[sq]*i,sq))
  for i in queue:
    if i[0] == target:
      answer += 1
  return answer

print(solution([1,1,1,1,1],3))