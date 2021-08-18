import math

def solution(n,a,b):
  answer = 1

  while answer < n/2:
    if a%2 != 0:
      if a+1 == b:
        return answer
    if a%2 == 0:
      if a-1 == b:
        return answer
    a = math.ceil(a/2)
    b = math.ceil(b/2)
    answer += 1

  return answer
