def solution(brown, yellow):
  answer = []
  for i in range(1,(brown+yellow)//2+1):
    answer.append([i,(brown+yellow)/i])
  for a,b in answer:
    while a>=b:
      if a*2 + (b-2)*2 == brown:
        return [a,b]
      break