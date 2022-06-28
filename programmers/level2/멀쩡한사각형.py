# import math

# def solution(w,h):
#   answer = 0
#   cnt=1
#   while cnt != w:
#     answer += math.floor(-h/w * cnt + h)
#     cnt += 1
#   return answer*2

import math

def solution(w,h):
  
  return w*h - (w+h-math.gcd(w,h))
