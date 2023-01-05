import math

def solution(number, limit, power):
  answer = 0
  for i in range(1, number + 1):
    chk = 0
    for j in range(1, int(math.sqrt(i) + 1)):
      if(i % j == 0):
        if(j * j == i):
          chk += 1
        else:
          chk += 2
      if(chk > limit):
        answer += power
        break
    if(chk <= limit):
      answer += chk
    
  return answer

print(solution(10,3,2))