import re

def solution(s):
  sstack=[]
  s=list(s)
  while s:
    sstack.append(s.pop())
    if len(sstack) > 1 and sstack[-1] == sstack[-2]:
      sstack.pop()
      sstack.pop()
  if(len(sstack)==0):
    return 1
  else:
    return 0

  
# def solution(s):
#   answer = []
#   for i in s:
#       if not(answer):
#           answer.append(i)
#       else:
#           if(answer[-1] == i):
#               answer.pop()
#           else:
#               answer.append(i)    
#   return not(answer)
